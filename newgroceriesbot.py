from aiogram.utils import executor
from create_bot import dp
from aiogram import types



async def on_startup(_):
    print('Бот вышел в онлайн')

from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)


#@dp.message_handler()
#async def echo_send(message : types.Message):
    #if message.text == 'Привет':
        #await message.answer('Я Вас категорически приветствую!')
    
    #elif message.text == 'привет':
        #await message.answer('Я Вас категорически приветствую!')
    
    #elif message.text == '👋':
        #await message.answer('Я Вас категорически приветствую!')
    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)