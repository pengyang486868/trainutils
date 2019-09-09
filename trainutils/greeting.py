import os

dirname, filename = os.path.split(os.path.abspath(__file__))


def sayhello():
    # file name fit linux
    f = open(os.path.join(dirname, 'greeting.txt'), 'r')
    lines = 0
    for row in f:
        lines += 1
        print(row.strip())
    print()
    print('total', str(lines), 'lines')


if __name__ == '__main__':
    sayhello()
