import environs
from telebot import TeleBot, types
from pycoingecko import CoinGeckoAPI

env = environs.Env()
env.read_env('.env')
BOT_TOKEN = env('BOT_TOKEN')

api = CoinGeckoAPI()
bot = TeleBot(token=BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Узнать стоимость монеты")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Я бот по проверки стоимости крипто монет.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def buttons_handler(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="😇 Привеет.. Спасибо что запустил меня!)")
    elif(message.text == "❓ Узнать стоимость монеты"):
        send = bot.send_message(message.chat.id, text="💰 Напиши название монеты на английском")
    else:
        crypto_id = message.text.lower()
        price_usd = api.get_price(ids=crypto_id, vs_currencies='usd')
        price_rub = api.get_price(ids=crypto_id, vs_currencies='rub')
        if price_usd:
            price_usd = price_usd[crypto_id]['usd']
            price_rub = price_rub[crypto_id]['rub']
        else:
            bot.send_message(message.chat.id, "😥 Такая криптовалюта не найдена ...")
            return
        bot.send_message(message.chat.id, f"Цена {crypto_id}:\n{price_usd} USD\n{price_rub} RUB")

bot.polling(none_stop=True)
