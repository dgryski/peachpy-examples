#include <stdio.h>
#include <stdint.h>

#include "add.h"

int main() {
    uint64_t t[]={100, 200, 1000, 50000};
    printf("sum=%ld\n", add(&t, 4, 4));
}
