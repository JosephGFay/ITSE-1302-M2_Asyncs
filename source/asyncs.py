import asyncio
from utils import Question, Answer, exercise

@exercise
def asyncs():
  
  #1 
  Question(1, """
    Implement an asynchronous coroutine function to add two variables and 
    sleep for the duration of the sum. Use the async loop to call the function 
    with two numbers.
  """)
  async def sum(a, b):
    print(f'\tStarting sum({a},{b})')
    await asyncio.sleep(a+b)
    return a + b

  results = asyncio.run(sum(2,3))
  Answer(results)

  #2 
  Question(2, """
    Change the previous program to schedule the execution of two calls 
    to the sum function
  """)
  async def scheduler(*args):
    return await asyncio.gather(*args)
    
  results = asyncio.run(scheduler(sum(2,3), sum(1,2)))
  Answer(results)



