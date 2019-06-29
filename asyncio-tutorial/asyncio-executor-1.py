""" Combine coroutine with Thread
    This can be better than multithreading only because:
    - event loop never get blocked and executor workers will run task instead
    - event loop can go work on something else while wait to workers to complete their jobs
"""
import time
import asyncio
import threading
import concurrent.futures


def blocking_func(n):
    """ This is a blocking function
        no asyncio.sleep() used, no await
    """
    time.sleep(0.5)
    return n**2


async def main(loop, executor):
    print("Creating executor tasks")
    blocking_tasks = [
        # run_in_executor is a coroutine
        loop.run_in_executor(executor, blocking_func, i) for i in range(6)
    ]
    print("Waiting for tasks to complete")
    results = await asyncio.gather(*blocking_tasks)
    print("Results: {!r}".format(results))


if __name__ == "__main__":
    start = time.perf_counter()
    # Create 1 executor with 3 workers
    # worker in executor will be distributed to work on multiple coroutines
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=6)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop, executor))
    finally:
        loop.close()
        print("Time spent {}".format(time.perf_counter() - start))

    # Use multithreading only
    # start = time.perf_counter()
    # thread_list = []
    # for i in range(6):
    #     t = threading.Thread(target=blocking_func, args=(i,))
    #     t.start()
    #     thread_list.append(t)
    # for t in thread_list:
    #     t.join()
    # print("Time spent multithreading {}".format(time.perf_counter() - start))

