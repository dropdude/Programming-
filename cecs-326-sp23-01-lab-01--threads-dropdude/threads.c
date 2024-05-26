/*
1.
We call a 2nd thread and give it the argument of child to run.
Child sleeps for 3 seconds then gives a brief message.
If a 2nd thread cannot be create post a error message.
I run a infinite loop waiting for the user to press the enter key.
When the enter key is pressed we cancel the 2nd thread.
It takes a couple of seconds for the thread to cancel.
We wait 5 seconds for the program to complete
exit.

2.When we create a second thread.It can work in parallel or independently from the main thread.This is usefully in many applications but does not guarentee in which order the will execute.
*/

#include <pthread.h>
#include <unistd.h>
#include <stdio.h>
// function for what the child process does.
static void *child(void *ignored){
    while (1) {
        sleep(3);
        printf("Child is done sleeping 3 seconds.\n");
    }
    return NULL;
}

int main(int argc, char *argv[]){
   pthread_t child_thread;
   int code;
   code = pthread_create(&child_thread, NULL, child, NULL); // creates new thread and assigns it child function
   while (1) {
       printf("Waiting til Enter key is pressed!\n"); //infinite loop till enter is pressed
       if (getchar() == '\n')
       {
           printf("Enter key was pressed\n"); // when enter is pressed cancel code
           pthread_cancel(code);
           printf("Second thread has been canceled.\n");
           break;
       }
   }
   sleep(5); 
   printf("Parent is done sleeping 5 seconds.\n");
   return 0;
}
