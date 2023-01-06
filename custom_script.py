import asyncio
from datetime import datetime


async def main():
    print(f"Now is {datetime.now().isoformat()}")
    await asyncio.sleep(1.0)
    print(f"Now is {datetime.now().isoformat()}")


asyncio.ensure_future(main())
