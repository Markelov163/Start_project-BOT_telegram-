from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# Ёхо хендлер, куда лет€т текстовые сообщени€ без указанного состо€ни€
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Ёхо без состо€ни€."
                         f"—ообщение:\n"
                         f"{message.text}")


# Ёхо хендлер, куда лет€т ¬—≈ сообщени€ с указанным состо€нием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Ёхо в состо€нии <code>{state}</code>.\n"
                         f"\n—одержание сообщени€:\n"
                         f"<code>{message}</code>")