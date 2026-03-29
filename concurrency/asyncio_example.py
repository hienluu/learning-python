#thread, process, and asyncio

import threading
import multiprocessing
# good for io bound tasks using a single thread with event loop to manage multiple co-routines
# more efficient it doesn't need to manage thousands of threads like the ThreadPoolExecutor
import asyncio
import time
# ProcessPoolExecutor is good for cpu bound tasks
# ThreadPoolExecutor is good for io bound tasks
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def do_work(task_id: int, duration: float) -> str:
    time.sleep(duration)
    return f"Task {task_id} completed"

def run_sync_work(task_no: int = 5) -> list[str]:
    print("==== run_sync_work Example ====")
    results: list[str] = []
    for i in range(task_no):
        result:str = do_work(i, 0.1)
        results.append(result)
    return results

def run_sync_work_example():
    print("==== Running run_sync_work_example ====")
    start_time: float = time.perf_counter()
    results: list[str] = run_sync_work()
    elapsed_time: float = time.perf_counter() - start_time

    print("synchronous results")
    for result in results:
        print(result)
    print(f"total elapsed time: {elapsed_time:.2f} seconds")

def run_async_work_using_threadpool(task_no: int = 5, max_workers: int = 5) -> list[str]:
    print("==== Running run_async_work_using_threadpool ====")
    results: list[str] = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_work, i, 0.1) for i in range(task_no)]

        for future in as_completed(futures):
            results.append(future.result())

    return results

def do_cpu_bound_work(task_id: int, iterations: int = 1000000) -> str:
    result:int = 0
    for i in range(iterations):
        result += (i * i)
    return f"Task {task_id} completed with results: {result}"

def run_cpu_bound_work(task_no: int = 5, max_workers: int = 5) -> list[str]:
    print("==== Running run_cpu_bound_work using process pool executor ====")
    results: list[str] = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(do_cpu_bound_work, i, 1000000) for i in range(task_no)]

        for future in as_completed(futures):
            results.append(future.result())

    return results

def run_cpu_bound_work_example():
    print("==== Running run_cpu_bound_work_example ====")
    start_time: float = time.perf_counter()
    results: list[str] = run_cpu_bound_work(5,5)
    elapsed_time: float = time.perf_counter() - start_time

    print("cpu bound results")
    for result in results:
        print(result)
    print(f"total elapsed time: {elapsed_time:.2f} seconds")

def run_threaded_work_example():
    print("==== Running run_threaded_work_example ====")
    start_time: float = time.perf_counter()
    results: list[str] = run_async_work_using_threadpool(5)

    elapsed_time: float = time.perf_counter() - start_time

    print("asynchronous results using threadpool")
    for result in results:
        print(result)
    print(f"total elapsed time: {elapsed_time:.2f} seconds")


async def do_async_io_work(task_id: int, duration: float) -> str:
    await asyncio.sleep(duration) # non blocking
    return f"Task {task_id} completed"

async def run_async_io_work(task_no: int = 5) -> list[str]:
    print("==== Running run_async_io_work ====")
    tasks = [do_async_io_work(i, 0.1) for i in range(task_no)]
    results = await asyncio.gather(*tasks)
    print(f"results type: {type(results)}")
    return list(results)

def run_async_io_work_example():
    print("==== Running run_async_io_work_example ====")
    start_time: float = time.perf_counter()
    # need to call asyncio.run to run the asyncio program and wait for the results
    results: list[str] = asyncio.run(run_async_io_work(5))
    elapsed_time: float = time.perf_counter() - start_time
    print(f"total elapsed time: {elapsed_time:.2f} seconds")
    print("async io results")
    for result in results:
        print(result)

    print("tasks run concurrently using asyncio (run and gather methods) for modern I/O bound tasks")
    


if __name__ == "__main__":
    # from this video https://www.youtube.com/watch?v=QlkXji08lno
    #run_sync_work_example()
    print("--------------------------------")
    #run_threaded_work_example()
    print("--------------------------------")
    #print(run_cpu_bound_work_example())
    run_async_io_work_example()