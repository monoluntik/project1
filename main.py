import logging
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime
from write_to_exel import write_to_exel
API_TOKEN = '5235054996:AAEDhSdKv7c3NiZxRVaPT5CKQoQ9FlqQEsM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

class Just:
    def __init__(self, id, work_space):
        self.id = id
        self.work_space = work_space
        self.name = None
        self.model = None
        self.quantity = None
        

    def __str__(self):
        return f"{self.id}"

just_list = []

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Цех 1", "Цех 2", "Цех 3", "Цех 4", "Цех 5", "Цех 6"]
    keyboard.add(*buttons)
    await message.answer("Выберите цех:", reply_markup=keyboard)

@dp.message_handler(lambda message: "Цех" in message.text )
async def cmd_start(message: types.Message):
    li = [i for i in just_list if i.id == message.chat.id]
    if li != []:
        del just_list[just_list.index(li[0])]
    just = Just(message.chat.id, message.text)
    just_list.append(just)
    await message.answer("Введите данные\nИмя:\nМодель:\nКоличество:")

@dp.message_handler()
async def get_data(message: types.Message):
    li = [i for i in just_list if i.id == message.chat.id][0]
    data = message.text.split('\n')
    dt = datetime.now()
    data.append(f'{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}')
    data.append(li.work_space)
    write_to_exel(data)
    await message.answer("Данные сохранены.")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)