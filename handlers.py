from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


# 🔴 заглушки
async def generate_post(topic: str) -> str:
    return f"🔥 Пост про {topic}\n\nЭто пример текста. Скоро здесь будет AI."


async def generate_ideas(topic: str) -> str:
    return f"💡 Идеи для {topic}:\n1. Идея 1\n2. Идея 2\n3. Идея 3"


# /start
@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "🔥 Привет! Я PostGenie — бот для генерации постов.\n\n"
        "Напиши тему или используй команды:\n"
        "/post — создать пост\n"
        "/ideas — создать идеи постов\n"
        "/help — помощь"
    )


# /help
@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "📌 Как пользоваться:\n\n"
        "Напиши тему и я сгенерирую пост\n\n"
        "Пример:\nмаркетинг"
    )


# /post
@router.message(Command("post"))
async def post_command_handler(message: Message):
    await message.answer("Напиши тему поста 👇")


# /ideas
@router.message(Command("ideas"))
async def ideas_command_handler(message: Message):
    await message.answer("Напиши тему для идей 👇")


# обработка текста
@router.message()
async def text_handler(message: Message):
    topic = message.text

    post = await generate_post(topic)

    await message.answer(post)