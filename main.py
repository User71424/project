import threading
import requests

# Использование неинициализированных данных
def use_uninitialized_data():
    var = None  # должно быть инициализировано
    print(var + 1)  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

# Утечки ресурсов
def resource_leak():
    file = open('some_file.txt', 'w')  # Файл не закрывается
    file.write('Hello, world!')

# Неправильное использование API
def incorrect_api_usage():
    # Неправильный URL вызовет исключение requests.exceptions.MissingSchema
    response = requests.get('htp://example.com')  # Опечатка в 'http'
    print(response.text)

# Проблемы с управлением потоком выполнения
def control_flow_issue():
    x = 10
    if x > 5:
        raise Exception("Just an error")
    print(x)  # Этот код никогда не выполнится из-за исключения выше

# Ошибки обработки ошибок
def error_handling_issue():
    try:
        1 / 0
    except ZeroDivisionError:
        pass  # Неправильно игнорировать ошибку без логгирования или обработки

# Некорректные выражения
def incorrect_expressions():
    print("Sum of 1 and None is", 1 + None)  # TypeError

# Проблемы согласованности данных из-за параллелизма
balance = 0
def update_balance():
    global balance
    for _ in range(100000):
        balance += 1  # Race condition

# Запуск примеров
threads = [threading.Thread(target=update_balance) for _ in range(2)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Final balance (expected 200000):", balance)

use_uninitialized_data()  # Используется для демонстрации
resource_leak()
incorrect_api_usage()
control_flow_issue()
error_handling_issue()
incorrect_expressions()
