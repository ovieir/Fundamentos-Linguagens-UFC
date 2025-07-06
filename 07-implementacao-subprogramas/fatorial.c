#include <stdio.h>
#include <stdlib.h>

int fatorial(int n){
   if(n == 0 || n == 1){
    return 1;
    }
   else{
    return n * fatorial(n -1);
   } 

}

int main() {
   int numero = 4;
   
   printf("Fatorial de %d = %d\n", numero, fatorial(numero));

   return 0;
}