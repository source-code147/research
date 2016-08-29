#include <windows.h>
#include <stdio.h>
#include <WinSock.h>


//

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
//

typedef unsigned __int8  int8;

DWORD* Space();
DWORD* Space_1(char Byte);
void Free_Byte(void *data);

int a = 0;
int b;
size_t x;
u_long y;

int First_Stage (DWORD Size, BYTE * byBuff)
{
	BYTE tmp=0;
	int i;
	int count = 0;

	for(i=0; i<Size; i++)
	{
		if (count <= Size)
		{
			tmp = byBuff[i] ^ (0xc7 ^ 0xe7 ^ 0xb7);
			byBuff[i] = tmp;
			count++;
		}else
			return -1;	
	}
	return 0;
}

void  *Create_Table(BYTE * byBuff, DWORD Size, size_t * x, u_long *y)
{
	
	DWORD size_1; 
	DWORD *addr16;
	DWORD *addr10;
    DWORD *addr11;
    DWORD *addr12;
	DWORD *addr13; 

	u_long *var; 
	u_long  netlong;
    
	int Byte;
	int var14;
	int8 var20;
	unsigned int var8; 
	unsigned int var19;
	size_t *addr5;

	void *addr7;
	void *result;
	void *addr15;
	void *addr_space;

	size_t addr9;
	
	var = y;
	addr5 = x;
	size_1 = Size; //c4f2
	addr_space = Space(); //malloc

	if (Read_Byte(Size,byBuff,addr5, 4,&netlong)) 
	{
		Free_Byte(addr_space);
		
	}
	else
	{
		netlong = ntohl(netlong); // counter for inner loop 1000 ntohl 100
		 if (Read_Byte(size_1, byBuff, addr5, 4, var))
		 {
			 Free_Byte(addr_space); //freeup
		 }
		 else
		 {
			 *var = ntohl(*var); //counter for outer loop f20000 ntohl f200
			 while (1)
			 {
				 if ( !netlong )
				 {
					 return (addr_space);
				 }
				 addr7 = addr_space;
				 --netlong;
				 addr16 = (DWORD *)addr_space;
				 if (Read_Byte(size_1, byBuff, addr5, 1, &var14) || Read_Byte(size_1, byBuff, addr5, 1, &var20))
				 {
					 Free_Byte(addr_space); //freeup
					 goto Finish;
				 }
				 var8 = var20; //copied middle byte
				 addr9 = (int8)((var20 >> 3) + ((var20 & 7) != 0));
				 addr15 = malloc(addr9);
				 if (Read_Byte(size_1, byBuff, addr5, addr9, addr15) )
				 {
					break;
				 }
				 var19 = 0;
				 if (var8)
				 {
					 do 
					 {
						  addr10 = addr16;
						  if ( (*((BYTE *)addr15 + (var19 >> 3)) >> (var19 & 7)) & 1 )
						  {
								if ( !addr16[4] )
								{
									if ( var19 == (int8)(var20 - 1) )
									{
										addr11 = Space_1(var14);
									}
									else
									{
										addr11 = Space();
									}
									addr10[4] = (DWORD)addr11; //Swap Addresses
									addr11[2] = (DWORD)addr10;
								 }
								addr12 = (DWORD *)addr10[4];
						   }
						  else
						  {
								if ( !addr16[3] )
								{
									if ( var19 == (int8)(var20 - 1) )
									{	
										addr13 = Space_1(var14);
									}
									else
									{
										addr13 = Space();
									}
									addr10[3] = (DWORD)addr13; // check value
									addr13[2] = (DWORD)addr10;
								}
								addr12 = (DWORD *)addr10[3];
						  }
						  ++var19;
						  addr16 = addr12;
					 }
					 while (var19 < var8);
				 }
				 free(addr15);
			 }
			 free(addr15);
			 Free_Byte(addr_space); // freeup
		 }
Finish:
		result = 0;
	}
		return result;
}


DWORD *Space()
{
	DWORD *space;
	int mem = 20;
	int i;
	space = (DWORD *) malloc(mem); //allocated 20 byte and add 0 to 0,4,8,12 location
	*(BYTE *)space = 0;
	for (i=1; i<=4;i++)
	{
	space[i] = 0;
	}

	return space;

}

