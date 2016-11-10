package main

import "fmt"

type foo struct {
	zot uint16
	bar uint16
	qux uint64
}

func main() {
	var f = foo{bar: 200, qux: 50000}
	sum := add(&f)
	fmt.Printf("sum = %+v\n", sum)
}
