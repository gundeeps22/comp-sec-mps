#!/usr/bin/python

import sys, getopt, hashlib

def main(argv):
    # parse the command line
    # there are 3 arguments: input_string, perturbed_string, output_file
    input_string_file = ''
    perturbed_string_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, '', ["ifile=","ifile2=","ofile="])
    except getopt.GetoptError:
        print 'Error! Usage: your_script.py file_1.txt file_2.txt output_file'
        sys.exit(2)
    input_string_file = args[0]
    perturbed_string_file = args[1]
    output_file = args[2]
    
    # read each file
    file = open(input_string_file, "r")
    file2 = open(perturbed_string_file, "r")

    # Convert input_string into input_hash_bin, then put the binary str into an array
    input_string = file.read().strip()
    input_hash = hashlib.sha256()
    input_hash.update(input_string)
    input_hash_hex = input_hash.hexdigest()
    input_hash_bin = bin(int(input_hash_hex, 16))[2:].zfill(256) # to avoid possible leading 0s
    u = [int(d) for d in input_hash_bin]

    # Convert perturbed_string into perturbed_hash_bin, then put the binary str into an array
    perturbed_string = file2.read().strip()
    perturbed_hash = hashlib.sha256()
    perturbed_hash.update(perturbed_string)
    perturbed_hash_hex = perturbed_hash.hexdigest()
    perturbed_hash_bin = bin(int(perturbed_hash_hex, 16))[2:].zfill(256) # same reason as above
    v = [int(d) for d in perturbed_hash_bin]

    # Calculate the hamming distance between two arrays
    hamming_distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            hamming_distance += 1
    hamming_distance = hex(hamming_distance)[2:] # switch to hex

    ofile = open(output_file, "w")
    ofile.write(hamming_distance)

    file.close()
    file2.close()
    ofile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
