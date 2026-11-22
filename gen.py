from pyrogram import Client
api_id = int(input("API_ID: "))
api_hash = input("API_HASH: ")
with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
    print("--- انسخ السطر اللي تحت ده كله ---")
    print(app.export_session_string())
