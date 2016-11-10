package main

import "fmt"

func main() {
	var s = []uint64{100, 200, 1000, 50000}

	sum := add(s)

	fmt.Printf("sum = %+v\n", sum)
}
