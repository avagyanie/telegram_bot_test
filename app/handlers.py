from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello!")
    await message.reply("How're you?")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("You pressed the button HELP")


@router.message(Command(F.text == "OK"))
async def ok(message: Message):
    await message.answer("Glad I could help you!")
    