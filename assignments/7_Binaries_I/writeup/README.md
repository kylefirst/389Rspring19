# Writeup 7 - Binaries I

Name: *Kyle Liu*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Kyle Liu*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
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
```

### Part 2 (10 Pts)

This program swaps the values contained in two integer variables and prints their values before and after the swap.
