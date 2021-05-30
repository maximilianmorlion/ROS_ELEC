import time

def main():
    while True:
        now = time.localtime()
        print("Current time: ", time.asctime(now))
        time.sleep(1)
    return

if __name__ == "__main__":
    main()