import socket
import threading

# Настройки сервера
HOST = '127.0.0.1'
PORT = 12345

clients = []  # Список подключенных клиентов (сокет, адрес, имя)


# Функция для обработки подключения клиента
def handle_client(conn, addr):
    print(f"[НОВОЕ ПОДКЛЮЧЕНИЕ] {addr} подключился.")

    # Получаем имя пользователя
    username = conn.recv(1024).decode('utf-8')
    clients.append((conn, addr, username))
    print(f"[НОВОЕ ПОДКЛЮЧЕНИЕ] Пользователь {username} подключился.")

    try:
        while True:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[СООБЩЕНИЕ ОТ {username}] {message}")
            # Рассылаем сообщение всем клиентам, кроме отправителя
            for client, client_addr, client_name in clients:
                if client != conn:
                    formatted_message = f"{username}: {message}"
                    client.sendall(formatted_message.encode('utf-8'))
    except:
        print(f"[ОТКЛЮЧЕНИЕ] {username} ({addr}) отключился.")
    finally:
        clients.remove((conn, addr, username))
        conn.close()


# Запуск сервера
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[СЕРВЕР ЗАПУЩЕН] Сервер запущен на {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[АКТИВНЫЕ ПОДКЛЮЧЕНИЯ] {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
