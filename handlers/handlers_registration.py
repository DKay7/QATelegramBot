from aiogram import Dispatcher

from handlers.user_comands_handler import get_question_answer, process_start_command


def register_user_commands_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(process_start_command, commands="start")
    dispatcher.register_message_handler(get_question_answer, commands=['ask', 'q', 'question'])
