def exgcd(a, b):     
    if b == 0:         
        return 1, 0, a     
    else:         
        x, y, q = exgcd(b, a % b)        
        x, y = y, (x - (a // b) * y)         
        return x, y, q

def main():
    a = 3
    b = 5
    tx, ty, tq = exgcd(a, b)
    print('the gcd of {}, {} is {}.'.format(a, b, tq))
    print('the invert value of {} in mod {} is {}'.format(a, b, tx))

if __name__ == '__main__':
    main()