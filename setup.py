import logging
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand
from config.bot.bot_config import TOKEN
from config.commands.commands_names import QUESTION_COMMAND_NAME
from handlers.handlers_registration import register_user_commands_handlers

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command=QUESTION_COMMAND_NAME, description="Задать вопрос нейросети"),
    ]
    await bot.set_my_commands(commands)


def prepare_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot...")


async def setup():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)

    prepare_logger()
    register_user_commands_handlers(dp)
    await set_commands(bot)

    return dp
