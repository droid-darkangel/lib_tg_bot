from aiogram import Dispatcher, Bot, executor, types


class Tg_Bot:
    """Your Telegram Bot for sent messages"""

    def __init__(self, token: str):
        """For settings, your Telegram Bot"""

        self.token = token
        self.bot = Bot(token)
        self.dp = Dispatcher(self.bot)
        self.executor = executor


    async def send_msg(self,
                       chat_id: int,
                       message: str,
                       reply_markup = None
                       ):
        """
        For sent message from your bot

        :param chat_id: chat ID user who used bot
        :param message: your message
        :param reply_markup: your markup for message, default None
        """

        await self.bot.send_message(chat_id=chat_id,
                                    text=message,
                                    reply_markup=reply_markup)

    async def send_photo(self,
                         chat_id: int,
                         photo: str):
        """
        For sent photo from your bot

        :param chat_id: chat id user who used bot
        :param photo: you're photoed
        """

        await self.bot.send_photo(chat_id=chat_id,
                                  photo=photo)


    def start_polling(self,
                      dp = None,
                      skip_updates = True,
                      on_startup = None,
                      on_shutdown = None):

        """
        For start using your Telegram Bot
        
        :param dp: Dispatcher, use bot.dp, default None
        :param skip_updates: False|True, default True
        :param on_startup: your define for startup, default None
        :param on_shutdown: your define for shutdown, default None\
        """

        self.executor.start_polling(dp,
                                    skip_updates=skip_updates,
                                    on_startup=on_startup,
                                    on_shutdown=on_shutdown)
