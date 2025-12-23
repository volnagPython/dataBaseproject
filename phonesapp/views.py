from phonesapp.phone_data_selenium import phone_characteristics
from django.shortcuts import render
from Lib.http.client import HTTPResponse
from phonesapp.models import Phones
from phonesapp.models import MainSpec
# from SeleniumScripts.data_transfer import new_dict
# from phonesapp.phone_data_import import phone_characteristics
# from SeleniumScripts.data_transfer import phone_characteristics
############################################################

# Create your views here.
def index_page(request):
    ''' Виводить інформацію на терміналі про зареєстровані телефони'''

    all_phones = Phones.objects.all()
    print("Ваше замовлення включає :",all_phones)
    return render(request, 'index.html')

    # del_phones = Phones.objects.filter(name = 'Readme',properties = "White").delete()
    # print(del_phones)
    # #
    # #
    # # Phones.objects.create(name= 'Readme',properties="White")
    # # return render(request,'index.html')


def index_page2(request):

    # added_phones = Phones.objects.create(name = 'Huawei')
    # print(added_phones)
    # selected_phones = Phones.objects.filter(name = "Apple")
    # print(selected_phones)
    return render(request, 'stores.html')


def stores_site(request):
    ''' Adding a phone to the bucket'''

    added_phones = Phones.objects.create(name ='Apple', color="Black", price= "43598")
    print("Added item :",added_phones)
    return render(request, 'stores.html')

def specifications(request, **kwargs): #value = None):

            # added_specs = MainSpec.objects.create(name = 'Форм-фактор', property = "Моноблок")
            # print(added_specs)
    # new_dict = phone_characteristics = {'Форм-фактор': 'моноблок', 'Кількість SIM-карт': '1 SIM + e-sim', 'Формат SIM-карти': 'e-sim , Nano', "Покоління зв'язку (2G /3G/4G/5G)": '2G , 3G , 4G , 5G', 'Тип дисплея': 'OLED', 'Діагональ екрану': '6.1"', 'Роздільна здатність екрану': '1179 х 2556'}
    # # new_dict = {'Форм-фактор': 'моноблок', 'Кількість SIM-карт': '1 SIM + e-sim', 'Формат SIM-карти': 'e-sim , Nano', "Покоління зв'язку (2G /3G/4G/5G)": '2G , 3G , 4G , 5G', 'Тип дисплея': 'OLED', 'Діагональ екрану': '6.1"', 'Роздільна здатність екрану': '1179 х 2556', 'Частота оновлення екрану': '60 Гц',
    #             'Процесор': 'Apple A16 Bionic', 'Кількість ядер': '6 core', "Вбудована пам'ять": '128 Gb', 'Кількість модулів основної камери': '2', 'Основна камера': '48 + 12 Mpx', 'Діафрагма основної камери': 'f/1.6 + f/2.4', 'Метод стабілізації': 'оптична', 'Запис відео основної камери': '4K / 3840x2160 / стереозвук',
    #             'Кількість модулів фронтальної камери': '1', 'Фронтальна камера': '12 Mpx', 'Діафрагма фронтальної камери': 'f/1.9', 'Функції камери': 'панорама , розпізнавання обличчя , геотегінг , спалах , автофокус', 'Операційна система': 'iOS 17', 'Мультимедіа': 'FM-радіо , мобільні сервіси Google , соціальні мережі , відеоплеєр , музичний плеєр , ігри',
    #             'Органайзер': 'калькулятор , телефонна книга , диктофон , секундомір , нотатки , будильник , світовий час , годинник , календар', 'Бездротові підключення': 'Bluetooth , WI-FI , NFC', 'Навігація': 'BeiDou , Galileo , QZSS , iBeacon , GPS , A-GPS', 'Інтерфейси і підключення': 'USB Type-C', 'Особливості': 'IP68 certified',
    #             'Вбудовані датчики': 'датчик освітлення , компас , акселерометр , датчик наближення , гіроскоп , барометр', 'Безпека': 'FaceID', 'Оснащення': 'пило/вологозахист , гіроскоп , бездротове заряджання', 'Розміри (мм)': '147.6 x 71.6 x 7.80 мм', 'Вага': '171 г', 'Колір': 'чорний', 'Особливості корпусу': 'водонепроникні', 'Виробник': 'Apple',
    #             'Модель': 'iPhone 15 128GB Black', 'Артикул': 'MTP03', 'Гарантія, міс': '12', 'Штрихкод': '195949036019', 'Примітка': 'Виробник може змінювати властивості, характеристики, зовнішній вигляд і комплектацію товарів без попередження', 'Всі характеристики': 'Приховати'}

    for key,value in phone_characteristics.items():
        added_specs = MainSpec.objects.get_or_create(name = key, property = value)
        # print(f'{added_specs}')

    return render(request, 'specifications.html')
