from telethon import TelegramClient
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.contacts import GetContactsRequest
import asyncio
import qrcode

# Replace with your API credentials from my.telegram.org
api_id = '<get this from your account>'
api_hash = '<get this from your account>'

async def main():
    client = TelegramClient("session", api_id, api_hash)

    await client.connect()
    if not await client.is_user_authorized():
        print(">> Generating QR code, scan it in Telegram (Settings > Devices > Link Desktop Device)")
        qr_login = await client.qr_login()
        qr = qrcode.QRCode()
        qr.add_data(qr_login.url)
        qr.make(fit=True)
        qr.print_ascii(invert=True)
        await qr_login.wait()

    # 🔹 Get contact list
    result = await client(GetContactsRequest(hash=0))
    contacts = result.users

    # 🔹 Iterate through contacts
    for contact in contacts:
        try:
            await client(DeleteHistoryRequest(
                peer=contact.id,
                max_id=0,
                just_clear=False,
                revoke=True  # delete for both sides
            ))
            print(f"✅ Deleted chat with {contact.first_name or contact.username}")
        except Exception as e:
            print(f"❌ Could not delete {contact.first_name or contact.username}: {e}")

    await client.disconnect()

asyncio.run(main())
