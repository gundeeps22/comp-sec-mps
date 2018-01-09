#!/usr/bin/python

import sys, getopt, binascii
from Crypto import Random
from Crypto.Cipher import AES

def main(argv):
    # parse the command line
    # there are 4 arguments: ciphertext_file, key_file, iv_file, output_file
    ciphertext_file = ''
    key_file = ''
    iv_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, '', ["ifile=","ifile2=","ifile3=","ofile="])
    except getopt.GetoptError:
        print 'Error! Usage: your_script.py ciphertext_file key_file iv_file output_file'
        sys.exit(2)
    ciphertext_file = args[0]
    key_file = args[1]
    iv_file = args[2]
    output_file = args[3]

    # read each file and convert them from hex to binary
    file = open(ciphertext_file, "r")
    ciphertext = binascii.unhexlify(file.read())
    file2 = open(key_file, "r")
    key = binascii.unhexlify(file2.read())
    file3 = open(iv_file, "r")
    iv = binascii.unhexlify(file3.read())

    # decrypt using PyCrypto library and write them in the output file
    mode = AES.MODE_CBC
    decryptor = AES.new(key, mode, IV=iv)
    plaintext = decryptor.decrypt(ciphertext)
    file4 = open(output_file, "w")
    file4.write(plaintext)

    file.close()
    file2.close()
    file3.close()
    file4.close()

if __name__ == "__main__":
    main(sys.argv[1:])
