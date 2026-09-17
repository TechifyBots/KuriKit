import asyncio
from pyrogram.types import Message
from pyrogram import Client, StopPropagation

if not getattr(Message, "_listen_patched", False):
    Message._listen_patched = True
    Message._original_parse = Message._parse

    @staticmethod
    async def _custom_parse(client, message, users, chats, *args, **kwargs):
        msg = await Message._original_parse(client, message, users, chats, *args, **kwargs)

        if hasattr(client, "listen_futures"):
            chat_id = getattr(getattr(msg, "chat", None), "id", None)
            user_id = getattr(getattr(msg, "from_user", None), "id", None)

            key = (chat_id, user_id)
            key_chat = (chat_id, None)

            future = client.listen_futures.pop(key, None)

            if future is None:
                future = client.listen_futures.pop(key_chat, None)

            if future is not None and not future.done():
                future.set_result(msg)
                raise StopPropagation

        return msg

    Message._parse = _custom_parse


async def custom_listen(self, chat_id, filters=None, timeout=60, user_id=None):
    if not hasattr(self, "listen_futures"):
        self.listen_futures = {}

    future = asyncio.get_running_loop().create_future()
    key = (chat_id, user_id) if user_id else (chat_id, None)

    self.listen_futures[key] = future

    try:
        if timeout is None:
            message = await future
        else:
            message = await asyncio.wait_for(future, timeout)

        if filters and not await filters(self, message):
            return await self.listen(chat_id, filters, timeout, user_id)

        return message

    except asyncio.TimeoutError:
        self.listen_futures.pop(key, None)
        raise


Client.listen = custom_listen