# 1. Что такое функция и как ее объявить?
# Ответ: Функции Python — это объекты первого класса. Их можно присваивать переменным, хранить в структурах данных,
# передавать в качестве аргументов другим функциям и даже возвращать в качестве значений из других функций.
# Функция объявляется с помощью ключевого слова def.

# 2. Как создать функцию?
# Ответ: Используется ключевое слово def, за которым следует имя функции и круглые скобки ().
# В скобках указываются аргументы функции (если они есть), а после скобок ставится двоеточие :.
# Тело функции записывается с отступом.

# 3. Как показать что созданная функция возвращает результат?
# Ответ: Для этого используется слово return

# 4. В чем разница между параметрами и аргументами функции?
# Ответ: Параметр — это переменная, которой будет присваиваться входящее в функцию значение.
# Аргумент — само это значение, которое передается в функцию при её вызове.

# 5. Как рекурсивные функции работают в Python?
# Ответ: Рекурсивные функции в Python работают следующим образом:
# - Когда вызывается какая-либо функция, она помещается в стек вызова функций, в котором хранится порядок вызова различных функций.
# - Затем выполняется тело функции, и в нём встречается вызов той же самой функции, но с аргументом на единицу больше.
# Соответственно, в стеке появляется новая запись.
# - Всё повторяется до тех пор, пока стек полностью не заполнится и не произойдёт ошибка.
# Чтобы избежать ошибки, нужно ограничить глубину рекурсии. Для этого у любой рекурсивной функции должно быть условие останова,
# чтобы она не продолжалась вечно.

# 6. Что такое декораторы функций и как они используются? ( привести свой пример декоратора)
# Ответ: Декоратор - это функция, которая позволяет обернуть другую функцию для расширения ее функционала без изменения ее кода.
# - Определяем функцию - декоратор, которая принимает декорируемую функцию
# - Внутри нее определяем функцию-обертку
# - Внутри функции обертки присваиваем переменной результат выполнения декорируемой функции
# - Возвращаем из обертки результат
# - Из декоратора возвращаем обертку(без круглых скобок)
# Пример:
# def decor(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('Stop')
#     return wrapper()
# @decor
# def func1():
#     print('Test text 1')

# 7. Как расшифровывается ООП?
# Ответ: Объектно-ориентированное програмирование.

# 8. Что относится к основным принципам(парадигмам) ООП?
# Ответ: - Инкапсуляция
# - Наследование
# - Полиморфизм
# - Абстракция

# 9. Что будет результатом программы и почему?
# class Test:
#     test = None
#
# print(Test.test)
# # Ответ: Результат None. Здесь Test.test - это атрибут класса Test, который инициализирован значением None.
# # Поэтому при обращении к Test.test будет возвращено None.

# 10. Какой принцип ООП описывает следующее предложение?
# Этот принцип является способностью использовать общий интерфейс для нескольких форм (типов данных).
# Ответ: полиморфизм.

# 11. Какой из перечисленных вариантов является верным объявлением private поля?
# private field = 0
# field = 0
# _field = 0
# __field = 0
# Ответ: __field = 0

# 12. Как создать конструктор класса?
# Ответ: с помощью метода __init__()

# 13. Как много конструкторов в классе может иметь Python?
# Ответ: может быть только один конструктор - метод __init__(). Этот метод вызывается при создании нового объекта класса
# и инициализирует его начальное состояние.
# Если вы определяете более одного метода __init__() в классе, только последний будет учитываться, а все предыдущие будут перезаписаны.

# 14. Что будет результатом данной программы
# class Test:
#     def print_text(self):
#         print('Это родительский класс Test')
# class Test2(Test):
#     def print_text(self):
#         print('Это класс потомок Test2')
# test = Test2()
# test.print_text()
# # Ответ: Это класс потомок Test2

# 15. Какой параметр обязательно принимает в себя метод экземпляра?
# Ответ: сам экземпляр класса.

# 16. Как использовать инкапсуляцию для защиты данных в классах?
# Ответ: # public - всем доступный
# # _protected - частично закрытый
# # __private - ограниченный доступ
# # class Class1:
# #     def public(self):
# #         print('Это публичный метод')
# #
# #     def _protected(self):
# #         print('Это метод частично защищенный')
# #
# #     def __private(self):
# #         print('Это метод полностью защищенный')
# #
# # exp = Class1
# # exp.public()

# 17. Какая разница между абстрактными классами и интерфейсами в Python?
# Ответ: Абстрактный класс — это класс, у которого не реализован один или больше методов
# (некоторые языки требуют такие методы помечать специальными ключевыми словами).
# Интерфейс — это абстрактный класс, у которого ни один метод не реализован, все они публичные и нет переменных класса.
# Можно считать, что любой интерфейс — это уже абстрактный класс, но не наоборот.

# 18. Как показать в классе что метод является абстрактым?
#Ответ: нужно использовать декоратор abstractmethod из модуля abc

