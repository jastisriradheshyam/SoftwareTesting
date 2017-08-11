#include<stdio.h>
#include<stdlib.h>
int main(int arg,char *args[])
{
int a,b,c;
float d;
a=atoi(args[1]);
b=atoi(args[2]);
c=atoi(args[3]);
printf("%d %d %d ", a,b,c);
d = b*2 - 4*a*c;
if(d==0)
{
printf("Equal");
}
if(d<0)
{
printf("Imaginary");
}
if(d>0)
{
printf("Real");
}
return 0;
}
