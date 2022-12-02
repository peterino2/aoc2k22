#include <stdio.h>
#include <stdlib.h>

#define CHKERR(X) do{if((X)){printf("%s: error\n",#X);return -1;}}while(0)
#define CHKALLOC(X) do{if((X)==(void*)-1){printf("%s: error\n",#X); return -1;}}while(0)
#define p(X)printf("part"#X"=%d\n",s);
#define I int
#define C char
I main(I c,C**v)
{
    FILE* f=fopen("day2.input","r");C* b=NULL;
    size_t z;CHKERR(fseek(f,0,SEEK_END));z = ftell(f)+1;I s=0;
    CHKALLOC(b=malloc(z));fseek(f,0,SEEK_SET),fread(b,1,z,f);
    for(I i;i<z;i+=4){I o=b[i]-'A';I m=b[i+2]-'X';
    s+=m+1;if(((o+1)%3)==m)s+=6;else if(o==m)s+=3;}
    p(1)s = 0; for(I i;i<z;i+=4){I o=b[i]-65;
    I r=b[i+2]-88;I d=o+1+3;if(r==0)d=(o>0?o-1:2)+1;
    else if(r==2)d=((o+1)%3)+6+1;s+=d;}p(2)free(b);
    fclose(f);
}
