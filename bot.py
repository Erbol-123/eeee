from aiogram import types, executor,Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext


from my_buttons import main_menu
api = '7420564756:AAEGT3vrMhoBePFtYHv2iYBIQYhktAS6kpY'
bot = Bot(api)
storage = MemoryStorage()
dp  =Dispatcher(bot,storage=storage)


class CourceState(StatesGroup):
    qaysisi= State()
    waqiti = State()
    fio = State()





@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer('Assalamu aleykum',
                     reply_markup=main_menu)
    
@dp.message_handler(text='Videosabaqlar')
async def send_videourok(sms:types.Message):
    video  = open(file='',mode='rb')
    await sms.answer_video(
        video=video,
        caption='Bul 1 sabaq'
    )



@dp.message_handler(text='Kursqa jaziliw')
async def send_response(sms:types.Message):
    await sms.answer('Axa, qanday kursqa jazilmaqshisiz?')
    await CourceState.qaysisi.set()

@dp.message_handler(state=CourceState.qaysisi)
async def send_qaysisi(sms:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['qaysisi']=sms.text
    await sms.answer(text='Endi qanday waqitqa kele alasiz?')
    await CourceState.waqiti.set()


@dp.message_handler(state=CourceState.waqiti)
async def send_waqiti(sms:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['waqiti']=sms.text
    await sms.answer(text='atiniz jane nomerinizdi jazip qaldirin')
    await CourceState.fio.set()

@dp.message_handler(state=CourceState.fio)
async def send_fio(sms:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['fio']=sms.text    
    await bot.send_message(
        chat_id=6538857550,
        text=f'''Sizge jana oqiwhsi jazildi:

{data['qaysisi']} - kursina,
{data['waqiti']} saatda,
{data['fio']} fio '''
    )
    await state.finish()

    





if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)


    




