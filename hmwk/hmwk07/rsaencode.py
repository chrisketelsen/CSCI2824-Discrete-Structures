#! /usr/bin/python

def computePow (m,n,e): 
    """ The idea is to compute m^e mod n """
    p = m
    r = 1
    while ( e > 0):
        if (e %2 == 1):
            r = (r * p)%n
        p = (p*p) % n
        e = e // 2
    return r %n


def encodeMessageString (s, n, e):
    """ Encode a string as a sequence of RSA numbers """
    l = list(s)
    l1 = list(map(lambda c: ord(c), l))
    print(l1)
    l2 = list(map(lambda j: computePow(j,n,e), l1))
    return l2

if __name__ == "__main__":
    import sys
    print('Enter the string to encode:', end=" ")
    st = input()
    print('Enter key file: ', end=" ")
    keyFile = input()
    print(' >> I will read keys from: ', keyFile)
    f = open(keyFile,'r')
    n = int(f.readline())
    e = int(f.readline())
    print(' >> n=',n,' e= ',e)
    dlist = encodeMessageString(st,n,e)
    print(' >> Encoded Message Stream: ', dlist)
    f.close ()
    print('Where should I write the encoded message to? ', end=" ")
    outFile = input()
    f = open(outFile, 'w')
    for n in dlist:
        f.write(str(n))
        f.write('\n')
    f.close()
    print(' >> done. ')

