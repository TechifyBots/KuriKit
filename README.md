# 🧩 Kurikit

> A lightweight monkey patch that adds `client.listen()` support to Kurigram.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Kurigram](https://img.shields.io/badge/Kurigram-Compatible-blue?style=for-the-badge)](https://github.com/Kurimod/kurigram)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## ✨ Features

- 🎧 Adds `client.listen()` support to Kurigram
- ⏱️ Custom timeout support
- ♾️ Unlimited waiting with `timeout=None`
- 👤 User-specific message listening
- 🔍 Message filter support
- 🪶 Lightweight and simple
- 🔌 Works without modifying your existing handlers

---

## 📦 Installation

Install Kurikit directly from GitHub:

    pip install git+https://github.com/TechifyBots/Kurikit.git

---

## 🚀 Usage

Import Kurikit before using `client.listen()`:

    import kurikit

Then simply use:

    message = await client.listen(message.chat.id)

By default, `client.listen()` waits for **60 seconds**.

---

## ♾️ No Timeout

To wait indefinitely:

    message = await client.listen(
        message.chat.id,
        timeout=None
    )

---

## ⏱️ Custom Timeout

You can specify your own timeout:

    message = await client.listen(
        message.chat.id,
        timeout=120
    )

The above example waits for **120 seconds**.

---

## 👤 Listen From a Specific User

You can listen for a message from a specific user:

    message = await client.listen(
        message.chat.id,
        user_id=123456789
    )

---

## 🔍 Using Filters

Kurikit also supports message filters:

    from pyrogram import filters

    message = await client.listen(
        message.chat.id,
        filters=filters.text,
        timeout=None
    )

---

## 📋 Example

    from kurigram import Client
    import kurikit

    app = Client(
        "my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    @app.on_message()
    async def main(client, message):
        await message.reply("Send me a message...")

        response = await client.listen(
            message.chat.id,
            timeout=None
        )

        await response.reply(
            f"You sent: {response.text}"
        )

    app.run()

---

## ⚙️ Requirements

- Python 3.8+
- Kurigram

---

## 🤝 Contributing

Contributions, improvements, and bug reports are welcome.

Feel free to open an **Issue** or submit a **Pull Request**.

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Techify Bots**

[![GitHub](https://img.shields.io/badge/GitHub-TechifyBots-black?style=for-the-badge&logo=github)](https://github.com/TechifyBots)

---

⭐ If Kurikit is useful to you, consider giving the repository a star!
