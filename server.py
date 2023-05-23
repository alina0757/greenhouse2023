import asyncio
import requests
from pyrogram import Client, filters

# Создайте нового клиента Pyrogram
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
client = Client('my_session', api_id, api_hash)


# Функция для отправки команды и сохранения ответа
async def send_command_and_save_response():
    async with client:
        # Отправляем команду /sens на @akina_ai_bot
        response = await client.send_message('@akina_ai_bot', '/sens')

        # Ожидаем ответа бота
        await asyncio.sleep(5)  # Подождите некоторое время, чтобы получить ответ

        # Сохраняем ответ бота в файл
        with open('response.txt', 'a') as file:
            file.write(response.text + '\n')

        # Отправляем ответ бота на сервер alina-ai.ru/greenhouse
        payload = {'response': response.text}
        response = requests.post('https://alina-ai.ru/greenhouse', data=payload)
        print('Response sent:', response.status_code)


# Обработчик для POST-запроса на сервер
@client.on_message(filters.command(['sens'], prefixes='/') & filters.private)
async def handle_post_command(client, message):
    await send_command_and_save_response()
    await client.send_message(
        message.chat.id,
        'Ответ от бота сохранен и отправлен на сервер alina-ai.ru/greenhouse.'
    )


# Асинхронная функция для выполнения каждый час
async def main():
    while True:
        await asyncio.sleep(3600)  # Подождите один час перед следующим выполнением


# Запускаем асинхронный цикл событий
loop = asyncio.get_event_loop()
loop.create_task(main())
client.run()
