from functools import wraps
from datetime import datetime
def Time(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
      start=datetime.now()
      result = func(*args, **kwargs)
      end=datetime.now()
      print(f"Execution time: {end - start}")
      return result
  return wrapper

def cache(func):
    cache_data = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache_data:
            return cache_data[args]
        else:
            result = func(*args, **kwargs)
            cache_data[args] = result
            print(result)
            return result
    return wrapper



@Time
@cache
def fib_cached(n):
    if n <= 1:
        return n
    else:
        return fib_cached(n - 1) + fib_cached(n - 2)

@Time
def fib_no_cache(n):
    if n <= 1:
        return n
    else:
        return fib_no_cache(n - 1) + fib_no_cache(n - 2)

if __name__ == '__main__':
    print(fib_cached(7))
    print(fib_no_cache(7))
