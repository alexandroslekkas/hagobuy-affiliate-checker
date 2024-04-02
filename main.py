import asyncio
from bot import bot_loop
from statistics import statistics_loop

async def main():
    await asyncio.gather(
        bot_loop(),
        statistics_loop(),
    )

if __name__ == '__main__':
    asyncio.run(main())