import asyncio
import httpx
import time


"""
1. The Core Concepts

To get proficient, you need to understand three main pillars:
    The Event Loop: The "brain" that manages all the tasks. It keeps track of what is running and what is waiting.
    Coroutines: Functions defined with async def. They don't run immediately when called; they return a "coroutine object" 
    that needs to be scheduled on the loop.
    Await: The keyword await tells the loop: "I'm going to wait for this result; feel free to go run other tasks in the meantime."

Important Rules
    Only call it once: You should generally only call asyncio.run() once in your entire program (usually at the very bottom). 
    If you are already inside an async def function, you should use await instead.
    Top-level only: It is designed to be the main entry point. If you try to call it while another loop is already running, 
    Python will raise a RuntimeError.
"""
async def fetch_url(client: httpx.AsyncClient, url: str) -> str:
    print(f"Fetching {url}...")
    response = await client.get(url)
    print(f"Finished fetching {url} with status {response.status_code}  ")
    return response.text[:100]  # Return the first 100 characters for brevity


async def scrape_urls(urls: list[str]) -> list[str]:
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        pages =  await asyncio.gather(*tasks)
        return pages
    

if __name__ == "__main__":
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com"
    ] * 5  # 15 requests total
    
    start = time.perf_counter()
    all_pages = asyncio.run(scrape_urls(urls))
    end = time.perf_counter()
    
    print(f"Finished {len(urls)} requests in {end - start:.2f} seconds.")

    for i, page in enumerate(all_pages):
        print(f"Page {i+1} content preview: {page[:50]}...")