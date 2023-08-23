import threading
import time


def mythread():
    time.sleep(1000)


def main():
    threads = 0  # thread counter
    y = 1000000  # a MILLION of 'em!
    for i in range(y):
        try:
            x = threading.Thread(target=mythread, daemon=True)
            threads += 1  # thread counter
            x.start()  # start each thread
        except RuntimeError:  # too many throws a RuntimeError
            break
    print("{} threads created.\n".format(threads))


print(__name__)
if __name__ == "__main__":
    main()
