import asyncio
import requests
from pyrogram import Client, filters
from flask import Flask, request

botID = "@alina_ai_demo_bot"
command = "/sens"

route = '/command'

serverURL = 'http://alina-ai.ru/greenhouse'
# Создайте нового клиента Pyrogram
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
client = Client('my_session', api_id, api_hash)

app = Flask(__name__)

# Функция для отправки команды и сохранения ответа
async def send_command_and_save_response():
    async with client:
        # Отправляем команду /sens на @akina_ai_bot
        response = await client.send_message(botID, command)

        # Ожидаем ответа бота
        await asyncio.sleep(0.2)  # Подождите некоторое время, чтобы получить ответ

        # Сохраняем ответ бота в файл
        with open('response.txt', 'a') as file:
            file.write(response.text + f"\n\n\n\n")

        # Отправляем ответ бота на сервер alina-ai.ru/greenhouse
        payload = {'response': response.text}
        response = requests.post(serverURL, data=payload)
        print('Response sent:', response.status_code)

        
async def send_command_post(post_command):
    async with client:
        # Отправляем команду /sens на @akina_ai_bot
        response = await client.send_message(botID, post_command)

        # Ожидаем ответа бота
        await asyncio.sleep(0.2)  # Подождите некоторое время, чтобы получить ответ

        # Сохраняем ответ бота в файл
        with open('response.txt', 'a') as file:
            file.write(response.text + f"\n\n\n\n")

        # Отправляем ответ бота на сервер alina-ai.ru/greenhouse
        payload = {'response': response.text}
        response = requests.post(serverURL, data=payload)
        print('Response sent:', response.status_code)


# Обработчик для POST-запроса на сервер
@app.route(route, methods=['POST'])
async def handle_post_command():
    await send_command_post(post_command = request.json.get('command'))
    

# Асинхронная функция для выполнения каждый час
async def main():
    while True:
        await asyncio.sleep(3600)  # Подождите один час перед следующим выполнением


# Запускаем асинхронный цикл событий
loop = asyncio.get_event_loop()
loop.create_task(main())
client.start()

if __name__ == '__main__':
    app.run()
