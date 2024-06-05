# import yaml
# datas={
#     "name": input("Enter your name"),
#     "age": int(input("Enter your age")),
#     "surname": input("Enter your surname"),
# }
# with open("data.yaml","w") as file_yaml:
#     yaml.dump(datas,file_yaml)
#
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import Message
# from aiogram.filters.command import Command
# import yaml
#
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token="6709959864:AAFakIbD5Gw-EQQz22XEUHf9DckQUv799qo")
# dp = Dispatcher()
#
#
# @dp.message(Command("start"))
# async def cmd_start(message: Message):
#     await message.answer("hello")
#     user={
#         "username": message.from_user.username,
#         "full_name": message.from_user.full_name,
#         "user_id": message.from_user.id
#     }
#     with open("users.yaml","w") as file_yaml:
#         yaml.dump(user,file_yaml)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
