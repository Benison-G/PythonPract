import asyncio
from datetime import datetime

def debounceFun(fn):
    async def wrapper(n):
        start = datetime.now()
        await fn(n)
        end = datetime.now()
        print("Elapsed time: ", end - start)
    return wrapper

@debounceFun
async def printNumbers(n):
    for i in range(1, n+1):
        await asyncio.sleep(1)
        print(i)

asyncio.run(printNumbers(5))
