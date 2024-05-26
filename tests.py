import unittest
from unittest.mock import Mock, patch
from googletrans import Translator
import owm

class City:
    def init(self, name, composition, photos):
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

def start_message(message):
    bot = Mock()
    bot.send_message = Mock(return_value=None)
    menu = {"city_choise_menu": {"Moscow": "moscow", "Saint Petersburg": "saint_petersburg"}}

    bot.send_message(
        message.from_user.id, "Здравствуйте. Вы можете выбрать город и посмотреть погоду и отели в нём!" + "\n",
        reply_markup=create_markup(menu["city_choise_menu"].keys())
    )
    menu[message.from_user.id] = None

@patch('bot_module.bot', new_callable=Mock)
class TestCityMethods(unittest.TestCase):
    def setUp(self):
        self.bot_mock = Mock()
        self.message_mock = Mock()
        self.message_mock.from_user = Mock()
        self.message_mock.from_user.id = 12345
        self.city = City("Moscow", "Это отличный город!", ["default.png"])

    def test_get_weather(self):
        weather_mock = Mock()
        weather_mock.temperature.return_value = {"celsius": {"temp": 20}}
        weather_mock.humidity = 50
        weather_mock.clouds = 25
        owm.weather_manager.return_value.weather_at_place.return_value.weather = weather_mock
        result = self.city.get_weather()
        self.assertEqual(result, "В этом городе: 20°C\nОтносительная влажность: 50%\nБезоблачно")

    def test_to_eng(self):
        GoogleTranslator.return_value.translate.return_value = "Moscow"
        result = self.city.to_eng()
        self.assertEqual(result, "Moscow")

    def test_start_message(self, bot_mock):
        bot_mock.send_message.return_value = None
        start_message(self.message_mock)
        bot_mock.send_message.assert_called_with(12345, "Здравствуйте. Вы можете выбрать город и посмотреть погоду и отели в нём!" + "\n", reply_markup=create_markup(menu["city_choise_menu"].keys()))
        self.assertEqual(menu[self.message_mock.from_user.id], None)

if name == 'main':
    unittest.main()