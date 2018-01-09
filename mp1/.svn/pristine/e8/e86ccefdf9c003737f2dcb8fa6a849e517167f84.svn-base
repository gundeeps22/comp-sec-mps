#!/usr/bin/python

from fractions import gcd
from Crypto.PublicKey import RSA
import math, pbp, sys

sys.setrecursionlimit(1000000)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b%a, a)
        return (g, y - (b // a)*x, x)

def mulinv(a, b):
    g, x, _ = egcd(a, b)
    if g == 1:
        return x % b

def product_fast(X):
    if len(X) == 0: return 1
    while len(X) > 1:
        if len(X) % 2 != 0:
            loner = X[-1]
            X = [X[i*2]*X[i*2+1] for i in range(((len(X)+1)/2)-1)]
            X.append(loner)
        else:
            X = [X[i*2]*X[i*2+1] for i in range((len(X)+1)/2)]
    return X[0]

def producttree(X):
    result = [X]
    while len(X) > 1:
        #print 'Multiplying...'
        if len(X) % 2 != 0:
            loner = X[-1]
            X = [X[i*2]*X[i*2+1] for i in range(((len(X)+1)/2)-1)]
            X.append(loner)
            result.append(X)
        else:
            X = [X[i*2]*X[i*2+1] for i in range((len(X)+1)/2)]
            result.append(X)
    return result

def remaindersusingproducttree(n,T):
    result = [n]
    for t in reversed(T):
        result = [result[i/2] % t[i] for i in range(len(t))]
    return result

def remainders(n,X):
    return remaindersusingproducttree(n, producttree(X))

def batchgcd_simple(X):
    R = remainders(product_fast(X), [n**2 for n in X])
    return [gcd(r/n,n) for r,n in zip(R,X)]

def batchgcd_faster(X):
    prods = producttree(X)
    R = prods.pop()
    while prods:
        #print 'GCDing...'
        X = prods.pop()
        R = [R[i/2] % X[i]**2 for i in range(len(X))]
    return [gcd(r/n,n) for r,n in zip(R,X)]


def main():
    with open('1.2.4_ciphertext.enc.asc') as c:
        ciphertext = c.read()
    with open('moduli.hex') as n:
        moduli = []
        for line in n:
            moduli.append(int(line, 16))
    
    P = batchgcd_faster(moduli)
    #print(P)
    for i in range(len(P)):
        if P[i] == 1:
            pass
        else:
            q = moduli[i]/P[i]
            totient = (P[i]-1)*(q-1)
            e = 65537L
            d = mulinv(e, totient)
            N = moduli[i]
            try:
                private_key = RSA.construct((N, e, d))
                plaintext = pbp.decrypt(private_key, ciphertext)
                outputfile = open('sol_1.2.4.txt', 'w')
                outputfile.write(plaintext)
                outputfile.close()
            except:
                #print 'Wrong private key!'
                pass

if __name__ == "__main__":
    main()
