.section .data
filename:
.asciz  "/bin/sh"

.global _main
.section .text

_main:

pushl    %ebp
movl    %esp,%ebp
subl    $0x8, %esp

movl    $filename, %edi
movl    %edi, -0x8(%ebp)
movl    $0, -0x4(%ebp)

movl    $11, %eax
movl    $filename, %ebx
leal    -8(%ebp), %ecx
movl    $0, %edx
int     $0x80

leave
ret

