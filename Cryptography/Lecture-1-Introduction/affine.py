from gmpy2 import invert

def enc(str, a, b, m):
    res = ""
    for i in str:
        ch = chr(ord('a') + (a * (ord(i) - ord('a')) + b) % m)
        res += ch
    return(res)

def dec(str, a, b, m):
    res = ""
    for i  in str:
        ch = chr((invert(a, m) * (ord(i) - ord('a') - b)) % m + ord('a'))
        res += ch
    return(res)

def main():
    str1 = 'security'
    str2 = 'vlxijh'
    print(enc(str1, 7, 21, 26))
    print(dec(str2, 7, 21, 26))

if __name__ == '__main__':
    main()