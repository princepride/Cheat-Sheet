package main

import (
	"fmt"
)

func test() {
	defer fmt.Println("world")
	fmt.Println("ddddd")
}
func main() {
	test()
	fmt.Println("hello")
	fmt.Println("hello")
	fmt.Println("hello")
	fmt.Println("hello")
	fmt.Println("hello")
	fmt.Println("hello")
}
