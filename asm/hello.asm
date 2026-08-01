section .data
    msg db "Hello, World!", 10
    len equ $ - msg

section .text
    global _start

_start:
    ; sys_write(int fd, const char *buf, size_t count)
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    ; sys_exit(int error_code)
    mov rax, 60
    mov rdi, 0
    syscall
