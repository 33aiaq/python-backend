import time

start = time.perf_counter()


def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")



do_something()


finiish = time.perf_counter()
print(f"Finished in {round(finiish - start, 2)} second(s)")
