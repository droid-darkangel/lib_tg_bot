from lib import Tg_Bot, types

token = ''

bot = Tg_Bot(token)

def on_startup():
    print("I'm working")


@bot.dp.message_handler(commands=['start'])
async def send_start_msg(msg: types.Message):
    print('worked')
    await bot.send_msg(chat_id=msg.from_user.id,
                       message=f'Hello, my friend {msg.from_user.first_name}')


if __name__ == "__main__":
    bot.start_polling(bot.dp, on_startup=on_startup())
