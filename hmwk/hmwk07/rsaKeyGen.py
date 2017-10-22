import sys
import random

def toBinary(n):
  r = []
  while (n > 0):
    r.append(n % 2)
    n = n // 2
  return r

def test(a, n):
  """
  test(a, n) -> bool Tests whether n is composite.

  Returns:
    - True, if n is composite.
    - False, if n is probably prime.
  """
  b = toBinary(n - 1)
  d = 1
  for i in range(len(b) - 1, -1, -1):
    x = d
    d = (d * d) % n
    if d == 1 and x != 1 and x != n - 1:
      return True # Composite
    if b[i] == 1:
      d = (d * a) % n
  if d != 1:
    return True # Composite
  return False # Prime

def MillerRabin(n, s = 50):
  """
    MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not

    Returns:
      - True, if n is probably prime.
      - False, if n is composite.
  """
  for j in range(1, s + 1):
    a = random.randint(1, n - 1)
    if (test(a, n)):
      return False # n is composite
  return True # n is prime


def computeGCD(u,v):
    """ The euclidean GCD algorithm """
    if (u > v):
        u,v = v,u
    u1,u2,u3 = 1,0,u
    v1,v2,v3 = 0,1,v
    while (v3 > 0):
        q = u3//v3
        t1 = u1 - q * v1
        t2 = u2 - q * v2
        t3 = u3 - q * v3
        u1,u2,u3 = v1,v2,v3
        v1,v2,v3 = t1,t2,t3
    return u1,u2,u3


def computePublicKey(k):
    e = 3
    i = k//3
    iLim = 2*k//3
    while ( i < iLim): 
        e = i
        i = i +1
        (a,b,l) = computeGCD(e,k)
        if (l == 1):
            return e
    print('Finding public key fail.')
    assert false
    return e


def computePrivateKey(k,e):
    (d,v,l) = computeGCD(e,k)
    assert (l == 1)
    assert( d * e + v * k == 1)
    # d * e + v * k = 1
    # k * e - e * k = 0
    # therefore (d + m* k)  * e + (v - m * e) k = 1
    if ( d < 0):
        m = int (-d//k) + 1 
        d = d + m * k
    return d


def generateRandomPrimes(s = 5):
  """ fun. generateRandomPrimes: int -> (int,int)
      generate a pair of random prime numbers """
  x = random.randint(10**(s-1), 10 ** s)
  i = x;
  while ( i < 2 * x):
    if (MillerRabin(i,50)):
      return i
    i = i + 1

  print ('Prime Number Gen. Failed')
  # assert false
  return -1


if __name__ == "__main__":
    import sys
    if (len(sys.argv) >= 3):
      p,q = int(sys.argv[1]),int(sys.argv[2])
    elif (len(sys.argv) >= 2):
      p = generateRandomPrimes(int(sys.argv[1]))
      q = generateRandomPrimes(int(sys.argv[1]))
    else:
      p = generateRandomPrimes()
      q = generateRandomPrimes()

    assert(MillerRabin(p))
    assert(MillerRabin(q))
    print('p = ',p,' q = ', q)
    print('n = ', p * q)
    k = (p-1) * (q-1)
    e = computePublicKey(k)
    print('e = ', e)
    d = computePrivateKey(k,e)
    print('d = ', d)
    