DWORD *Space_1(char Byte)
{
	DWORD *space;
	int mem = 20;

	space = (DWORD *) malloc(mem); //allocated 20 byte and Store data here 
	space[1] = 0;
	space[2] = 0;
	*(BYTE *)space = 1;
	*((BYTE *)space + 12) = Byte;
	return space;
}


int Read_Byte(DWORD Size, BYTE * byBuff,size_t *a,int b,void *c)
{
	size_t new_var;
	int result;
	size_t counter;

	new_var = *a;

	if ( Size >= *a )
	{
		counter = new_var + b;
		if ( counter < Size )
		{
			memcpy(c,(const void *)(byBuff+new_var),b); //Copied 1st b bytes so on.
			*a = counter;
			return 0;
		}
		else
		{
		result = 1;
		}
	} else { result = 1;}
  
	return result;
}

void Free_Byte(void *data)
{
	if ( data )
	{
		if ( !*(BYTE *)data )
		{
			Free_Byte(*((void **)data + 3));
			Free_Byte(*((void **)data + 4));
		}
	free(data);
	}
}

signed int Decryption(BYTE * byBuff, DWORD Size, size_t *x, u_long *y){

	void * table_addr;
	size_t addr13;
	size_t addr11;
	
	int var4;
	int result;
	unsigned int var6;
	int8 var9;
	int8 var14;

	BYTE * addr5;
	BYTE * addr7;

	DWORD *addr8; 

	var4 = 0;
	addr11 = 0;

	if (x && y && (table_addr = Create_Table(byBuff,Size,&addr11,(u_long *)&addr13)) != 0 ) // Create Table using doubly link list
	{
	    addr5 = (BYTE *)malloc(addr13); // memory allocated for decrypted data f200
		var6 = addr11; // Size of Header 3BE
		addr7 = addr5;  // Address of newly allocated memory
		addr8 = (DWORD *)table_addr; // Address of Table 

		while ( var6 < Size && addr13 )
		{
			var9 = *(BYTE *)(var6 + byBuff);
			var14 = 1;
			do
			{
				if ( !var14 )
				{
					break;
				}
				addr8 = (DWORD *)(var9 & var14 ? addr8[4] : addr8[3]);
				var14 *= 2;
				if ( *(BYTE *)addr8 )
				{
					addr7[var4] = *((BYTE *)addr8 + 12);        // data goes Here
					addr8 = (DWORD *)table_addr; // start from the start ;)
					++var4;
					--addr13;  // lets do this f200 - 1
				}
			} //do ends here dnt get confused .
			while ( addr13 );
			{
				++var6;
			}
		}
		Free_Byte(table_addr);
		*x = (size_t) addr7;
		*y = var4;
		result = 0;
	}
	else
	{
		result = 1;
	}
	printf("The address of decrypted data in memory :%x",addr5);
	return result;
}

int main(void) 
{
	LPCSTR fname = "C:\\raw_1";
	DWORD Size;
	DWORD byteread;
	BYTE * byBuff; 
	
	//LPDWORD NumberofBytes = &byteread; 

	HANDLE hFile = CreateFileA(fname,                // name of the write
						GENERIC_READ| GENERIC_WRITE,          // open for writing
						   1,                      // do not share
						   NULL,                   // default security
						   OPEN_EXISTING,             // create new file only
						   FILE_ATTRIBUTE_READONLY,  // normal file
						   NULL);                  // no attr. template

	if (hFile == INVALID_HANDLE_VALUE)
	{
		printf("Could not open %s file, error %d\n", fname, GetLastError()); 
		return 0;
	}
	else
		printf("File's HANDLE is OK!: %d:\n",hFile);

	Size = GetFileSize(hFile,NULL);
	printf("Size:%d\n",Size);
	
	byBuff = (BYTE *)VirtualAlloc(NULL,Size,0x3000,0x40);
	if(!ReadFile(hFile,byBuff,Size,&byteread,NULL))
		return 0;

	First_Stage(Size,byBuff); //decryption first stage Xor with 0x97
	Decryption(byBuff,Size,&x,&y); // unpacking logic
 
	//If you are allocating a memory then you should free it 
	VirtualFree(byBuff, Size, 0);
	CloseHandle(hFile);

return 0;

}