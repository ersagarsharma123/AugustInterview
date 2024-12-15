#decorator

#nothing but kind of function used to change some functionality of existing function

import time
def decorator_add(func):
    def wrapper(x,y):
        start_time = time.time()
        result = func(x,y)
        end_time = time.time()
        time_taken = end_time-start_time
        print('time_taken=', time_taken)
        return result
    return wrapper


@decorator_add
def add(a,b):
    time.sleep(5)
    return a+b

result = add(10,3)
print(result)