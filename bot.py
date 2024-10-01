import telebot
""" from keep_alive import keep_alive
keep_alive() """
from datetime import datetime
from telebot import types
import os
import pytz

day_number = datetime.today().weekday()

if day_number <= 5:
    day_now = 'weekday'
else:
    day_now = 'holiday'

# Ваши расписания
bus_schedule_weekday_from_Minsk = {...}
bus_schedule_weekday_to_Minsk = {...}
bus_schedule_holiday_from_Minsk = {...}
bus_schedule_holiday_to_Minsk = {...}


#bot = telebot.TeleBot(token=os.environ.get('token'))


bot = telebot.TeleBot('7537092117:AAHeVSZK5AFO_FWzRZf4B6BuPmNKiEuUBHQ')


bus_schedule_weekday_from_Minsk = {
    '323': ["06:20", "07:10", "07:43", "08:05", "08:25", "09:10", "09:25", "10:00", "10:20", "11:10", "11:40", "12:25", "12:40", "13:00", "13:55", "14:10", "14:37", "15:05", "15:35", "16:07", "16:29", "17:07", "17:24", "17:44", "18:42", "18:59", "19:14", "20:05", "20:30", "21:05", "21:30", "22:20"],

    '429': ["06:34", "06:44", "06:55", "07:05", "07:15", "07:25", "07:36", "07:44", "07:55", "08:15", "08:27", "08:50", "09:22", "09:40", "10:27", "11:27", "11:54", "12:02", "12:10", "12:41", "13:10", "14:05", "14:32", "14:45", "15:03", "15:20", "15:29", "15:55", "16:11", "16:19", "16:28", "16:38", "16:48", "16:58", "17:17", "17:26", "17:41", "17:48", "18:05", "18:23", "18:47", "19:01", "19:42", "20:29", "20:54", "21:06", "21:15", "21:41", "22:36", "22:58", "23:08", "23:38", "00:10"],

    '31': ["07:00", "07:15", "07:27", "07:37", "07:47", "07:57", "08:07", "08:17", "08:27", "08:37", "08:49", "09:01", "09:13", "09:26", "09:39", "09:52", "10:05", "10:20", "10:35", "10:50", "11:05", "11:20", "11:35", "11:50", "12:05", "12:20", "12:35", "12:50", "13:05", "13:20", "13:33", "13:46", "13:59", "14:12", "14:25", "14:38", "14:52", "15:03", "15:16", "15:29", "15:41", "15:53", "16:03", "16:13", "16:24", "16:33", "16:42", "16:52", "17:02", "17:11", "17:20", "17:29", "17:39", "17:47", "17:57", "18:07", "18:17", "18:28", "18:38", "18:48", "18:59", "19:09", "19:19", "19:29", "19:39", "19:50", "20:02", "20:14", "20:27", "20:38", "20:50", "21:02", "21:14", "21:26", "21:38", "21:52", "22:04", "22:17", "22:30", "22:44"],

    '45': [":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":", ":"]
}

bus_schedule_weekday_to_Minsk = {
    '323': ["06:19", "06:52", "07:02", "07:29", "07:59", "08:22", "08:49", "09:07", "09:49", "10:08", "10:43", "11:03", "12:08", "12:23", "13:03", "13:18", "13:38", "14:03","14:33", "14:58", "15:18", "15:53", "16:13", "16:48", "17:13", "17:46", "18:03", "18:23", "18:58", "19:21", "19:37", "19:57", "20:52", "21:12", "21:52"],

    '429': ["05:53", "06:24", "06:36", "06:44", "06:51", "06:59", "07:03", "07:10", "07:17", "07:25", "07:34", "07:48", "08:03", "08:12", "08:22", "08:32", "08:41", "08:51", "09:01", "09:12", "09:22", "09:34", "09:56", "10:23", "10:38", "10:53", "11:23", "11:53", "12:23", "12:48", "12:56", "13:11", "13:45", "14:17", "15:05", "15:17", "15:31", "15:46", "16:05", "16:15", "16:25", "16:52", "17:16", "17:23", "17:31", "17:44", "17:57", "18:15", "18:25", "18:42", "19:16", "19:39", "19:56", "20:13", "20:31", "20:53", "21:25", "21:38", "21:56", "22:16", "22:24", "23:05", "23:19", "23:41"],
    '31': ["06:25", "06:40", "07:02", "07:11", "07:20", "07:29", "07:38", "07:47", "07:56",  "08:05", "08:15", "08:25", "08:35", "08:45", "08:55",  "09:05", "09:15", "09:27", "09:39", "09:51",  "10:04", "10:17", "10:30", "10:45",  "11:00", "11:15", "11:30", "11:45",  "12:00", "12:15", "12:30", "12:45",  "13:00", "13:15", "13:30", "13:45",  "14:00",  "15:05", "15:18", "15:31", "15:44", "15:57",  "16:09", "16:21", "16:33", "16:43", "16:53:", "17:02", "17:12", "17:22", "17:32", "17:42", "17:52",  "18:01", "18:11", "18:21", "18:31", "18:41", "18:51", "19:01", "19:11", "19:21", "19:31", "19:41", "19:51",  "20:01", "20:12", "20:24", "20:37", "20:50",  "21:03", "21:16",  "22:02", "22:16"],

    '45': []
}

bus_schedule_holiday_from_Minsk = {
    '323': ["06:30", "07:20", "08:15", "09:20", "10:15", "11:00", "11:45", "12:30", "14:15", "15:15", "16:15", "17:10", "19:07", "20:10", "21:15", "22:15"],

    '429': ["06:35", "07:10", "07:35", "08:12", "08:38", "09:15", "10:35", "11:30", "12:00", "12:30", "13:00", "13:30", "14:01", "14:35", "15:10", "15:32", "16:05", "16:26", "17:00", "17:40", "18:13", "19:05", "19:22", "19:59", "20:41", "21:18", "21:50", "23:09", "23:45"],

    '31': ["07:10", "07:35", "07:55", "08:15", "08:35", "08:55", "09:15", "09:35", "09:50", "10:10", "10:25", "10:45", "11:05", "11:22", "11:38", "11:52", "12:05", "12:20", "12:35", "12:55", "13:15", "13:35", "13:52", "14:10", "14:25", "14:40", "14:55", "15:10", "15:25", "15:40", "15:55", "16:10", "16:25", "16:40", "16:55", "17:10", "17:25", "17:45", "18:00", "18:20", "18:40", "18:55", "19:15", "19:30", "19:50", "20:10", "20:30", "20:50", "21:10", "21:30", "22:00", "22:30", "23:00"],

    '45': []
}

bus_schedule_holiday_to_Minsk = {
    '323': ["06:14", "07:09", "07:59","08:54", "09:58", "10:53", "11:38", "12:23","13:13", "14:03", "15:08", "16:08", "17:03", "17:58", "18:48", "19:57", "21:07", "22:07"],

    '429': ["06:38", "07:18", "07:38", "08:15", "08:47", "09:20", "09:40", "10:18", "10:56", "11:36", "11:56", "12:33", "13:06", "13:46", "14:06", "14:36", "15:06", "15:41", "16:03", "16:37", "17:28", "18:03", "18:31", "19:01", "19:28", "20:08", "20:28", "21:34", "22:34", "23:04"],

    '31': ["06:35",  "07:00", "07:20", "07:40",  "08:00", "08:20", "08:40",  "09:00", "09:20", "09:35", "09:55",  "10:15", "10:30", "10:48",  "11:02", "11:22", "11:42",  "12:00", "12:15", "12:30", "12:45",  "13:00", "13:15", "13:35", "13:55",  "14:12",  "15:05", "15:20", "15:35", "15:50",  "16:05", "16:17", "16:35", "16:50",  "17:05", "17:20", "17:35", "17:50",  "18:05", "18:25", "18:40", "18:57",  "19:17", "19:35", "19:55",  "20:20", "20:50",  "21:20", "21:49",  "22:19"],

    '45': []
}

bus_number = None
path = None

# Логика выбора расписания на будни
def weekday_choose_bus(message):
    markup = types.InlineKeyboardMarkup()
    button1_weekday = types.InlineKeyboardButton("323", callback_data="bus_323_weekday")
    button2_weekday = types.InlineKeyboardButton("429", callback_data="bus_429_weekday")
    button3_weekday = types.InlineKeyboardButton("31", callback_data="bus_31_weekday")
    button4_weekday = types.InlineKeyboardButton("45", callback_data="bus_45_weekday")
    markup.row(button1_weekday, button2_weekday)
    markup.row(button3_weekday, button4_weekday)
    bot.send_message(message.chat.id, "Choose a bus for weekday", reply_markup=markup)

# Логика выбора расписания на выходные
def holiday_choose_bus(message):
    markup = types.InlineKeyboardMarkup()
    button1_holiday = types.InlineKeyboardButton("323", callback_data="bus_323_holiday")
    button2_holiday = types.InlineKeyboardButton("429", callback_data="bus_429_holiday")
    button3_holiday = types.InlineKeyboardButton("31", callback_data="bus_31_holiday")
    button4_holiday = types.InlineKeyboardButton("45", callback_data="bus_45_holiday")
    markup.row(button1_holiday, button2_holiday)
    markup.row(button3_holiday, button4_holiday)
    bot.send_message(message.chat.id, "Choose a bus for holiday", reply_markup=markup)

# Функция для получения времени следующего автобуса
def get_next_bus_time(bus_number, schedule):
    tz = pytz.timezone('Europe/Minsk')
    current_time = datetime.now(tz)
    upcoming_buses = []
    
    for bus_time in schedule.get(bus_number, []):
        if bus_time != ":":
            bus_time_obj = datetime.strptime(bus_time, '%H:%M').time()
            if bus_time_obj > current_time.time():
                upcoming_buses.append(bus_time)

    if upcoming_buses:
        return upcoming_buses[:4]  # Возвращаем ближайшие 2 автобуса
    else:
        return ["No more buses for today."]

# Обработчик команды /bus
@bot.message_handler(commands=['bus'])
def path_bus(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("to Minsk", callback_data="to_Minsk")
    button2 = types.InlineKeyboardButton("from Minsk", callback_data="from_Minsk")
    markup.row(button1, button2)
    bot.reply_to(message, "Choose a path", reply_markup=markup)

# Обработчик нажатий на кнопки (callback_data)
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global bus_number, path
    
    if callback.data == "to_Minsk":
        path = "to_Minsk"
        if day_now == 'weekday':
            weekday_choose_bus(callback.message)  # Будний день
        else:
            holiday_choose_bus(callback.message)  # Выходной
    elif callback.data == "from_Minsk":
        path = "from_Minsk"
        if day_now == 'weekday':
            weekday_choose_bus(callback.message)  # Будний день
        else:
            holiday_choose_bus(callback.message)  # Выходной
    elif callback.data.startswith('bus_'):
        bus_number = callback.data.split('_')[1]
        
        # Определение расписания в зависимости от направления и дня
        if path == "to_Minsk":
            if day_now == 'weekday':
                schedule = bus_schedule_weekday_to_Minsk
            else:
                schedule = bus_schedule_holiday_to_Minsk
        else:
            if day_now == 'weekday':
                schedule = bus_schedule_weekday_from_Minsk
            else:
                schedule = bus_schedule_holiday_from_Minsk
        
        # Получение ближайших автобусов
        next_buses = get_next_bus_time(bus_number, schedule)
        bot.send_message(callback.message.chat.id, f"Next buses: {', '.join(next_buses)}")

bot.polling(non_stop=True)