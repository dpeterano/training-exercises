import asyncio

async def somme(a, b):
    print(a + b)
    await asyncio.sleep(1)

async def main():
    print("début")
    task = asyncio.create_task(somme(5,5))
    print("fin")

asyncio.run(main())