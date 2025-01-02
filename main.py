import telebot

# Ваш токен Telegram-бота
API_TOKEN = 'ВАШ_ТОКЕН'

# Создаём бота
bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Привет! Я бот, который исполняет Python-код. Отправь мне код, и я исполню его!"
    )

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def execute_python(message):
    try:
        # Здесь мы используем exec(), чтобы интерпретировать Python-код
        local_variables = {}
        exec(message.text, {}, local_variables)

        # Если код имеет переменную result — вернём её значение
        result = local_variables.get('result', 'Код выполнен! Переменной result нет.')
        bot.reply_to(message, f"Результат выполнения:\n{result}")
    except Exception as e:
        # Обрабатываем ошибки и отправляем их пользователю
        bot.reply_to(message, f"Произошла ошибка:\n{e}")

# Запуск бота
print("Бот запущен...")
bot.infinity_polling()
