#include "../memory_cell/memory_allocator.h"
#include "node.h"

node * newnode(void *value, node *next) {
    node *n = (node*)allocate_memory(sizeof(node));
    n->value = value;
    n->next = next;
    return n;
}
