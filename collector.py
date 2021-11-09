import datetime

def main():
    with open('LOGS.txt', 'a') as file:
        file.write(f'[{datetime.datetime.now()}]: LOGGED\n')

if __name__ == '__main__':
    main()