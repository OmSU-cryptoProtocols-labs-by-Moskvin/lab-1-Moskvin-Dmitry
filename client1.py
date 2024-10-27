import socket
import threading

# Настройки клиента
HOST = '127.0.0.1'
PORT = 12345

# Подключение к серверу
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Вводим имя пользователя и отправляем его серверу
username = input("Введите ваше имя: ")
client.sendall(username.encode('utf-8'))

# Функция для получения сообщений от сервера
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"\n[НОВОЕ СООБЩЕНИЕ] {message}")
        except:
            print("[ОШИБКА] Потеряно соединение с сервером.")
            client.close()
            break

# Функция для отправки сообщений
def send_message():
    while True:
        message = input("Введите сообщение: ")
        client.sendall(message.encode('utf-8'))

# Запуск потоков для получения и отправки сообщений
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
