from lib import executor, Tg_Bot
from aiogram import types

token = ''

bot = Tg_Bot(token)


@bot.dp.message_handler(commands=['start'])
async def send_start_msg(msg: types.Message):
    print('worked')
    await bot.send_msg(chat_id=msg.from_user.id,
                       message=f'Hello, my friend {msg.from_user.first_name}'
                               f'')


if __name__ == "__main__":
    executor.start_polling(bot.dp, skip_updates=True)
