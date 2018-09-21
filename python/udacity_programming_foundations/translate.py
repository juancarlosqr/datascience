#!/usr/bin/python

def run_test():
    intab = 'aeiou'
    outtab = '54321'
    trantab = str.maketrans(intab, outtab)

    result = 'this is string example....wow!!!'
    print(result)
    print(result.translate(trantab))

    trantab = str.maketrans(outtab, intab)
    print(result.translate(trantab))

if __name__ == '__main__':
    run_test()