# 🧹 delete-telegram-chatlists
A Python script using [Telethon](https://github.com/LonamiWebs/Telethon) that deletes all private chats with your contacts in Telegram.  
Supports QR code login (no phone/code needed) and removes chats for both you and the other person.

## ✨ Features

- 🔑 Login with **QR code** (secure, no need to store phone number).
- 📇 Iterates through your **contact list only** (skips groups, channels, bots).
- 🗑️ Deletes entire chat history for both sides (`revoke=True`).
- ⚡ Fast bulk execution (100+ chats at once).
- 📦 Works on macOS, Linux, and Windows.

## 🔧 Usage

1. Get your **API ID** and **API Hash** from [my.telegram.org](https://my.telegram.org/apps).  
2. Add them in `delete.py`.  
3. Run:
   ```bash python delete.py```
4. Scan the QR code shown in terminal (Settings > Devices > Link Desktop Device).

The script will remove all chats with your contacts.

## ⚠️ Limitations

- Works only with private 1-to-1 chats.
- In groups/channels, deletion applies only to your side.
- Forwarded messages outside the chat can’t be recalled.
