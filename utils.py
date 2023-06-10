from discord import Message
from typing import AsyncIterator
import json


def load_json(file_path: str) -> dict:
    with open(file_path, mode='r', encoding='utf-8') as file:
        return json.load(file)


def load_jokes(file_path: str) -> list:
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.readlines()


def format_messages(messages: list) -> str:
    messages.reverse()
    formated_messages = [
        f'{msg.author.name}: {msg.content}' for msg in messages]
    return '\n'.join(formated_messages)


async def get_message_context(message_iterator: AsyncIterator, message: Message) -> str:
    history_buffer: int = 5
    messages: list = []
    async for item in message_iterator:
        messages.append(item)
        if item.id != message.id:
            if len(messages) > history_buffer:
                messages.remove(messages[0])
        else:
            break
    messages[-1].content = f'⭐ {messages[-1].content} ⭐'
    for _ in range(0, history_buffer):
        messages.append(await message_iterator.__anext__())

    return format_messages(messages)
