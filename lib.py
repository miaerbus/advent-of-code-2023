import time


def my_timer(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f"Starting {func_name}")

        t1 = time.perf_counter()
        output = func(*args, **kwargs)
        t2 = time.perf_counter()

        print(f"Total time for {func_name}: {t2 - t1:.9f} s\n")
        return output

    return wrapper


# https://stackoverflow.com/questions/8848294/how-to-get-char-from-string-by-index
def find_all(string, sub):
    start = 0
    while True:
        start = string.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches
