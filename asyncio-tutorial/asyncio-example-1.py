""" Basic asyncio examples, asyncio.run_until_complete & coroutine chaining
"""
import time
import asyncio


async def say_hello():
    """ Simple asyncio example
    """
    print("Hello World!")

    # Run below in main
    # loop = asyncio.get_event_loop()  # create event loop
    # print(loop.is_running())  # not running at this point
    # loop.run_until_complete(future=say_hello())  # loop is running now
    # print(loop.is_running())  # not running at this point
    # loop.close()  # close finished loop

    # Run below in main: task switching
    # loop = asyncio.get_event_loop()
    # asyncio.ensure_future(delayed_hello(), loop=loop)
    # asyncio.ensure_future(say_hello(), loop=loop)
    # loop.run_forever()  # this is a blocking method, it will never reach to next line
    # loop.stop() 
    # loop.close()

async def delayed_hello():
    """ Asyncio with await example
    """
    print("Hello ")
    await asyncio.sleep(1)  # switch to other task when doing this time consuming job
    print("World!")

    # Run below in main
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(delayed_hello())
    # loop.close()


async def chain_coroutine():
    print("Performing task")
    print("Waiting for result1")
    result1 = await subtask1()
    print("Waiting for result2")
    result2 = await subtask2(result1)
    return (result1, result2)

    # Run below in main
    # loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(chain_coroutine())
    # print("Get result {}".format(result))
    # loop.close()


async def subtask1():
    print("Perform subtask1")
    await asyncio.sleep(1)
    return "result1"


async def subtask2(arg):
    print("Perform subtask2")
    await asyncio.sleep(1)
    return "result2 relies on {}".format(arg)


if __name__ == "__main__":
    pass
