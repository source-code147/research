#include <stdio.h>
#include <windows.h>
#include <string.h>

#define INT_BITS 32
#define INT_MAX 0x7fffffff

typedef unsigned int uint;

//Shift Rotate Left

DWORD rol(int val, uint bits){

    while (bits--) {
        (val = (val << 1) | ((val >> (sizeof(int) * 8 - 1)) & 1));
    }
    return val;
}

//Shift Rotate Right

DWORD ror(int val, uint bits){

    while (bits--) {
        val = (((val >> 1) & (INT_MAX)) | ((val & 1) << (sizeof(int) * 8 - 1)));
    }
    return val;
}

int DGA(int year, int month, int day){

    char domain_str[60] = "ru000info0biz00clicksu000work0pl000org00pw000xyz00";
    char name_str[25] = "";
    char domain[5] = "";

    uint var4, var5, var6, var7, var8, var9, var10;
    uint var11, var12, var13, var14, var15, var16;

    uint seed_1, seed_2, seed_3;
    int seed = 7;

    uint const_1 = 0xB11924E1;
    uint const_2 = 0x27100001;

    uint i, j, k, tmp, char1;
    uint name_len, tmp_1, var17;

    uint shift_day = day;

    for (i = 0; i <= 12; i++) {
        int var3 = i;
        int var1 = 0x15CB;
        uint var2 = 0x0;

        tmp_1 = shift_day;
        tmp_1 = (tmp_1 >> 1);

        var3 = (rol(var3, 0x15));
        var4 = (rol(var1, 0x11));

        seed_1 = var3 + var4;
        seed_2 = tmp_1;
        seed_3 = year;

        for (i = 0; i < seed; i++) {
            tmp = (seed_3 + var2 + 0x1BF5);
            tmp = (const_1 * tmp);

            var5 = (ror(tmp, 7));
            tmp = (var5 + const_2);

            var6 = (tmp ^ var2);
            tmp = (var6 + var1);

            tmp = (const_1 * tmp);
            var7 = (ror(tmp, 7));

            tmp = (var7 + const_2);
            var8 = (tmp ^ var6);

            tmp = (tmp_1 + var8);
            tmp = (const_1 * tmp);

            var9 = (ror(tmp, 7));
            tmp = (0x0D8EFFFFF - var9);

            var10 = (tmp + var8);

            tmp = (month + var10 - 0x65CAD);
            tmp = (const_1 * tmp);

            var11 = (ror(tmp, 7));
            var12 = (var10 + var11 + const_2);

            tmp = (var12 + seed_1);
            tmp = (const_1 * tmp);

            var13 = (ror(tmp, 7));
            tmp = (var13 + const_2);

            var2 = (tmp ^ var12);
            seed_3 = (seed_3 + 1);

            tmp_1 = seed_2;
        } // end of for loop 2

        name_len = ((var2 % 0x0B) + 7);

        if (name_len != -7) {
            for (j = 0; j < name_len; j++) {
                var14 = (rol(var2, j));
                tmp = (const_1 * var14);

                var15 = (ror(tmp, 7));
                var2 = (var15 + const_2);

                char1 = (var2 % 0x19 + 0x61); // Domain char
                name_str[j] = (char)char1;
            }
            name_str[j] = ('.');
        }
        tmp = (const_1 * var2);
        var16 = (ror(tmp, 7));
        var16 = (var16 + const_2);

        var17 = (5 * (var16 % 0x0A));
        k = 0;
        for (i = var17; i < (var17 + 5); i++, j++) {
            domain[k] = domain_str[i];
            if (domain[k] != '0') {
                name_str[j + 1] = domain[k];
            }
        }
        printf("Generated Subdomains by Zepto : %s \n", name_str);
    } // end of for loop 1
}

int main(){

    int year, month, day;

    SYSTEMTIME st;
    GetSystemTime(&st);

    DGA(st.wYear, st.wMonth, st.wDay);
}