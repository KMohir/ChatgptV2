from aiogram import types
from handlers.translation import translation, translationuz
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from loader import dp,bot
import openai

openai.api_key = "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"



@dp.message_handler(text="/start")
async def audio_start(message:Message):
    await message.reply("Savolni bering")


    @dp.message_handler(content_types='text')
    async def auido(message:Message):
        t=message.text


        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{message.text}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        text=response.choices[0].text
        textuz=str(translationuz(text))

        textuz.replace("'",'')

        print(textuz)
        await message.answer(text=f"<code>{textuz}</code>")

