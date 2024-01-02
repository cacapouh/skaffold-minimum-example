import time


def main():
    count = 0
    while True:
        count += 1
        print("{} Hello Skaffold".format(count))
        time.sleep(1)


if __name__ == '__main__':
    main()
