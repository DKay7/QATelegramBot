import asyncio
from setup import setup


async def main():
    dp = await setup()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())