# 19. Что будет результатом программы?
# class Test:
#     __test = 0
#
# print(Test.__test)
# Ответ: возникнет ошибка AttributeError, указывающая на то, что атрибут не найден.

# 20.Что делает финализатор класса?
# Ответ: это метод, который вызывается при уничтожении экземпляра класса или объекта.
# В Python финализатор класса обычно реализуется с помощью метода __del__().

# 21. Распишите работу магических методов: new, call
# Ответ:
# new - используется для создания нового экземпляра класса. Он вызывается перед методом __init__() и должен вернуть
# новый объект. Обычно __new__() используется в классах, наследующих от неизменяемых типов данных (как например int, str и т. д.),
# чтобы управлять процессом создания экземпляра.
# call - позволяет вызывать объекты класса, как если бы они были функциями. Если класс имеет метод __call__(),
# то экземпляры этого класса можно вызывать, передавая аргументы напрямую после имени экземпляра, как если бы они были
# вызываемой функцией.

# 22. Если в классе определены два метода с одинаковыми именами и разными списками параметров, что будет результатом?
# Ответ: Python будет использовать только последний определенный метод. При вызове метода с одинаковым именем будет
# использоваться последняя версия метода, которая была определена в классе.

# 23. Значением поля класса по умолчанию может являться?
# - значение переменной
# - константа
# - результат вызова функции
# - возможность указания значений полей по умолчанию в Python не предусмотрена
# Ответ: значение переменной, константа, результат вызова функции

# 24. Укажите результат выполнения скрипта и почему:
# class Foo:
#     count = x
#
#     def __init__(self):
#         self.count += 1
#
#     def __del(self):
#         self.count += 1
#
# obj = Foo()
# print(obj.count)
# Ответ: ошибка, так как в строке count = x переменная x не определена. Это приведет к исключению NameError.

# 25. Как указать в программе что класс A наследуется от B?
# Ответ:
# class B:
#     pass
#
# class A(B):
#     pass

# 26. Что такое API и для чего оно используется?
# Ответ: API (Application Programming Interface) - это набор определенных правил и инструкций, которые определяют,
# как различные компоненты программного обеспечения должны взаимодействовать между собой.
# API обычно определяет набор функций, протоколов и инструментов для разработки приложений,
# обеспечивая способ обмена данными и коммуникации между различными программными компонентами.
# Используется для: интеграции, разработки приложений, управления данными, автоматизации, создания расширений.

# 27. Какие преимущества предоставляют API?
# Ответ:
# - Интеграция: позволяет различным приложениям и сервисам обмениваться данными и взаимодействовать друг с другом.
# - Расширяемость: позволяет расширять функциональность существующих приложений и сервисов путем интеграции дополнительных модулей и компонентов.
# - Универсальность: предоставляет стандартизированный способ взаимодействия с приложениями и сервисами.
# - Автоматизация: позволяет автоматизировать определенные задачи и процессы, используя программный интерфейс для взаимодействия с другими системами.
# - Стандартизация: API обычно предоставляет стандартизированные методы и протоколы для взаимодействия.
# - Безопасность: позволяет контролировать доступ к данным и функциям, обеспечивая защиту информации и конфиденциальность.
# - Повторное использование кода: позволяет использовать уже существующий функционал без необходимости его повторного написания.

# 28. Расскажите о различных типах HTTP-запросов.
# Ответ:
# Запросы (HTTP Requests) — сообщения, которые отправляются клиентом на сервер, чтобы вызвать выполнение некоторых действий. Зачастую для получения доступа к определенному ресурсу.
# Ответы (HTTP Responses) — сообщения, которые сервер отправляет в ответ на клиентский запрос.

# 29. Какие основные методы HTTP используются в RESTful API?
# Ответ: GET, POST, PUT, DELETE

# 30. Что такое запросы GET, POST, PUT и DELETE? Как они используются в API?
# Ответ:
# - GET: используется для запроса данных с сервера.
# - POST: используется для отправки данных на сервер для обработки.
# - PUT: используется для создания или обновления ресурса на сервере.
# - DELETE: используется для удаления ресурса на сервере.

# 31. Что такое заголовки HTTP? Какие заголовки часто используются в API?
# Ответ: заголовки HTTP - это часть HTTP-запросов и ответов, которая содержит метаданные о передаваемом сообщении.
# Они представляют собой пары "ключ-значение" и используются для передачи дополнительной информации о запросе или ответе.
# Часто используются заголовки в API:
# - Content-Type: определяет тип содержимого тела запроса или ответа.
# - Authorization: содержит данные для аутентификации клиента на сервере.
# - Accept: указывает типы содержимого, которые клиент может принять от сервера.
# - Content-Length: указывает длину тела запроса или ответа в байтах.
# - User-Agent: содержит информацию о клиентском приложении или браузере, который инициирует запрос.
# - Cache-Control: управляет кэшированием содержимого на клиенте или сервере.
# - X-Requested-With: используется для указания типа AJAX-запроса.
# - Origin: указывает источник запроса в CORS (Cross-Origin Resource Sharing).