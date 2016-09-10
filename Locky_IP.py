from numpy import uint32, uint16, uint8, seterr
from goto import with_goto
import copy
import binascii
from rotate import __ROR4__,__ROL4__
 
class FindIP:
     
   
    en_list = []
     
     
    AF_ecx,AF_ecx4,AF_ecx8,AF_eax = 0, 0, 0, 0
    DC_eax = 0
     
    49 = []
    list1_49 = [0x10,0x11,0x12,0x0,0x8,0x7,0x9,0x6,0xA,0x5,0xB,0x4,0xC,0x3,0xD,0x2,0xE,0x1,0xF,0x0]
    list2_49 = []
    temp_list  = []
    list6_49 = []
    list8_49 = []
    list9_49 = []
    list11_49 = []
     
    BBDA = [0]*16
    BDF8 = [0]*24
    BE28 = [0]*144
    BF48 = [0]*8
    BF58 = [0]*112
    BB00 = [0]*16
    BB20 = [0]*32
    BD9C = [0]*30
    BAE0 = [0]*32
    BD60 = [0]*30
    BAC0 = [0]*32
    
    final_list = []
    final_1 = []
     
    CC_BUF_LEN = 0x100
    CC_IP = [0]*CC_BUF_LEN
     
    def __init__(self):
        pass
     
    def readData(self):
        CONST_1 = 0x88BBDD8D
        CONST_2 = 0x0DDBCA2B2
        CONST_3 = 0xA078C405
        CONST_4 = 0x72462828
        seterr(over='ignore')
        f_path = input('Enter fullpath of unpacked locky: ')
        f = open(f_path,'rb')
        pos = 0
        while True:
            f.seek(pos,0)
            data = f.read(0x4)
            data = int(binascii.b2a_hex(data[::-1]),16)
            if data != 0:
                temp = data
                temp = temp ^ CONST_1
                data1 = f.read(0x4)
                data1 = int(binascii.b2a_hex(data1[::-1]),16)
                if data1 == temp:
                    data = data ^ CONST_2
                    data2 = f.read(0x4)
                    data2 = int(binascii.b2a_hex(data2[::-1]),16)
                    
                    if data2 == data:
                        break
            pos = pos + 1
        f.seek(pos,0)
        var1 = f.read(0x4)
        var1 = int(binascii.b2a_hex(var1[::-1]),16)
        f.seek(pos + 0x0C,0)
        var2 = f.read(0x4)
        var2 = int(binascii.b2a_hex(var2[::-1]),16)
        var3 = pos + 0x14
        f.seek(pos + 0x10,0)
        var4 = f.read(0x4)
        var4 = int(binascii.b2a_hex(var4[::-1]),16)
       
        decrypt_data_len = var4 ^ var1
        encrypt_data_len = var2 ^ var1
         
        FindIP.CC_IP = [0]*decrypt_data_len
        FindIP.en_list = [0]*encrypt_data_len
        var1 = uint32(var1) + uint32(CONST_3)
        var5 = 0
        f.seek(var3,0)
        if encrypt_data_len != 0:
            while var5 < encrypt_data_len:
                c = uint8(var5)
                c = uint8(c & 0x1F)
                a = uint32(var1)
                a = uint32(__ROL4__(a,c))
                var1 = uint32(__ROR4__(var1,3))
                c = uint32(var5)
                var1 = uint32(var1 + a)
                c = uint32(__ROR4__(c,0x0B))
                c = uint32(c + CONST_4)
                var1 = uint32(var1 ^ c)
                c = f.read(1)
                c = int(binascii.b2a_hex(c[::-1]),16)
                c = uint8(c^uint8(var1))
                FindIP.en_list[var5] = c
                var5 = var5 + 1
     
    def 105B(self):
        FindIP.BB00[5] = 0x20
        FindIP.BBDA[7] = 0x18
        FindIP.BBDA[8] = 0x98
        FindIP.BBDA[9] = 0x70
         
        j = 24
        i = 0
        value = 0x100
        while i < j:
            FindIP.BDF8[i] = value
            value = value + 1
            i = i + 1
         
        j = 144
        i = 0
        while i < j:
            FindIP.BE28[i] = i
            i = i + 1
         
        j = 8
        i = 0
        value = 0x118
        while i < j:
            FindIP.BF48[i] = value
            value = value + 1
            i = i + 1
         
        j = 112
        i = 0
        value = 0x90
        while i < j:
            FindIP.BF58[i] = uint16(value)
            value = value + 1
            i = i + 1
         
        j = 32
        i = 0
        while i < j:
            FindIP.BB20[i] = i
            i = i + 1
        
         
        self.1000(3,FindIP.BD9C,FindIP.BAE0,4)
         
        self.1000(1, FindIP.BD60,FindIP.BAC0,2)
         
        FindIP.BAE0[28] = 0
        FindIP.BD9C[28] = 0x102
         
        FindIP.final_list = FindIP.BAC0 + FindIP.BAE0 + FindIP.BB00 + FindIP.BB20
        FindIP.final_1 = FindIP.BD60 + FindIP.BD9C + FindIP.BBDA + FindIP.BDF8 + FindIP.BE28 + FindIP.BF48 + FindIP.BF58
         
    def 1000(self,arg8,list1,list2,eax):
        esi = eax
         
        self.C7E0(esi, 0, list2 , 0)
         
        i = 0
        j = 0x1E
        j = j - esi
        while i < j:
            value = i / esi
            list2[esi+i] = uint8(value)
            i = i + 1
         
        i = 0
        j = 0x1E
        while i < j:
            list1[i] = uint16(arg8)
            x = uint8(list2[i])
            y = uint32(1 << x)
            arg8 = arg8 + y
            i = i + 1           
                  
    def 11AF(self):
         
        seterr(over='ignore')
         
        x = FindIP.AF_ecx8
        FindIP.AF_ecx8 = FindIP.AF_ecx8 - 1
         
        if x  == 0:
            FindIP.AF_ecx4 = FindIP.en_list[FindIP.AF_ecx]
            FindIP.AF_ecx = FindIP.AF_ecx + 1
            FindIP.AF_ecx8 = 7
             
        FindIP.AF_eax = uint32(FindIP.AF_ecx4 & 1)
        value = uint32(FindIP.AF_ecx4 >> 1)
        FindIP.AF_ecx4 = value
         
    def 11DC(self,ecx,arg4):
        esi,edi,ebx = 1,1,0
         
        if ecx != 0:
            esi = uint32(esi << ecx)
            if esi > edi:
                while True:
                    self.11AF()
                    if FindIP.AF_eax != 0:
                        ebx = ebx + edi
                    edi = edi + edi
                    if edi >= esi:
                        break
        FindIP.DC_eax = arg4
        FindIP.DC_eax = FindIP.DC_eax + ebx
     
    @with_goto
    def 1249(self):
         
        self.11DC(5, 0x101)
        FindIP.49.append(hex(FindIP.DC_eax))
        self.11DC(5, 1)
        FindIP.49.append(hex(FindIP.DC_eax))
        self.11DC(4, 4)
        FindIP.49.append(hex(FindIP.DC_eax))
        FindIP.49 = FindIP.49[::-1]
         
        counter = int(FindIP.49[1],16) + int(FindIP.49[2],16)
        FindIP.list2_49 = [0]*counter
        FindIP.temp_list = [0]*counter
         
        i = 0
        while i < int(FindIP.49[0],16):
            self.11DC(3, 0)
            index = FindIP.list1_49[i]
            i = i + 1
            FindIP.list2_49[index] = FindIP.DC_eax
        
        list3_49 = [0]*0x13
        list4_49 = [0]*0x10
        list5_49 = [0]*0x13
         
        self.1125(0x13,list3_49,list4_49,list5_49)
         
        counter = int(FindIP.49[2],16) + int(FindIP.49[1],16)
        i = 0
        while True:
            eax = self.1211(list3_49,list5_49)
            ecx = eax
            ecx = ecx - 0x10
            if ecx == 0:
                goto .loc_132B
            ecx = ecx - 1
            if ecx == 0:
                goto .loc_1324
            ecx = ecx - 1
            if ecx == 0:
                goto. loc_130C
            FindIP.list2_49[i] = eax
            i = i + 1
            goto .end
             
            label .loc_130C
            self.11DC(7, 0xB)
            edi = FindIP.DC_eax
            if edi == 0:
                goto .end
            goto .loc_134B
             
            label .loc_1324
            self.11DC(3, 3)
            edi = FindIP.DC_eax
            if edi == 0:
                goto .end
            self.C7E0(edi,0,FindIP.list2_49,i)
            i = i + edi
            goto .end
             
            label .loc_132B
            al = uint8(FindIP.list2_49[i-1])
            FindIP.49[0] = al
            self.11DC(2, 3)
            edi = FindIP.DC_eax
            if edi == 0:
                goto .end
            self.C7E0(edi,FindIP.49[0],FindIP.list2_49,i)
            i = i + edi
            goto .end
             
            label .loc_134B
            self.C7E0(edi,0,FindIP.list2_49,i)
            i = i + edi
            label.end
            if i >= counter:
                break
        counter = int(FindIP.49[2],16)
        FindIP.list6_49 = [0]*counter
        list7_49 = [0]*0x10
        FindIP.list8_49 = [0]*counter
        self.1125(counter, FindIP.list6_49, list7_49, FindIP.list8_49)
        FindIP.temp_list = copy.copy(FindIP.list2_49)
         
        counter = int(FindIP.49[1],16)
        end = int(FindIP.49[2],16)
        del FindIP.list2_49[0:end]
        FindIP.list9_49 = [0]*counter
        list10_49 = [0]*0x10
        FindIP.list11_49 = [0]*counter
        self.1125(counter, FindIP.list9_49, list10_49, FindIP.list11_49)
     
    @with_goto   
    def 138D(self):
        i = 0x100
        j = 0
         
        value = self.1211(FindIP.list6_49, FindIP.list8_49)
        if value != i:
            goto .loc_13AE
        goto .end
         
        label .loc_13AE
        if value >= i:
            goto .loc_13BB
        FindIP.CC_IP[j] = uint8(value)
        j = j + 1
        goto .loc_141C
         
        label .loc_13BB
        index =  (value*2 - 454)//2
        x = FindIP.final_1[index]
        index = value - 225
        y = FindIP.final_list[index]
        self.11DC(y, x)
        z = FindIP.DC_eax
        index = self.1211(FindIP.list9_49, FindIP.list11_49)
        x = FindIP.final_1[index]
        y = FindIP.final_list[index]
        self.11DC(y, x)
        x = j
        x = x - FindIP.DC_eax
        goto .loc_140E
         
        label .loc_140E
        y = 0
         
        
        end = j + z     #Buffer Check
        if FindIP.CC_BUF_LEN < end:
            temp = FindIP.CC_BUF_LEN
            temp = end - temp
            temp_list = [0]*temp
            FindIP.CC_IP.extend(temp_list)
         
        while y < z:
            a = uint8(FindIP.CC_IP[x+y])
            FindIP.CC_IP[j+y] = a
            y = y + 1
        label .loc_1419
        j = j + z
         
        label .loc_141C
        value = self.1211(FindIP.list6_49, FindIP.list8_49)
        if value != i:
            goto .loc_13AE
        goto .end
         
        label .end
        return
                
    def 1125(self,counter,list3,list4,list5):
        i = 0
         
        while i < counter:
            j = FindIP.list2_49[i]
            list3[j] = list3[j] + 1
            i = i + 1
        list3[0] = 0
         
                 
        k = 0x10
        j = 0
        temp = 0
         
        if counter < k:
            diff = k - counter
            for i in range(0,diff):
                list3.append(0)
                list5.append(0)
                 
        while k > 0:
            list4[j] = temp
            temp = temp + list3[j]
            j = j + 1
            k = k - 1
             
        l = 0
        while l < counter:
            if FindIP.list2_49[l] != 0:
                temp = FindIP.list2_49[l]
                temp = list4[temp]
                list5[temp] = l
                temp = FindIP.list2_49[l]
                list4[temp] = list4[temp] + 1
            l = l + 1
     
    def 1211(self,list3,list5):
        i = 0
        temp = 0
        esi = 0
        while True:
            i = i + 1
            ebx = list3[i]
            temp = temp + ebx
            self.11AF()
            esi = esi + esi
            esi = esi - ebx
            esi = esi + FindIP.AF_eax
            if (esi < 0):
                break
        esi = esi + temp
        eax = list5[esi]
        return eax
     
    @with_goto
    def C7E0(self,arg8,arg4,list2_49,ecx):
        edx = arg8
        edi = ecx
         
        if edx != 0:
            al = uint8(arg4)
            if al != 0:
                goto .loc_C80C
            else:
                if edx < 0x80:
                    goto .loc_C80C  
            label .loc_C80C
            if edx < 4:
                goto .loc_C845
            ecx = ecx & 3
            if ecx == 0:
                goto .loc_C827
            edx = edx - ecx
            label .loc_C81D
            while ecx > 0:
                list2_49[edi] = al
                edi = edi + 1
                ecx = ecx - 1
            label .loc_C827
            eax = uint32(al)
            ecx = eax
            eax = uint32(eax << 8) + ecx
            ecx = uint32(eax << 0x10)
            eax = eax + ecx
            ecx = edx
            edx = edx & 3
            ecx = ecx >> 2
            if ecx == 0:
                goto .loc_C845
            while ecx > 0:
                list2_49[edi:edi+4] = al,al,al,al
                edi = edi + 4
                ecx = ecx - 1
            tmp = edx
            tmp = tmp & tmp
            if tmp == 0:
                goto .end
            label .loc_C845
            while edx > 0:
                list2_49[edi] = al
                edi = edi + 1
                edx = edx - 1
        else:
            goto .end
        label .end
        return
             
if __name__ == '__main__':
    f = FindIP()
    f.readData()   
    f.105B()
    f.11AF()
    f.11DC(2, 0)
    f.1249()
    f.138D()
    for i in range(0,len(FindIP.CC_IP)):
        value = chr(FindIP.CC_IP[i])
        print(value,end='')
