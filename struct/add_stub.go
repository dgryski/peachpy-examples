// +build amd64

package main

//go:generate python -m peachpy.x86_64 add.py -S -o add_amd64.s -mabi=goasm
//go:noescape
func add(f *foo) uint64
