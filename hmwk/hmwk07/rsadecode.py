#! /usr/bin/python

def computePow (m,n,e): 
    """ The idea is to compute m^e mod n """
    p = m #
    r = 1 # 
    while ( e > 0):
        if (e %2 == 1):
            r = (r * p)%n
        p = (p*p) % n
        e = e // 2
    return r %n

def decodeMessageList (l, n, d):
    l = list(map(lambda j: computePow(j,n,d) % 256, l))
    l1 = list(map(chr, l))
    s = ''.join(l1)
    return s


if __name__ == "__main__":
    import sys
    print('Enter filename to decode:', end=" ")
    encFile = input()
    f1 = open (encFile,'r')
    dlist = []
    for line in f1:
        dlist.append(int(line))
    print('   >> OK! Encoded msg:', str(dlist))
    f1.close()
    print('Enter key file: ', end= " ")
    keyFile = input()
    print('   >> I will read keys from: ', keyFile)
    f = open(keyFile,'r')
    n = int(f.readline())
    e = int(f.readline())
    print('   >> n=',n,' d= ',e)
    s = decodeMessageList(dlist,n,e)
    print('   >> decoded message: ', s)
    
    
