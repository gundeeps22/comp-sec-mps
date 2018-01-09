#!/usr/bin/python

import sys, getopt, binascii

def main(argv):
    # parse the command line
    # there are 2 arguments: input_file, output_file
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, '', ["ifile=","ofile="])
    except getopt.GetoptError:
        print 'Error! Usage: your_script.py file.txt output_file'
        sys.exit(2)
    input_file = args[0]
    output_file = args[1]

    # read the input file
    file = open(input_file, "r")
    inStr = file.read().strip()
    #char_list = list(inStr)
    #changed_inStr = ''.join(sorted(char_list))
    outHash = WHA(inStr)
    ofile = open(output_file, "w")
    ofile.write(outHash)
    file.close()
    ofile.close()

# weak hashing algorithm
def WHA(input_string):
    #inStr = bin(int(binascii.hexlify(input_string), 16))[2:]
    #inStr = inStr.zfill(8*((len(inStr)+7) // 8)) # padding
    inStr = map(bin, bytearray(input_string))
    mask = 0x3FFFFFFF
    outHash = 0
    for byte in inStr:
        intermediate_value = ((int(byte,2) ^ 0xCC) << 24) | ((int(byte,2) ^ 0x33) << 16) | ((int(byte,2) ^ 0xAA) << 8) | (int(byte,2) ^ 0x55)
        outHash = (outHash & mask) + (intermediate_value & mask)
    return hex(outHash).rstrip("L").lstrip("0x") or "0"

if __name__ == "__main__":
	main(sys.argv[1:])
