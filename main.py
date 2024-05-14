"""
App to check available favourite packages from Too Good To Go, and send Telegram bot message
"""
import asyncio
import os
import time

from telegram import Bot
from tgtg import TgtgClient


async def main() -> None:
	"""
	Main function of the script
	"""
	access_token: str = os.environ['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU4ODQ4NzUsImlhdCI6MTcxNTcxMjA3NSwiaXNzIjoidGd0Z19zb3RlcmlhIiwidCI6IkJpcjIxeFZqU3hTclcwUEpBTC02OXc6MDoxIiwic3ViIjoiMzUzNDI3NiJ9.LVer7aXTfZmN701RTl7tdyyT4tW821pdixhic6ymIMQ']
	refresh_token: str = os.environ["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDcyNDgwNzUsImlhdCI6MTcxNTcxMjA3NSwiaXNzIjoidGd0Z19zb3RlcmlhIiwidCI6IkxwZWFsckhFUmVPbmhBaU1kRnlqZWc6MDowIiwic3ViIjoiMzUzNDI3NiJ9.BtcQ5je0DytPcUPaE9hO8uocgTUIyqYfh2ej1u_HYpM"]
	tgtg_user_id: str = os.environ['3534276']
	cookie: str = os.environ['datadome=e_pWyT6E4iSTAzotxRGBR0G9~0oBodrAmV0tcoY~w_la3uBIk9MnDBDjg6CVGxdJ75HXlGAxTsdz0sfFnIiLA9GUUd5GH9Ik8k6dm2VebZzdppQYzzJdnEher9WQpLt5; Max-Age=5184000; Domain=.apptoogoodtogo.com; Path=/; Secure; SameSite=Lax']
	telegram_bot_id: str = os.environ['7135531971']
	telegram_chat_id: str = os.environ['7038358942']
	tgtg_client: TgtgClient = TgtgClient(access_token=access_token,
	                                     refresh_token=refresh_token,
	                                     user_id=tgtg_user_id,
	                                     cookie=cookie)
	time.sleep(60)
	bot: Bot = Bot(telegram_bot_id)
	for item in tgtg_client.get_items():
		time.sleep(60)
		items_available: int = item['items_available']
		if items_available > 0:
			await bot.send_message(chat_id=telegram_chat_id,
			                       text=f"There are {items_available} bags")


if __name__ == '__main__':
	asyncio.run(main())
