#include <stdio.h>
int main()
{
   int num;
   FILE *fptr;
//Opening the file and checking to see if it is not empty
   if ((fptr = fopen("test_subprocess","r")) != NULL){
       printf("You opened the file!");

   }
//Closing the file
   fclose(fptr);

//I don't know if I need this return statement, I just left it there when copying from an example
   return 0;
}
