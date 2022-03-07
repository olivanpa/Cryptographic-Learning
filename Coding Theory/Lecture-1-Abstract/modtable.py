def get_table(n):
    print('Mod {} Add\n+ '.format(n), end = '')
    for i in range(n):
        print('{:3}'.format(i), end = ' ')
    print('')
    for i in range(n):
        print(i, end=' ')
        for j in range(n):
            print('{:3}'.format((i + j) % n), end = ' ')
        print('')

    print('Mod {} Multiply\n* '.format(n), end = '')
    for i in range(n):
        print('{:3}'.format(i), end = ' ')
    print('')
    for i in range(n):
        print(i, end=' ')
        for j in range(n):
            print('{:3}'.format((i * j) % n), end = ' ')
        print('')

def main():
    get_table(5)
    get_table(6)

if __name__ == '__main__':
    main()