def get_table(n):
    print('Mod {} Add'.format(n))
    for i in range(n):
        for j in range(n):
            print((i + j) % n, end = ' ')
        print('')
    print('Mod {} Multiply'.format(n))
    for i in range(n):
        for j in range(n):
            print((i * j) % n, end = ' ')
        print('')

def main():
    get_table(5)
    get_table(6)

if __name__ == '__main__':
    main()