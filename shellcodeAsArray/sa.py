#!/usr/bin/env python
#from isis import chunk
from sys import argv
if len(argv)<2:
    print 'Usage: {} <shellcode> [<bytes/line>]'.format(argv[0])
    exit(1)

LINE_LEN=15
if len(argv)>2:
    LINE_LEN=int(argv[2])

shellcode = file(argv[1]).read()
hex_bytes="\\x"
hex_bytes+="\\x".join([i.encode('hex').zfill(2) for i in shellcode])
print "Shellcode=",hex_bytes
print "Byte:\n",len(shellcode)



