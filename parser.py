import requests
import datetime
import telebot
import sqlite3
import os
import random
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from datetime import datetime
from telebot import types
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

clear = lambda: os.system('cls')

url1 = 'https://game-tournaments.com/dota-2'

url2 = 'https://game-tournaments.com/csgo'

bot = telebot.TeleBot('TOKEN')

table_prof = []
table_analys = [{'ID': 457225002, 'NAME': 'Калы'}]



@bot.message_handler(commands=['help', 'start'])
def start(message):
    prof_idx = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('id')
    btn2 = types.KeyboardButton('Анализировать')
    btn3 = types.KeyboardButton('CS:GO')
    markup.add(btn1, btn2)
    send_mess = f"<b>Приветствую {message.from_user.first_name} ! </b>\nНапиши 'id', чтобы узнать id  "
    id1 = message.from_user.id
    name = message.from_user.first_name
    prof_idx = prof_idx + 1
    prof_idxa = prof_idx - 1
    table_prof.append({
        'ID': id1,
        'NAME': name
    })
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def mess(message):
            if message.text == 'id':
                print(table_prof)
                bot.send_message(message.chat.id, 'Ваш id:')
                bot.send_message(message.chat.id, table_prof[prof_idxa]['ID'])
                bot.send_message(message.chat.id, 'Теперь отправьте этот id: https://t.me/iamvalued')
            else:
                a = int(message.from_user.id)
                b = int(table_analys[prof_idxa]['ID'])
                print(a==b)
                if a==b:
                    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                    btn3 = types.KeyboardButton('CS:GO')
                    btn4 = types.KeyboardButton('DOTA 2')
                    markup1.add(btn3, btn4)
                    bot.send_message(message.chat.id, 'Выберите спорт', reply_markup=markup1)
                    if message.text == 'CS:GO':
                        idx = 0
                        num = 0
                        page = requests.get(url2)
                        soup = BeautifulSoup(page.content, "html.parser")
                        tables = soup.select('div[id^="block_matches_current"]')  # таблица с сайта
                        table1 = []
                        clear()
                        for table in tables:  # парсинг команд
                            bot.send_message(message.chat.id,
                                             '\n          Расписание матчей CS:GO (game-tournaments)\n')

                            trs = table.select('tr')

                            for tr in trs:
                                l = "LIVE (tested)"
                                if tr.attrs.get('class'):
                                    team1 = tr.select_one('.teamname.c1')
                                    team2 = tr.select_one('.teamname.c2')
                                    href = urljoin(url2, tr.select_one('.mlink').get('href'))
                                    bot.send_message(message.chat.id,
                                                     '{}. {} VS {} ({})'.format(idx + 1, team1.text.strip(),
                                                                                team2.text.strip(),
                                                                                l))
                                    table1.append({
                                        'NUMBER': idx + 1,
                                        'TEAM1': team1.text.strip(),
                                        'TEAM2': team2.text.strip(),
                                        'HREF': href})
                                    idx = idx + 1
                                else:
                                    team1 = tr.select_one('.teamname.c1')
                                    team2 = tr.select_one('.teamname.c2')
                                    href = urljoin(url2, tr.select_one('.mlink').get('href'))
                                    bot.send_message(message.chat.id,
                                                     '{}. {} VS {}'.format(idx + 1, team1.text.strip(),
                                                                           team2.text.strip()))
                                    idx = idx + 1
                                    table1.append({
                                        'NUMBER': num + 1,
                                        'TEAM1': team1.text.strip(),
                                        'TEAM2': team2.text.strip(),
                                        'HREF': href})
                                    num = num + 1
                        bot.send_message(message.chat.id, 'Введите номер матча: ')
                    elif message.text == 'DOTA 2':
                        idx = 0
                        num = 0
                        page = requests.get(url1)
                        soup = BeautifulSoup(page.content, "html.parser")
                        tables = soup.select('div[id^="block_matches_current"]')  # таблица с сайта
                        table1 = []
                        clear()
                        for table in tables:  # парсинг команд
                            bot.send_message(message.chat.id,
                                             '\n          Расписание матчей Dota 2 (game-tournaments)\n')

                            trs = table.select('tr')

                            for tr in trs:
                                l = "LIVE (tested)"
                                if tr.attrs.get('class'):
                                    team1 = tr.select_one('.teamname.c1')
                                    team2 = tr.select_one('.teamname.c2')
                                    href = urljoin(url1, tr.select_one('.mlink').get('href'))
                                    bot.send_message(message.chat.id,
                                                     '{}. {} VS {} ({})'.format(idx + 1, team1.text.strip(),
                                                                                team2.text.strip(),
                                                                                l))
                                    table1.append({
                                        'NUMBER': idx + 1,
                                        'TEAM1': team1.text.strip(),
                                        'TEAM2': team2.text.strip(),
                                        'HREF': href})
                                    idx = idx + 1
                                else:
                                    team1 = tr.select_one('.teamname.c1')
                                    team2 = tr.select_one('.teamname.c2')
                                    href = urljoin(url1, tr.select_one('.mlink').get('href'))
                                    bot.send_message(message.chat.id,
                                                     '{}. {} VS {}'.format(idx + 1, team1.text.strip(),
                                                                           team2.text.strip()))
                                    idx = idx + 1
                                    table1.append({
                                        'NUMBER': num + 1,
                                        'TEAM1': team1.text.strip(),
                                        'TEAM2': team2.text.strip(),
                                        'HREF': href})
                                    num = num + 1
                        bot.send_message(message.chat.id, 'Введите номер матча: ')
                else:
                    bot.send_message(message.chat.id,'Вам этот раздел не доступен, произведите оплату! Ваш Id:')
                    bot.send_message(message.chat.id, table_prof[prof_idxa]['ID'])










