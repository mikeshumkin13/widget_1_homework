import functools
import sys


def log(filename: str = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            message = f"Function {func.__name__} started."
            if filename:
                with open(filename, 'a') as f:
                    print(message, file=f)
            else:
                print(message)

            try:
                result = func(*args, **kwargs)
                message = f"Function {func.__name__} completed successfully. Result: {result}"
                if filename:
                    with open(filename, 'a') as f:
                        print(message, file=f)
                else:
                    print(message)

                return result
            except Exception as e:
                message = f"Function {func.__name__} failed with error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a') as f:
                        print(message, file=f)
                else:
                    print(message)

                raise

        return wrapper

    return decorator
