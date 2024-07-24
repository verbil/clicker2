from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7183402840:AAHikl6aFATmA5RMHKTP28KZJ1U29FuCbqo')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.KeyboardButton("Play! Click!", web_app=WebAppInfo(url='https://verbil.github.io/clicker_new/')))

	await message.answer("""Привет!
		
Добро пожаловать в новый кликер в телеграме!. Тебе предстоит добывать RCoin. Что это? 

RCoin - новая эра новой эпохи кликеров. Кликай и прокачивай персонажа и получай монеты, за которые в будущем можно получить классные бонусы!

Как играть?

Команда /help подробно расскажет о всех тонкостях нашей игры. """, reply_markup=markup)

@dp.message_handler(commands=['help'])
async def start(message: types.Message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.KeyboardButton("Play! Click!", web_app=WebAppInfo(url='https://verbil.github.io/clicker_new/')))

	await message.answer("""🛠️ Помощь по игре

💰 В игре ты можешь добывать так называемую монету - RCoin. За один клик - +1 монета.
Так же в игре есть прогресс бар, при заполнении которого у тебя меняется уроверь и меняется кол-во монет за клик.

🫂 В игру скоро будет добавлена реферальная система. Ты сможешь приглашать друзей по специальной ссылке, а взамен тебе будут даваться 10% с монет друга.

📋 Ещё в игру скоро будет внедрена система заданий. Ты сможешь выполнять различные простые задания, а за них тебе будут добавлять монеты

Maybe nothing...""", reply_markup=markup)

executor.start_polling(dp)