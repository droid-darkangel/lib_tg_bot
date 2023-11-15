from aiogram import Dispatcher, Bot, executor


class Tg_Bot:
    """You're Telegram Bot for sent messages"""

    def __init__(self, token: str):
        """For settings, you're Telegram Bot"""

        self.token = token
        self.bot = Bot(token)
        self.dp = Dispatcher(self.bot)

    async def send_msg(self,
                       chat_id: int,
                       message: str
                       ):
        """
        For sent message from you're bot

        parameters:

        chat_id: chat id user who used bot

        message: you're messaged
        """

        await self.bot.send_message(chat_id=chat_id,
                                    text=message)

    async def send_photo(self,
                         chat_id: int,
                         photo: str):
        """
        For sent photo from you're bot

        parameters:

        chat_id: chat id user who used bot

        photo: you're photoed
        """

        await self.bot.send_photo(chat_id=chat_id,
                                  photo=photo)
