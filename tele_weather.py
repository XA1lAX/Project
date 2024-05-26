import pyowm #api for weather reading
import telebot #telegram api
from telebot import types
import time
from deep_translator import GoogleTranslator
from forex_python.converter import CurrencyRates
#from googlesearch import search
from langdetect import detect
from langcodes import Language
#import speech_recognition as sr
import webbrowser


bot = telebot.TeleBot('7013440101:AAE1os4MQVhWWC85fiOEVt6W4WlaoqO9uUc')
owm = pyowm.OWM('0dde369d6504f5f84f2596b7fb73b966')

#recognizer = sr.Recognizer()

class City:
    def __init__(self, name, composition, photos):
        self.menu = [
            name,
            "Узнать погоду",
            "Посмотреть отель",
            "Выбрать другой город",
            "Конвертер валют",
            "Сайты с новостями",
            "Аналих текста",
            "Вопрос Google голосом"
        ]
        self.name = name
        self.composition = composition
        self.photos = photos

    def get_weather(self):
        observation = owm.weather_manager()
        weather = observation.weather_at_place(self.name).weather
        temp = weather.temperature("celsius")['temp']

        answer = "В этом городе: " + str(temp) + "°C" + "\nОтносительная влажность: " + str(
            weather.humidity) + "%\n"

        if weather.clouds < 25:
            answer += "Безоблачно"
        elif weather.clouds < 50:
            answer += "Немного облачно"
        elif weather.clouds < 75:
            answer += "Облачно"
        else:
            answer += "Пасмурно"
        return answer

    def to_eng(self):
        return GoogleTranslator(source='ru', target='en').translate(self.name)

    def get_hotel(self):
        return (f"https://ostrovok.ru/hotel/russia/" + self.to_eng().lower())

    def converter(self):
        c = CurrencyRates()
        rate = c.get_rate('USD', 'EUR')
        return (rate)

    def Poisk(self):
        query = "Новости"

        for i in search(query, tld="co.in", num=10, stop=10, pause=1):
            return (i)

    def Analisy(self):
        text = input("Введите текст: ")
        lang_code = detect(text)
        language = Language.get(lang_code)
        return (language.display_name('ru'))

'''
    def golos(self):
        with sr.Microphone() as source:
            print("Говорите что нибудь...")
            audio = recognizer.listen(source)
            try:
                print("Распознание...")
                queryy = recognizer.recognize_google(audio, language = 'ru-RU')
                print(f"Вы сказали {queryy}")
                search_url = f"https://www.google.com/search?q={queryy}"
                webbrowser.open(search_url)
            except sr.UnknownValueError:
                print ("Извините, не удалось распознать речь.")
    search_google()
'''


