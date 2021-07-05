from aiogram.types import Message

from config.commands.commands_names import QUESTION_COMMAND_NAME
from config.commands.commands_text_config import START_TEXT, EMPTY_MESSAGE_ERROR_TEXT
from network.prediction import get_predicted_answer


async def process_start_command(message: Message):
    await message.answer(START_TEXT)


async def get_question_answer(message: Message):
    import utils.db
    text = message.get_args()

    if text:
        answer = get_predicted_answer(text)
        await message.answer(answer)

    else:
        await message.answer(EMPTY_MESSAGE_ERROR_TEXT)
