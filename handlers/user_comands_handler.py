from aiogram.types import Message

from config.commands_text_config import START_TEXT


async def process_start_command(message: Message):
    await message.answer(START_TEXT)


async def get_question_answer(message: Message):
    text = "Эта функция находится в разработке. Скоро она станет доступной"
    await message.answer(text)
