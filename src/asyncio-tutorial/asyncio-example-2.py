""" Basic asyncio examples with asyncio.wait()
    A easier way to wait on multiple coroutines
    
    asyncio.wait(future, *, loop=None, timeout=None, return_when=ALL_COMPLETED) 
        itself is a coroutine
        use `await` will wait on this coroutine
        return (done, pending)
        
    Replacement for asyncio.wait()
        asyncio.gather() vs asyncio.wait(): 
        https://stackoverflow.com/questions/42231161/asyncio-gather-vs-asyncio-wait
    results = await asyncio.gather(*item_coros)
"""
import time
import asyncio 


async def get_item(i):
    await asyncio.sleep(1)
    return 'item' + str(i)


async def get_items(num_items):
    print("Getting items")
    item_coros = [
        get_item(i)
        for i in range(num_items)
    ]
    print("Waiting for tasks to complete")
    completed, pending = await asyncio.wait(item_coros, timeout=None)
    
    if pending:
        print("Canceling remaining tasks")
        for t in pending:
            t.cancel()

    if pending:
        raise asyncio.TimeoutError  # Timeout Exception

    results = [t.result() for t in completed]
    print("results: {!r}".format(results))


if __name__ == "__main__":
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    try:
        # get_items() is a future, loop will wait until it's complete
        loop.run_until_complete(get_items(9))
    finally:
        loop.close()
        print("Time spent: {}".format(time.perf_counter() - start))
