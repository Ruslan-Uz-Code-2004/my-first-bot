from distutils.command.config import config
import json
import logging
import os
from config import token
from aiogram.utils.markdown import hbold, hlink
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import asyncio
from cs_skins_get import collect_data

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
db = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@db.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['💲Валюта', '📰Новости',
                     '🎮Топ игр', '🔥Скины CsGo со скидкой']
    keayboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keayboard.add(*start_buttons)
    await message.answer('Выберите категорию', reply_markup=keayboard)


@db.message_handler(Text(equals='💲Валюта'))
async def get_discount_many(message: types.Message):
    await message.answer('Пожалуйста подожди ...')
    with open('../result_mant_price.json', encoding='utf-8') as file:
        data = json.load(file)
    for index, item in enumerate(data[:5]):
        card = f"{hlink(item.get('CcyNm_RU'),item.get('Date'))}\n"\
            f"{hbold('Курс: ')}{item.get('Rate')}%\n" \
            f"{hbold('Наминал: ')}${item.get('Nominal')}🔥"
        if index % 20 == 0:
            await asyncio.sleep(3)
        await message.answer(card)


@db.message_handler(Text(equals='🎮Топ игр'))
async def get_discount_many(message: types.Message):
    await message.answer('Пожалуйста подожди ...')
    with open('../result.json', encoding='utf-8') as file:
        data = json.load(file)
    for index, item in enumerate(data):
        card = f"{hlink(item.get('article_title'),item.get('article_urls'))}\n🔥"
        if index % 20 == 0:
            await asyncio.sleep(3)
        await message.answer(card)


@db.message_handler(Text(equals='📰Новости'))
async def get_discount_many(message: types.Message):
    await message.answer('Пожалуйста подожди ...')
    with open('../result_information.json', encoding='utf-8') as file:
        data = json.load(file)
    for index, item in enumerate(data[:15]):
        card = f"{hlink(item.get('article_title'),item.get('article_urls'))}\n"\
            f"{hbold('Краткая информация ')}{item.get('article_text')}%\n"\
            f"{hbold('Дата публикации ')}{item.get('article_data')}%🔥\n"
        if index % 20 == 0:
            await asyncio.sleep(6)
        await message.answer(card)


@db.message_handler(Text(equals='🔥Скины CsGo со скидкой'))
async def start(message: types.Message):
    start_buttons = ['🔪Ножи', '🧤Перчатки', '🔫Снайперские винтовки']
    keayboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keayboard.add(*start_buttons)
    await message.answer('Выберите каткгорию', reply_markup=keayboard)


@db.message_handler(Text(equals='🔪Ножи'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подожди ...')
    collect_data()
    with open('../result_cs.json', encoding='utf-8') as file:
        data = json.load(file)
    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'),item.get('3d'))}\n"\
            f"{hbold('Скидка: ')}{item.get('overprice')}%\n" \
            f"{hbold('Стоимость: ')}${item.get('price')}🔥"
        if index % 20 == 0:
            await asyncio.sleep(5)
        await message.answer(card)


@db.message_handler(Text(equals='🔫Снайперские винтовки'))
async def get_discount_guns(message: types.Message):
    await message.answer('Пожалуйста подожди ...')
    collect_data(cat_type=4)
    with open('../result_cs.json', encoding='utf-8') as file:
        data = json.load(file)
    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'),item.get('3d'))}\n"\
            f"{hbold('Скидка: ')}{item.get('overprice')}%\n" \
            f"{hbold('Стоимость: ')}${item.get('price')}🔥"
        if index % 20 == 0:
            await asyncio.sleep(5)
        await message.answer(card)


@db.message_handler(Text(equals='🧤Перчатки'))
async def get_discount_perch(message: types.Message):
    await message.answer('Пожалуйста подожди ...')
    collect_data(3)
    with open('../result_cs.json', encoding='utf-8') as file:
        data = json.load(file)
    for index, item in enumerate(data):
        card = f"{hlink(item.get('full_name'),item.get('3d'))}\n"\
            f"{hbold('Скидка: ')}{item.get('overprice')}%\n" \
            f"{hbold('Стоимость: ')}${item.get('price')}🔥"
        if index % 20 == 0:
            await asyncio.sleep(5)
        await message.answer(card)


def main():
    executor.start_polling(db)


if __name__ == '__main__':
    main()
