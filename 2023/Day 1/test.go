package main

import (
	"fmt"
	"strings"
)

// "strings"

func main() {

	numMap := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}

	strSlice := []string{
		"two1nine",
		"eightwothree",
		"abcone2threexyz",
		"xtwone3four",
		"4nineeightseven2",
		"zoneight234",
		"7pqrstsixteen",
	}

	numberSlice := []int{}

	// for key, value := range numMap {
	// 	if strings.Contains(str, key) {
	// 		fmt.Println(value)
	// 	}
	// }

	for key, value := range numMap {
		firstDigit, lastDigit := -1, -1
		for _, str := range strSlice {
			if strings.Contains(str, key) {
				if firstDigit == -1 {
					firstDigit = value
				}
				lastDigit = value
			}
		}

		if firstDigit != -1 && lastDigit != -1 {
			numberSlice = append(numberSlice, ((firstDigit * 10) + lastDigit))
		}
	}

	fmt.Println(numberSlice)

	//given substring
	// substr := "educative"

	//check if str contains substr
	// isContains := strings.Contains(str, substr)

	//print the result
	// fmt.Println(isContains)
}
