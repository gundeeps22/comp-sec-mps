#!/usr/bin/python

import sys, getopt

def main(argv):
    # parse the command line
    # there are 3 arguments: ciphertext_file, key_file, output_file
    ciphertext_file = ''
    key_file = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, '', ["ifile=","ifile2=","ofile="])
    except getopt.GetoptError:
        print 'Error! Usage: your_script.py ciphertext_file key_file output_file'
        sys.exit(2)
    ciphertext_file = args[0]
    key_file = args[1]
    output_file = args[2]
    
    # decipher the key (make a dictionary to map {encrypted : decrypted})
    dict = {}
    letter = 'A'
    with open(key_file) as f:
        while True:
            c = f.read(1) # read one letter at a time
            if not c: # if reached EOF
                break
            if c == ' ': # ignore spaces
                continue
            elif c.isdigit(): # ignore numbers
                continue
            else:
                dict[c] = letter
                letter = chr(ord(letter)+1) # increment to the next letter

    # write the decrypted letters to an output file
    with open(ciphertext_file) as f:
        f2 = open(output_file, "w")
        while True:
            c = f.read(1)
            if not c:
                break
            if c == ' ':
                f2.write(' ')
            elif c.isdigit():
                f2.write(c)
            else:
                f2.write(dict[c])
        f2.close()
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
