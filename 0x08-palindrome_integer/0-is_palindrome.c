#include "palindrome.h"

/**
 * is_palindrome - check if integer is palindrome
 * @n: number to be checked
 * Return: 1 if n is a palindrome or 0 is not
 */

int is_palindrome(unsigned long n) {
    int pal;
    unsigned int reversed = 0, remainder, copyn;

    copyn = n;
    // reversed integer is stored in reversed variable
    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    // palindrome if orignal and reversed are equal
    if (copyn == reversed)
        pal = 1;
    else
        pal = 0;

    return (pal);
}
