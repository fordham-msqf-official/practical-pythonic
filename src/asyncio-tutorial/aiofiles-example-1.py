""" ailfiles example, coroutine on file I/O operations
"""
import asyncio
import aiofiles
# asyncio enabled alternative to standard file API
# Similar API
# Supports async and await


async def main():
    async with aiofiles.open('aiofiles-example-1.py', mode='r') as f:
        contents = await f.read()
    print(contents)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
