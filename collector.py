import datetime
import time

def main():
    for i in range(0, 100):
        with open('LOGS.txt', 'a') as file:
            file.write(f'[{datetime.datetime.now()}]: LOGGED\n')
            time.sleep(5)

if __name__ == '__main__':
    main()