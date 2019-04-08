/*
 * Name: *Kyle Liu*
 * Section: *0101*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *Kyle Liu*
 */

/* your code goes here */
#include <stdio.h>

int main () {
    int a = 0x1ceb00da;
    int b = 0xfeedface;

    printf("a = %d\n", b);

    printf("b = %d\n", a);

    /*XOR a & b*/
    b = a^b;
    a = a^b;
    b = a^b;

    printf("a = %d\n", b);

    printf("b = %d\n", a);

    return(0);
}
