#!/usr/bin/python

import sys, getopt, math

def main(argv):
    # parse the command line
    # there are 4 arguments: ciphertext_file, key_file, modulo_file, output_file
    ciphertext_file = ''
    key_file = ''
    modulo_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, '', ["ifile=","ifile2=","ifile3=","ofile="])
    except getopt.GetoptError:
        print 'Error! Usage: your_script.py ciphertext_file key_file modulo_file output_file'
        sys.exit(2)
    ciphertext_file = args[0]
    key_file = args[1]
    modulo_file = args[2]
    output_file = args[3]
    
    # read each file and convert them from hex to binary
    file = open(ciphertext_file, "r")
    file2 = open(key_file, "r")
    file3 = open(modulo_file, "r")
    ciphertext = int(file.read().strip(), 16)
    key = int(file2.read().strip(), 16)
    modulo = int(file3.read().strip(), 16)
        
    # decrypting with RSA
    plaintext = 1
    for e in range(1, key+1):
            plaintext = (plaintext*ciphertext)%modulo
    p = hex(int(plaintext))[2:]

    # another way of decrypting
    # plaintext = hex(pow(ciphertext, key, modulo)).rstrip("L")
    # print(plaintext)

    ofile = open(output_file, "w")
    ofile.write(p)

    file.close()
    file2.close()
    file3.close()
    ofile.close()

if __name__ == "__main__":
    main(sys.argv[1:])

