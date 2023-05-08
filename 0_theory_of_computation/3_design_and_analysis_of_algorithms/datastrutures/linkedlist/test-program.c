#include "linkedlist.h"
#include <stdio.h>
#include <assert.h>


int main()
{
    printf("Test creating Integer linkedlist\n");
    linkedlist numbers = new (INT);
    assert(numbers.head == NULL);
    assert(numbers.length == 0);
    assert(numbers.type == INT);

    printf("Test adding an item to the linked list\n");
    int n1 = 2;
    add(&numbers, &n1);
    assert(numbers.length == 1);
    assert(*(int *)(numbers.head->value) == 2);
    return 0;
}