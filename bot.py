from telethon import TelegramClient, events
from telethon.tl.types import User

api_id = 10953300
api_hash = '9c24426e5d6fa1d441913e3906627f87'

client = TelegramClient('session', api_id, api_hash)

async def delete_bot_chats():
    async for dialog in client.iter_dialogs():
        entity = dialog.entity

        if isinstance(entity, User) and entity.bot:
            try:
                await client.delete_dialog(entity)
                print(f"{entity.username} bot bilan chat o'chirildi.")
                
            except Exception as e:
                print(f"{entity.username} bot bilan chatni o'chirishda xatolik yuz berdi: {e}")

@client.on(events.NewMessage(pattern=r'^\.bot$'))
async def handle_bot_command(event):
    await delete_bot_chats()
    await event.reply("Barcha botlar bilan chatlar o'chirildi.")

client.start()
client.run_until_disconnected()