'''
def dota2():
    idx = 0
    num = 0
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.select('div[id^="block_matches_current"]')  # таблица с сайта

    # driver = webdriver.PhantomJS()
    clear()
    print('Подождите несколько секунд!')
    # wait = WebDriverWait(driver, 1000)

    # driver.get("https://game-tournaments.com/dota-2")
    # wait.until(EC.element_to_be_clickable((By.ID, "scrorepast")))

    # driver.find_element_by_id('scrorepast').click()
    table1 = []
    clear()
    for table in tables:  # парсинг команд
        print('\n          Расписание матчей Dota 2\n')

        trs = table.select('tr')

        for tr in trs:
            l = "LIVE (tested)"
            if tr.attrs.get('class'):
                team1 = tr.select_one('.teamname.c1')
                team2 = tr.select_one('.teamname.c2')
                href = urljoin(url1, tr.select_one('.mlink').get('href'))
                print('{}. {} VS {} ({})'.format(idx + 1, team1.text.strip(), team2.text.strip(), l))
                table1.append({
                    'NUMBER': idx + 1,
                    'TEAM1': team1.text.strip(),
                    'TEAM2': team2.text.strip(),
                    'HREF': href})
                idx = idx + 1
            else:
                team1 = tr.select_one('.teamname.c1')
                team2 = tr.select_one('.teamname.c2')
                href = urljoin(url1, tr.select_one('.mlink').get('href'))
                print('{}. {} VS {}'.format(idx + 1, team1.text.strip(), team2.text.strip()))
                idx = idx + 1
                table1.append({
                    'NUMBER': num + 1,
                    'TEAM1': team1.text.strip(),
                    'TEAM2': team2.text.strip(),
                    'HREF': href})
                num = num + 1
    print(table1)
    print('Введите номер матча: ')
    nummm = int(input())
    clear()
    numm = nummm - 1
    url = table1[numm]['HREF']
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.select('div[id^="block_matches_current"]')
    team1 = table1[numm]['TEAM1']
    team2 = table1[numm]['TEAM2']
    match = requests.get(url)
'''
'''
def csgo():
    idx = 0
    num = 0
    page = requests.get(url2)
    now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")  # текущая дата

    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.select('div[id^="block_matches_current"]')  # таблица с сайта

    # driver = webdriver.PhantomJS()
    clear()
    print('Подождите несколько секунд!')
    # wait = WebDriverWait(driver, 1000)

    # driver.get("https://game-tournaments.com/csgo")
    # wait.until(EC.element_to_be_clickable((By.ID, "scrorepast")))

    # driver.find_element_by_id('scrorepast').click()
    table1 = []
    clear()
    for table in tables:  # парсинг команд
        print('          Расписание матчей CS:GO\n')
        trs = table.select('tr')
        for tr in trs:
            l = "LIVE"
            if tr.attrs.get('class'):
                team1 = tr.select_one('.teamname.c1')
                team2 = tr.select_one('.teamname.c2')
                href = urljoin(url2, tr.select_one('.mlink').get('href'))
                print('{}. {} VS {} ({})'.format(idx + 1, team1.text.strip(), team2.text.strip(), l))
                table1.append({
                    'NUMBER': idx + 1,
                    'TEAM1': team1.text.strip(),
                    'TEAM2': team2.text.strip(),
                    'HREF': href})
                idx = idx + 1
            else:
                team1 = tr.select_one('.teamname.c1')
                team2 = tr.select_one('.teamname.c2')
                href = urljoin(url2, tr.select_one('.mlink').get('href'))
                print('{}. {} VS {}'.format(idx + 1, team1.text.strip(), team2.text.strip()))
                idx = idx + 1
                table1.append({
                    'NUMBER': num + 1,
                    'TEAM1': team1.text.strip(),
                    'TEAM2': team2.text.strip(),
                    'HREF': href})
                num = num + 1
'''



bot.polling(none_stop=True)
