def sayhello():
    f = open('greeting.txt', 'r')
    lines = 0
    for row in f:
        lines += 1
        print(row.strip())
    print('total', str(lines), 'lines')


if __name__ == '__main__':
    sayhello()
