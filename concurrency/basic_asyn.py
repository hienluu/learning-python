import asyncio

async def brew_coffee() -> str:
    print("... starting coffee...")
    await asyncio.sleep(2)
    print ("... coffee ready...")
    return "Cappuccino"

async def toast_bread() -> str:
    print("... starting toasting...")
    await asyncio.sleep(2)
    print ("... toast ready...")
    return "Crispy Bread"


async def main():
    results = await asyncio.gather(brew_coffee(), toast_bread())

    print(f" breakfast served: {results}")

if __name__ == "__main__":
    asyncio.run(main())