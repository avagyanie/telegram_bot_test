from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Catalog")],
                                     [KeyboardButton(text="Basket")],
                                     [KeyboardButton(text="Contacts"),
                                      KeyboardButton(text="About us")]],
                            resize_keyboard=True,
                            input_field_placeholder="Select menu item...")

catalog = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="Goods", callback_data="goods")],
                            [InlineKeyboardButton(text="Services", callback_data="services")],
                            [InlineKeyboardButton(text="Freight", callback_data="freight")]
                            ])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Send phone number",
                                                           request_contact=True,
                                                           resize_keyboard=True)]])
