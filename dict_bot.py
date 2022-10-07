# В google colab добавить: !pip install pyTelegramBotAPI
# Чтобы добавить новое слово — нужно его прописать в массиве DEFINITOINS на 11 строчке
# Важно все новые аббривиатуры в коде писать только с маленьких букв
# Пользователь в телеграм может писать и с большой и с маленькой — код всегда приводит к строчным

from telebot import TeleBot, types

bot = TeleBot(token='5767733016:AAEt0nqAhLx7flPVsb_O47jP1Hj8_GCXSco', parse_mode='html') # создание бота

# словарь с определениями и аббревиатурами, которые знает бот
# в формате:
# 'ключевая фраза': 'соответствующее ей определение'
DEFINITOINS = {
    'регресс': 'Регрессионое тестирование-(Regression testing)-это тестирование ранее протестированного функционала что бы убедиться что изменение в коде, например добавление новой функциональности либо же исправление какого либо дефекта, не повлияло на работу старой функциональности. Данный вид тестирования проводится в каждом новом билде.',
    'клиент': '(frontend), это то есть все что видит клиент своими глазами, это публичная часть сайта или приложения, с которой непосредственно контактирует пользователь.',
    'бекенд': '(backend)-это серверная часть, которая работает с запросами, базой данных, обработка данных и т.д. Это все то чего пользователь не видит.',
    'http': 'http-это протокол передачи данных между браузером и сервером.',
    'https': 'это тот же http, но с добавленными методами шифрования данных и проверки безопасности',
    'квери': 'query-это параметры запроса для подстановки в URL. Начинаются с ?, а разделяются с помощью &',
    'rest': 'это набор определенных правил, в котором программисты договорились соблюдать определенный архитектурный стиль, что бы все системы легко обменивались данными.',
    'xml': 'это формат данных который содержится в body. При создании XML используются только теги.',
    'json': 'JSON-это один из основных форматов передачи данных который содержится в body. JSON используется в REST запросах.',
    'джейсон': 'JSON-это один из основных форматов передачи данных который содержится в body. JSON используется в REST запросах.',
    'хедер': 'Хэдеры HTTP являются основной частью HTTP-запросов и ответов, и они содержат информацию о клиенте, закрытой странице, сервере и многих других.',
    'curl': 'это специальная программа или утилита, которая позволяет делать различные сетевые запросы по различным протоколам данных (HTTP, FTP, SCP, ...).',
    'апи': 'это специальная программа или утилита, которая позволяет делать различные сетевые запросы по различным протоколам данных (HTTP, FTP, SCP, ...).',
    'смоук': 'Smoke testing-как правило проверяется только самый важный и необходимый функционал. Проводится на начальном этапе например после первого билда. Билд это первая версия продукта направленно на проверку готовности разработанного продукта к проведению расширенного тестирования и определение общего состояния качества продукта. Обычно это короткий цикл тестов либо один тест который подтверждает либо отрицает факт того что продукт стартует и выполняет свои основные функции. Есть только два варианта развития событий мы можем сказать либо да либо нет продукту. Если нет то направляем репорт бага на разработчика и тестирование останавливается полностью',
    'тест кейс': 'Это четкое описание действий, которые необходимо выполнить для проверки функционала.В тест кейсе как правило есть такие поля как: -Название, -Приоритет, -Предусловие, -Шаги, -Ожидаемый рузультат, -Постусловие.В тест кейсе есть только ожидаемый результат и нет фактического результата.Формат строгий.Все тест кейсы ведут в ТМС системах.',
    'баг репорт': 'Багрепорт это описание бага и шаги к его воспроизведению.Состоит из:Summary (Заголовок).Description (Описание).Шаги воспроизведения.Текущий результат (Можно словами, но желательно скрин или видео)Ожидаемый результат (Можно словами, но желательно скрин или видео)Окружение (Билд-это версия приложения, сайта или бекенда) (Только IOS или Android или на обоих платформах)Тестовые устройства (IOS Android Mac).Ручка (чаще для багрепорта на бекенд) cURL запроса.Аналитика (яндекс метрика с количеством пользователей, которых заафектила проблема)Документация, ТЗ, СпекаЛоги(kibana) SentrySlack (ссылка на тред)Priority-Minor, normal, critSeverety-blocker, critica, normal, minor, trivialFollowers-boss, mannager, coder',
    'тмс': 'ТМС(Test managment system)-это система для ведения тест кейсов.',
    'test suit': 'это набор тест кейсов ТМС системе, другими словами коллекция или папка, в которой находится определенный набор тест кейсов для проверки определенной части функционала нашего ПО.',
    'тест сьют': 'это набор тест кейсов ТМС системе, другими словами коллекция или папка, в которой находится определенный набор тест кейсов для проверки определенной части функционала нашего ПО.',
    'чек лист': 'Чек лист-формат не строгий. Общий смысл записать и структурировать все проверки. Описываем только название тест кейсов которые используем.',
    'тест план': 'Тест план-формат не строгий. Общий смысл записать и структурировать все что нам может помочь провести успешное тестирование.',
    'html': 'это кирпичики из которых состоит сайт-теги. У кирпичиков есть технические свойства-атрибуты. Набор HTML тегов называется DOM.',
    'css': 'это свойства наших кирпичиков, мы можем изменять их стили. Селектор-это механизм поиска HTML элемента',
    'seo': 'За SEO отвечают такие теги как Meta, они никак не влияют на пользователя, но с помощью этих тегов прокачивается SEO.',
    'чарльз': 'Charles один из представителей снифферов, предназначен для того что бы перехватывать запросы и ответы между фронтендом и бекендом(аналог devtools).Из основных команд charles знаю такие как maplocal & breakpoint. Breakpoint останавливает запрос и(или) ответ в момент остановки их можно редактировать. Maplocal подставляет в body ответа json с твоего компьютера.',
    'charles': 'Charles один из представителей снифферов, предназначен для того что бы перехватывать запросы и ответы между фронтендом и бекендом(аналог devtools).Из основных команд charles знаю такие как maplocal & breakpoint. Breakpoint останавливает запрос и(или) ответ в момент остановки их можно редактировать. Maplocal подставляет в body ответа json с твоего компьютера.',
    'breakpoint': 'останавливает запрос и/или ответ.',
    'maplocal': 'подставляет в body ответа файл json, сохраненный на компьютере.',
    'гит': 'Гит- это система контроля версиями, также это система, которая позволяет сразу нескольким разработчикам сохранять и отслеживать изменения в файлах вашего проекта.',
    'git': 'Гит- это система контроля версиями, также это система, которая позволяет сразу нескольким разработчикам сохранять и отслеживать изменения в файлах вашего проекта.',
    'тестировщик': 'Тестировщик отвечает за прохождение чек-листов, тест-кейсов, проверку и документирование дефектов, разработку документации;',
    'testing': 'Тестировщик отвечает за прохождение чек-листов, тест-кейсов, проверку и документирование дефектов, разработку документации;',
    'qa engineer': 'Quality Assurance анализирует весь проект и процессы, ищет решения, превентивно работает над улучшением качества продукта.',
    'qa': 'Quality Assurance анализирует весь проект и процессы, ищет решения, превентивно работает над улучшением качества продукта.',
    'qs': 'Quality Control, в дополнение к обязанностям тестировщика, анализирует результаты тестирования и качество билдов, выявляет причины отклонений;',
    'рест': 'Договоренность, философия,правила этикета',
    'rest': 'Договоренность, философия,правила этикета',
    'get': 'Получение данных. Ограничен длинной урла 2048 символов.Идемпотентный метод. Нет боди',
    'гет': 'Получение данных. Ограничен длинной урла 2048 символов.Идемпотентный метод. Нет боди',
    'пост': 'POST-Отправление данных. НЕидемпотентный. Есть боди',
    'post': 'POST-Отправление данных. НЕидемпотентный. Есть боди',
    'soap': 'SOAP (simple object acces protocol)-этот протокол используется для обмена произвольными сообщениями в формате XML. SOAP-может использоваться с любым протоколом прикладного уровня.',
    'соап': 'SOAP (simple object acces protocol)-этот протокол используется для обмена произвольными сообщениями в формате XML. SOAP-может использоваться с любым протоколом прикладного уровня.',
    'agile': 'Философия гибкой разработки',
    'аджайл': 'Философия гибкой разработки',
    'эджайл': 'Философия гибкой разработки',
    'верификация': 'Верификация — это процесс оценки системы, чтобы понять, удовлетворяют ли результаты текущего этапа разработки условиям, которые были сформулированы в его начале. Без запуска кода. Отвечает на вопрос: Делаем ли мы продукт правильно? Проверка заключается в том, что система хорошо спроектирована и безошибочна. Проверяется наличие чего-нибудь. Проходит до Валидации.',
    'валидация': 'Валидация — это определение соответствия разрабатываемого ПО ожиданиям и потребностям пользователя, его требованиям к системе. Динамический процесс. Включает запуск кода. Отвечает на вопрос: Делаем ли мы правильный продукт? Проверяется работоспособность чего-нибудь. Проходит после Верификации, что позволяет найти ошибки, упущенные на стадии Верификации.',
    'кеш': 'КЭШ – это данные, которые загружаются с компьютера для того, чтобы упростить и ускорить работу на тех сайтах, которые посещались ранее.',
    'куки': 'Cookie – это временные файлы, которые хранятся на жёстком диске компьютера пользователя, они служат для хранения персональных данных пользователя. Например, логин и пароль для авторизации, предпочтения по рекламе и т.д.',
    'cookie': 'Cookie – это временные файлы, которые хранятся на жёстком диске компьютера пользователя, они служат для хранения персональных данных пользователя. Например, логин и пароль для авторизации, предпочтения по рекламе и т.д.',
    'идентификация': 'Идентификация — процедура, в результате выполнения которой для субъекта идентификации выявляется его идентификатор, однозначно определяющий этого субъекта в информационной системе.',
    'аутентификация': 'Аутентификация — процедура проверки подлинности, например проверка подлинности пользователя путем сравнения введенного им пароля с паролем, сохраненным в базе данных.',
    'авторизация': 'Авторизация — предоставление определенному лицу или группе лиц прав на выполнение определенных действий.',
    'логи': 'Логи — это текстовые файлы, в которых хранится информация о пользователях, их взаимодействии с сервером, а также системная информация о работе сервера.',
    'лог': 'Логи — это текстовые файлы, в которых хранится информация о пользователях, их взаимодействии с сервером, а также системная информация о работе сервера.',
    'баг': 'Баг-это несоответсвие фактического выполнения программы, ожидаемому результату',
    'дефект': 'Баг-это несоответсвие фактического выполнения программы, ожидаемому результату',
    'спецэффект': 'Баг-это несоответсвие фактического выполнения программы, ожидаемому результату',
    'bug': 'Баг-это несоответсвие фактического выполнения программы, ожидаемому результату',
    'апи': 'АПИ=HTTP методы. Интерфейс взаимодействия',
    'api': 'АПИ=HTTP методы. Интерфейс взаимодействия',
    'черный ящик': 'Черный ящик-это техника тестирования основанная на работе исключительно с внешними интерфейсами тестируемой системы т.е. мы вообще не знаем программного кода. Тестируем только GUI графический интерфейс',
    'белый ящик': 'Белый ящик-нам известны все детали реализации тестируемой программы т.е. это такой метод тестирования ПО который предпологает, что известна внутренняя структура, устройство, реализация известна тестировщику',
    'серый ящик': 'Серый ящик-здесь известны только некоторые особенности реализации тестирования систем. Это такой метод тестирования ПО который представляет комбинацию двух предидущих т.е. внутреннее устройство программы нам известно лишь частично. Например мы знаем внутреннюю структуру и алгоритм работы ПО для того что бы написать максимально эффективный тест кейс но само тестирование проводится по методике черного ящика',
    'функциональное': 'Функциональное-это один из видов тестирования направленный на проверку соответствия функциональных требований ПО к его реальным характеристикам ключевое здесь функциональные требования т.е. мы проверяем, что делает наша система. Основной задачей является подтверждение того, что наш разрабатываемый продукт обладает всем тем функционалом, который требует заказчик. Это тестирование проводится на всех уровнях и проверяет, то что система делает.',
    'функциональное тестирование': 'Функциональное-это один из видов тестирования направленный на проверку соответствия функциональных требований ПО к его реальным характеристикам ключевое здесь функциональные требования т.е. мы проверяем, что делает наша система. Основной задачей является подтверждение того, что наш разрабатываемый продукт обладает всем тем функционалом, который требует заказчик. Это тестирование проводится на всех уровнях и проверяет, то что система делает.',
    'не функциональное': 'Не функциональное-является проверка соответствия свойств приложения с его нефункциональными требованиями т.е. при данном виде тестирования мы проверяем как наша система работает. По сути это тестирование свойств которые не относятся к функциональным возможностям системы, данные свойств определяются не функциональными требованиями, к таким свойствам можно отнести например надежность, т.е. реакция системы на непредвиденные ситуации.',
    'не функциональное тестирование': 'Не функциональное-является проверка соответствия свойств приложения с его нефункциональными требованиями т.е. при данном виде тестирования мы проверяем как наша система работает. По сути это тестирование свойств которые не относятся к функциональным возможностям системы, данные свойств определяются не функциональными требованиями, к таким свойствам можно отнести например надежность, т.е. реакция системы на непредвиденные ситуации.',
    'позитивное': 'Позитивное-это такое тестирование когда применяются сценарии которые соответствуют нормальному ожидаемому поведению системы. С его помощью мы можем определить что система делает то для чего и была создана',
    'позитивное тестирование': 'Позитивное-это такое тестирование когда применяются сценарии которые соответствуют нормальному ожидаемому поведению системы. С его помощью мы можем определить что система делает то для чего и была создана',
    'негативное': 'Негативное (использование системы не типичным образом)-в рамках сценария соответствует не штатному поведению системы',
    'негативное тестирование': 'Негативное (использование системы не типичным образом)-в рамках сценария соответствует не штатному поведению системы',
    
}

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет! Я помогу тебе расшифровать сложные аббревиатуры и термины 🤓\nВведи интересующий термин, например, регресс', # текст сообщения
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    # пробуем найти ключевую фразу в словаре
    definition = DEFINITOINS.get(
        message.text.lower(), # приводим текст сообщения к нижнему регистру
    )
    # если фразы нет в словаре, то переменная definition будет иметь значение None
    # проверяем это условие
    if definition is None:
        # если ключевая фраза не была найдена в словаре
        # отправляем ответ
        bot.send_message(
            chat_id=message.chat.id,
            text='😋 Я пока не знаю такого определения',
        )
        # выходим из функции
        return
    
    # если ключевая фраза была найдена, формируем текст сообщения и отправляем его
    # если перед строкой поставить букву f, то в фигурных скобках {} можно использовать переменные :)
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Определение:\n<code>{definition}</code>',
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Жду следующий термин',
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
