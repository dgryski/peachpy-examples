#!/bin/sh
python -m peachpy.x86_64 ../add.py -emit-c-header add.h -mimage-format=elf -o add_amd64.o -mabi=sysv
gcc -g add.c add_amd64.o
