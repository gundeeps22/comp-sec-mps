#!/usr/bin/python

import sys, base64, urllib2, copy

BLOCKSIZE = 16
URL = 'http://192.17.90.133:9999/mp1/mschoi2/?'

def getUrlContent(url, debug=False):
    req = urllib2.Request(url)
    try:
        f = urllib2.urlopen(req)
        if debug:
                print f.read(), f.code
        return True
    except urllib2.HTTPError, e:
        if debug:
                print e.read(), e.code
        if e.code == 404: # correct padding
                return True
        return False # bad padding

def hexStr2ByteArray(strHex):
    hexData = strHex.decode('hex')
    return bytearray(hexData)

def byteArray2HexStr(byteA):
    s = ''
    for c in byteA:
        s += chr(c)
    return s.encode('hex')

def decrypt_block(block, next_block):
    c_prime = copy.copy(block)
    plain_block = bytearray(16)
    g_block = bytearray(16)
    for i in reversed(range(0, 16)):
        for j, k in zip(range(1, 16-i), range(i+1, 16)):
            c_prime[k] = g_block[k] ^ (16-j)
            c_prime[k]
            
        for g in range(0, 256):
            c_prime[i] = g^16
            c_prime[i]
            test_ciphertext = byteArray2HexStr(c_prime)
            test_ciphertext += byteArray2HexStr(next_block)
            if(getUrlContent(URL+test_ciphertext, True)):
                g_block[i] = g
                break
    
    for i in (range(0, 16)):
        plain_block[i] = g_block[i] ^ block[i]
    partial_plaintext = byteArray2HexStr(plain_block)
    return partial_plaintext

def main():
    with open('1.2.3_ciphertext.hex') as c:
        ciphertext = (c.read().strip()).upper()

    byteCipherText = hexStr2ByteArray(ciphertext)
    numBlocks = len(byteCipherText) / 16
    cipher_blocks = [byteCipherText[16*idx:16*(idx+1)] for idx in range(numBlocks)]
    
    plaintext = ''
    for i in reversed(range(1, numBlocks)):
        plaintext = decrypt_block(cipher_blocks[i-1], cipher_blocks[i]) + plaintext
    
    print plaintext
    print plaintext.decode('hex')

    with open('sol_1.2.3.txt', 'wb') as f:
        f.write(plaintext.decode('hex'))

if __name__ == '__main__':
    main()

