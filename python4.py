import asyncio
import aiohttp

async def get_api1_data():
    url1 = 'https://jsonplaceholder.typicode.com/todos/1'
    with await aiohttp.ClientSession() as session:
        with await session.get(url1) as response:
            return response.json()

async def get_api2_data():
    url2 = 'https://jsonplaceholder.typicode.com/todos/2'
    with await aiohttp.ClientSession() as session:
        with await session.get(url2) as response:
            return response.json()

async def main():
    async result1, result2 = await asyncio.gather(get_api1_data, get_api2_data)
    return result1, result2

asyncio.run(main())