menu = {
    "city_choise_menu": {
        "Горно-Алтайск": City("Горно-Алтайск",
                              "В краю гор, лесов, бурных рек и чистейших озер до сих пор чтут традиции предков и радушно встречают путешественников. Регион ежегодно принимает порядка двух миллионов человек. Путешественники выбирают экологический, аграрный, гастрономический, познавательный или спортивный туризм, кто-то объединяет несколько направлений.Здесь находится самая высокая точка Сибири и одна из крупнейших горных вершин России — гора Белуха, или Музтау Шыны. Местные зачастую называют гору Уч-Сюре, что переводится как «жилище трех богов». Именно эта гора изображена на гербе Республики Алтай.",
                              ["Горно-Алтайск1.jpeg", "Горно-Алтайск2.jpeg", "Горно-Алтайск3.jpeg"]),
        "Казань": City("Казань",
                       "Казань – третья столица России после Москвы и Санкт-Петербурга. Она яркая, современная, богатая и модная. Здесь есть даже своя кремниевая долина. Город привлекает туристов историей, интересной архитектурой, культурой и вкусной кухней. Для путешественников есть разные варианты жилья – от дорогих гостиниц и апартаментов до хостелов.Главный символ Казани – Казанский Кремль — входит в список объектов Юнеско. Он расположен на берегу реки Казанки. Здесь большое количество достопримечательностей: Кремль, мечеть Кул-Шариф, «падающая» башня Сююмбике, Благовещенский Собор, музеи и выставочные залы. Старинная и самая известная улица в Казани. Это местный Арбат, здесь выступают уличные артисты, атмосферно и довольно шумно.",
                       ["Казань1.jpeg", "Казань2.jpeg"]),
        "Калининград": City("Калининград",
                            "Европейский Калининград заслуженно попал в список лучших мест для отдыха в России. Тут красиво, уютно, интересно. Отдых в Калининграде особенно хорош в мае, летом и в начале осени – примерно до октября. Погода в это время особенно комфортная. Канун Нового года – еще одно удачное время, чтобы поехать в Калининград. Город становится сказочным, это один из лучших вариантов для путешествия по России на новогодних каникулах.\n\
Много достопримечательностей. Все самое главное в Калининграде можно посмотреть за 1 день. Особенно если быстро передвигаться. Но скучать не придется, даже если вы едете в отпуск недели на две или больше. Помимо пряничных домиков в центре, тут есть чудесный зоопарк, зеленые парки для прогулок, набережная, музеи и многое другое. А еще можно съездить за город. Это быстро и точно стоит того.\n\
Европа без «заграна». Калининград недаром называют «русской Европой». Остров Канта, Кафедральный собор, Рыбная деревня, Кирха Святого Семейства, Бранденбургские ворота – окружающие достопримечательности словно переносят вас в другую страну. А эти уютные улочки в глубине города… По ним можно гулять бесконечно. Калининград напоминает мне небольшие города Латвии и Литвы. Считайте, что съездили в Европу без загранпаспорта. Мы заново влюбились в Калининград, когда гуляли по нему с гидом и слушали местные легенды. Советуем вот эту экскурсию, если тоже любите что-то необычное.",
                            ["Калининград1.jpeg", "Калининград2.jpeg", "Калининград3.jpeg"]),
        "Кисловодск": City("Кисловодск",
                           "Кисловодск - популярный курорт с чистым воздухом и полезной водой. Но здесь мы столкнулись с трудностями, которые не ожидали увидеть в популярном туристическом городе.\n\
Самая главная достопримечательность Кисловодска - лечебная вода Нарзан. Вы можете попить её прямо на улице в нескольких местах в Кисловодске: в парке, или в центре города. Именно попить полезной воды многие приезжают в Кисловодск.",
                           ["Кисловодск1.jpeg", "Кисловодск2.jpeg"]),
        "Суздаль": City("Суздаль",
                        "Суздаль, пожалуй самый известный город \"Золотого кольца\".\n\
- Есть в Суздале свой Кремль. Пожалуй, лучшая достопримечательность города.\n\
- Много аутентичных кафе и ресторанов, в которых лучше заранее забронировать места на вечер, потому что желающих отведать настоящей русской еды явно больше, чем столов и стульев в этих заведениях.",
                        ["Суздаль1.jpeg", "Суздаль2.jpeg"]),
        "Ярославль": City("Ярославль",
                          "Начать знакомство с городом можно с бывшего Спасо-Преображенского монастыря на Богоявленской площади, которые многие принимают за Кремль и даже называют Ярославским Кремлём. Но на самом деле Кремль в Ярославле не сохранился. Строение отличают толстые каменные стены, а на его территории находится Спасо-Преображенский собор, несколько церквей, часовня, монастырские корпуса и несколько крепостных башен. Также здесь есть обширная ухоженная территория, по которой приятно гулять.\n\
Волжская набережная.Если верить преданию, то именно здесь был заложен город. Сегодня Волжская набережная является любимейшим местом для прогулок горожан и впечатляет гостей города. Особенно красивые виды открываются со Стрелки — места, где река Которосль впадает в Волгу. На набережной нет развлекательных точек, это просто приятное место для неспешного променада. Зато по пути от Успенского собора до Речного вокзала встретится несколько достопримечательностей, например, Музей истории города, Художественный музей.",
                          ["Ярославль1.jpeg", "Ярославль2.jpeg", "Ярославль3.jpeg"]),
        "Петрозаводск": City("Петрозаводск",
                             "Петрозаводск - город небольшой и почему-то незаслуженно обделён вниманием туристов, а между тем, посмотреть там есть что. Ну и кроме того, грех там не побывать, особенно если называешься путешественником и живёшь всего в 5 часах езды на \"Ласточке\". Прелесть Петрозаводска в том, что он, как и Выборг, вобрал в себя и карельское, и финское, и русское, что несомненно отразилось на облике и восприятии города.\n\
Набережная Онеги.Летом, когда «белые ночи», здесь наверняка приятно провожать закаты с бутылкой минерального шабли, но зимой можно получить дополнительные 7-10 градусов мороза, восхитительную влажность, задорный ветерок в 10-13 м/с и, как следствие, онемение лица 2-3 степени.\n\
Центральная улица города: очень аккуратная, чистая и опрятная. Простирается от ж/д вокзала до Онежского озера и на всём её протяжении можно в перспективе наблюдать Онежское озеро.",
                             ["Петрозаводск1.jpg", "Петрозаводск2.jpg"]),
        "Терскол": City("Терскол",
                        "Если из города хочется вырваться на простор, а на море уже были, — поехали в горы. В долине реки Баксан, начинающейся у подножья Эльбруса, можно устроить контрастный отдых, который легко подстроить под любые запросы и уровень подготовки. Планируем путешествие в Приэльбрусье: подняться выше облаков, попробовать всю продукцию Нальчикского халвичного пивзавода, побывать на леднике.\n\
Есть чем заняться в любое время года: летом — туризм, хайкинг и даже отдых с элементами лечебного, зимой — лыжи, сноуборд.\n\
Красивые виды доступны независимо от уровня подготовки: и из окна автомобиля, и с привалов размеченных троп.Есть вся инфраструктура для первой встречи с горами: тропы, простые маршруты, прокат снаряжения и гиды.",
                        ["Терскол1.jpeg", "Терскол2.jpeg", "Терскол3.jpeg"]),
        "Владивосток": City("Владивосток",
                            "Владивосток — это не только город-порт, но и город-портал, который перемещает туристов в нужное ему измерение. Для жителей западной части России — это ворота в Азию, для жителей Азии — ближайший европейский город, всего в пяти часах езды от русско-китайской границы.",
                            ["Владивосток1.jpeg", "Владивосток2.jpeg"]),
        "Гусь-Хрустальный": City("Гусь-Хрустальный",
                                 "Город Гусь-Хрустальный входит в знаменитое Золотое кольцо России в большинстве своем благодаря производству красивых и качественных изделий из хрусталя, прославленных на всю страну еще с 19 века: здешний материал сочетает яркие расцветки, оригинальный русский стиль и качество.",
                                ["Гусь-Хрустальный1.jpeg", "Гусь-Хрустальный2.jpeg"])
    }
}

