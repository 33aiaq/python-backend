from multiprocessing import Process
import time

def square_numbers():
    for i in range(5):
        print(f"{i} squared = {i*i}")
        time.sleep(1)

if __name__ == "__main__":
    # create two processes
    p1 = Process(target=square_numbers)
    p2 = Process(target=square_numbers)

    # start processes
    p1.start()
    p2.start()

    # wait until they finish
    p1.join()
    p2.join()

    print("Both processes finished!")
