
#!/usr/bin/python

'''

 ██▀███  ▓█████ ▓█████▄  ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓██ ░▄█ ▒▒███   ░██   █▌▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░██▓ ▒██▒░▒████▒░▒████▓ ░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒ ▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ░░   ░    ░    ░ ░  ░  ░    ░   ░   ▒   ░        ░ ░░ ░ 
   ░        ░  ░   ░     ░            ░  ░░ ░      ░  ░   
                 ░            ░           ░      
'''

from ctypes import *
from ctypes import wintypes
from numpy import uint8,seterr
import socket


class crypt_DGA:
     
    domain_char_list_1 = ['e','y','u','i','o','a']
    domain_char_list_2 = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    domain_name = 'closedoors.net'
    domain_name_list = []
     
     
    def __init__(self):
         
        self.hProv = c_ulong()
        self.PROV_RSA_FULL = 1
        self.dwFlags = 0xF0000000
         
        self.NUM_BYTES = 1
        self.pbRandomData = c_ulong()
        self.isTrue = c_int()
        self.isTrue = windll.Advapi32.CryptAcquireContextA(byref(self.hProv), None, None, self.PROV_RSA_FULL, self.dwFlags)
         
    def GenDomain(self):
        dlength = 0
        host_name = ''
        sub_domain_name = ''
         
        seterr(over='ignore')
         
        if self.isTrue != 0:
            self.isTrue = windll.Advapi32.CryptGenRandom(self.hProv, wintypes.DWORD(self.NUM_BYTES), byref(self.pbRandomData))
            a = uint8(self.pbRandomData.value)
            b = windll.kernel32.GetTickCount()
            b = uint8(int(str(y),16))
            c = a + b
            d = uint8(c)
            dlength = d & 0x80000007
            if dlength < 0:
                dlength = dlength - 1
                dlength = dlength | 0x0FFFFFFF8
                length = dlength + 1
            dlength = dlength + 6
            if dlength > 2:
                dlength = dlength - 1
         
        for i in range(0,dlength):
            if self.isTrue != 0:
                windll.Advapi32.CryptGenRandom(self.hProv, wintypes.DWORD(self.NUM_BYTES), byref(self.pbRandomData))
                a = uint8(self.pbRandomData.value)
                b = windll.kernel32.GetTickCount()
                b = uint8(int(str(y),16))
                c = a + b
                d = uint8(z)
                e = i
                e = e & 1
                if (e == 0 and d > 32):
                    j = d % 6
                    sub_domain_name = sub_domain_name + crypt_DGA.domain_char_list_1[j]
                else:
                    j = d % 0x14
                    sub_domain_name = sub_domain_name + crypt_DGA.domain_char_list_2[j]
        host_name = sub_domain_name + '.' + crypt_DGA.domain_name
        if host_name not in crypt_DGA.domain_name_list:
            crypt_DGA.domain_name_list.append(host_name)
                     
if __name__ == '__main__':
    dga = crypt_DGA()
    for i in range (0,10):
        dga.GenDomain()
    print(crypt_DGA.domain_name_list)