def create_markup(menu_items):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in (menu_items):
        markup.add(types.KeyboardButton(i))
    return markup

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(
        message.from_user.id, "Здравствуйте. Вы можете выбрать город и посмотреть погоду и отели в нём!" + "\n",
        reply_markup=create_markup(menu["city_choise_menu"].keys())
    )
    menu[message.from_user.id] = None



@bot.message_handler(content_types=["text"])
def send_message(message):
    """Send the message to user with the weather"""
    try:
        print(time.ctime(), "User id:", message.from_user.id)
        print(time.ctime(), "Message:", message.text.title())
        if (menu[message.from_user.id] == None):
            if (message.text in menu["city_choise_menu"].keys()):
                menu[message.from_user.id] = menu["city_choise_menu"][message.text]
            else:
                menu[message.from_user.id] = City(
                    message.text, "Это отличный город!",
                    ["default.png"])
                menu[message.from_user.id].get_weather()

        if (menu[message.from_user.id] != None):
            if (message.text.lower() == menu[message.from_user.id].name.lower()):
                bot.send_message(message.chat.id, menu[message.from_user.id].name)
                for filename in menu[message.from_user.id].photos:
                    bot.send_photo(
                        message.chat.id,
                        open(f'data/cities/{menu[message.from_user.id].name}/{filename}', "rb")
                    )
                bot.send_message(message.chat.id, menu[message.from_user.id].composition, reply_markup=create_markup(menu[message.from_user.id].menu))
            if (message.text.lower() == "узнать погоду"):
                bot.send_message(message.chat.id, menu[message.from_user.id].get_weather())
            if (message.text.lower() == "выбрать другой город"):
                bot.send_message(message.chat.id, "Введите название другого города", reply_markup=create_markup(menu["city_choise_menu"].keys()))
                menu[message.from_user.id] = None
            if (message.text.lower() == "посмотреть отель"):
                bot.send_message(message.chat.id, menu[message.from_user.id].get_hotel())
            if (message.text.lower() == "Конвертер валют"):
                bot.send_message(message.chat.id, menu[message.from_user.id].converter())
            if (message.text.lower() == "Сайты с новостями"):
                bot.send_message(message.chat.id, menu[message.from_user.id].Poisk())
            if (message.text.lower() == "Анализ текста"):
                bot.send_message(message.chat.id, menu[message.from_user.id].Analisy())
            if (message.text.lower() == "Вопрос Google голосом"):
                bot.send_message(message.chat.id, menu[message.from_user.id].Golos())
    except Exception:
        print(time.ctime(), "User id:", message.from_user.id)
        print(time.ctime(), "Message:", message.text.title(), 'Error')
        menu[message.from_user.id] = None
        bot.send_message(message.chat.id, "Не найден город, попробуйте ввести название снова.\n", reply_markup=create_markup(menu["city_choise_menu"].keys()))



if __name__ == __name__:
    bot.polling(none_stop=True)