from telebot import types
import telebot
import os


token = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "Здравствуйте, {0.first_name}.\nДобро пожаловать в бот магазина YoungTEA.\n"
                                           "Команда /info кратко расскажет Вам о нашем бренде, команда /catalog "
                                           "поможет вам выбрать одежду из"
                                           " предложенных категорий, а команда /contacts ознакомит Вас с нашими контактными данными".format(message.from_user))


@bot.message_handler(commands=['info'])
def start_message(message): 
    bot.send_message(message.from_user.id, "Бренд YoungTEA основан в 2017 году в городе Санкт-Петербург."
                                           " Наша миссия — показать, что гардероб молодежи может состоять не только из"
                                           " худи и кроссовок. Все модели бренда передают эстетику тихого осеннего"
                                           " вечера с чашкой чая и книгой в руках.")


@bot.message_handler(commands=['contacts'])
def start_message(message):
    bot.send_message(message.from_user.id, "Номер телефона и почта для связи: +7 (929) 645-**-**, youngtea_support@proekt.ru\nНаш адрес: г.Москва, м.Войковская, ул.Пушкина, д.17")


@bot.message_handler(commands=['catalog'])
def start_message(message):
    global markup_1, markup_2, markup_3, markup_4, markup_5, markup_6, markup_7, markup_8, markup_9, markup_10
    markup_1 = types.InlineKeyboardMarkup(row_width=2)
    markup_2 = types.InlineKeyboardMarkup(row_width=2)
    markup_3 = types.InlineKeyboardMarkup(row_width=2)
    markup_4 = types.InlineKeyboardMarkup(row_width=2)
    markup_5 = types.InlineKeyboardMarkup(row_width=2)
    markup_6 = types.InlineKeyboardMarkup(row_width=2)
    markup_7 = types.InlineKeyboardMarkup(row_width=2)
    markup_8 = types.InlineKeyboardMarkup(row_width=2)
    markup_9 = types.InlineKeyboardMarkup(row_width=2)
    markup_10 = types.InlineKeyboardMarkup(row_width=2)
    del_item1 = types.InlineKeyboardButton('Назад', callback_data='delete1')
    del_item2 = types.InlineKeyboardButton('Назад', callback_data='delete2')
    man_item = types.InlineKeyboardButton('Мужская  одежда', callback_data='man_catalog')
    woman_item = types.InlineKeyboardButton('Женская одежда', callback_data='woman_catalog')
    man_1 = types.InlineKeyboardButton('Верхняя одежда', callback_data='man_1')
    man_2 = types.InlineKeyboardButton('Брюки / шорты', callback_data='man_2')
    man_3 = types.InlineKeyboardButton('Обувь', callback_data='man_3')
    woman_1 = types.InlineKeyboardButton('Верхняя одежда', callback_data='woman_1')
    woman_2 = types.InlineKeyboardButton('Юбки / шорты', callback_data='woman_2')
    woman_3 = types.InlineKeyboardButton('Обувь', callback_data='woman_3')
    item_1 = types.InlineKeyboardButton('Ботинки мужские', callback_data='catalog_1')
    item_2 = types.InlineKeyboardButton('Брюки мужские', callback_data='catalog_2')
    item_3 = types.InlineKeyboardButton('Жилет мужской', callback_data='catalog_3')
    item_4 = types.InlineKeyboardButton('Кардиган', callback_data='catalog_4')
    item_5 = types.InlineKeyboardButton('Костюм мужской', callback_data='catalog_5')
    item_6 = types.InlineKeyboardButton('Костюм женский', callback_data='catalog_6')
    item_7 = types.InlineKeyboardButton('Лоферы', callback_data='catalog_7')
    item_8 = types.InlineKeyboardButton('Пальто мужское', callback_data='catalog_8')
    item_9 = types.InlineKeyboardButton('Пальто женское', callback_data='catalog_9')
    item_10 = types.InlineKeyboardButton('Платье', callback_data='catalog_10')
    item_11 = types.InlineKeyboardButton('Рубашка', callback_data='catalog_11')
    item_12 = types.InlineKeyboardButton('Свитер', callback_data='catalog_12')
    item_13 = types.InlineKeyboardButton('Туфли женские', callback_data='catalog_13')
    item_14 = types.InlineKeyboardButton('Шорты утепленные', callback_data='catalog_14')
    item_15 = types.InlineKeyboardButton('Юбка', callback_data='catalog_15')
    markup_1.add(man_item, woman_item)
    markup_2.add(man_1, man_2, man_3, del_item1)
    markup_3.add(woman_1, woman_2, woman_3, del_item1)
    markup_4.add(item_3, item_4, item_5, item_8, item_11, item_12, del_item1)
    markup_5.add(item_6, item_9, item_10, del_item1)
    markup_6.add(item_2, item_14, del_item1)
    markup_7.add(item_15, item_14, del_item1)
    markup_8.add(item_1, del_item1)
    markup_9.add(item_13, item_7, del_item1)
    markup_10.add(del_item2)
    bot.send_message(message.chat.id, text='Выберите интересующую Вас категорию:', reply_markup=markup_1)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'man_catalog':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующую Вас категорию:', reply_markup=markup_2)
        if call.data == 'delete1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите интересующую Вас категорию:',
                                  reply_markup=markup_1)
        if call.data == 'delete2':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.send_message(call.message.chat.id, text='Выберите интересующую Вас категорию:', reply_markup=markup_1)
        if call.data == 'man_1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующий Вас товар:',
                             reply_markup=markup_4)
        if call.data == 'man_2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующий Вас товар:',
                             reply_markup=markup_6)
        if call.data == 'man_3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующий Вас товар:',
                             reply_markup=markup_8)
        if call.data == 'woman_catalog':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующую Вас категорию:', reply_markup=markup_3)
        if call.data == 'woman_1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующий Вас товар:',
                             reply_markup=markup_5)
        if call.data == 'woman_2':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующий Вас товар:',
                             reply_markup=markup_7)
        if call.data == 'woman_3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите интересующий Вас товар:',
                             reply_markup=markup_9)
        if call.data == 'catalog_1':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('ботинки муж.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Ботинки мужские\n'
                                                              'Артикул: 001\n'
                                                              'Цена: 3500', reply_markup=markup_10)
        elif call.data == 'catalog_2':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('брюки муж.jpg', "rb")
            bot.send_photo(call.message.chat.id, img, caption='Брюки мужские\n'
                                                              'Артикул: 002\n'
                                                              'Цена: 2400', reply_markup=markup_10)
        elif call.data == 'catalog_3':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('жилет.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Жилет мужской\n'
                                                              'Артикул: 003\n'
                                                              'Цена: 1800', reply_markup=markup_10)
        elif call.data == 'catalog_4':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('кардиган.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Кардиган\n'
                                                              'Артикул: 004\n'
                                                              'Цена: 2300', reply_markup=markup_10)
        elif call.data == 'catalog_5':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('костюм муж.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Костюм мужской\n'
                                                              'Артикул: 005\n'
                                                              'Цена: 5800', reply_markup=markup_10)
        elif call.data == 'catalog_6':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('костюм.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Костюм женский\n'
                                                              'Артикул: 006\n'
                                                              'Цена: 6000', reply_markup=markup_10)
        elif call.data == 'catalog_7':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('лоферы жен.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Лоферы\n'
                                                              'Артикул: 007\n'
                                                              'Цена: 2100', reply_markup=markup_10)
        elif call.data == 'catalog_8':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('пальто муж.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Пальто мужское\n'
                                                              'Артикул: 008\n'
                                                              'Цена: 4900', reply_markup=markup_10)
        elif call.data == 'catalog_9':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('пальто.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Пальто женское\n'
                                                              'Артикул: 009\n'
                                                              'Цена: 6300', reply_markup=markup_10)
        elif call.data == 'catalog_10':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('платье.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Платье\n'
                                                              'Артикул: 010\n'
                                                              'Цена: 1900', reply_markup=markup_10)
        elif call.data == 'catalog_11':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('рубашка.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Рубашка\n'
                                                              'Артикул: 011\n'
                                                              'Цена: 1500', reply_markup=markup_10)
        elif call.data == 'catalog_12':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('свитер муж.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Свитер\n'
                                                              'Артикул: 012\n'
                                                              'Цена: 2400', reply_markup=markup_10)
        elif call.data == 'catalog_13':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('туфли жен.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Туфли женские\n'
                                                              'Артикул: 013\n'
                                                              'Цена: 2600', reply_markup=markup_10)
        elif call.data == 'catalog_14':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('шорты.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Шорты утепленные\n'
                                                              'Артикул: 014\n'
                                                              'Цена: 1600', reply_markup=markup_10)
        elif call.data == 'catalog_15':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            img = open('юбка.jpg', 'rb')
            bot.send_photo(call.message.chat.id, img, caption='Юбка\n'
                                                              'Артикул: 015\n'
                                                              'Цена: 1800', reply_markup=markup_10)


bot.polling(non_stop=True)