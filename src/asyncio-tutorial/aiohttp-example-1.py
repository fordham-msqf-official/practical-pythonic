""" aiohttp example, coroutine on networking I/O operations
    aiohttp is also a web framework. You can even create your web application 
"""
import aiohttp
import asyncio
import async_timeout


async def fetch(session, url):
    # async with await session.get(url) as resp:
    #     return resp.status
    resp = await session.get(url)
    async with resp:
        return resp.status


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://python.org")
        print(html)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
