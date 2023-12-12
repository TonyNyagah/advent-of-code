package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"

	// "strings"
	"unicode"
)

func ScanText(fileName string) []string {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	wordSlice := []string{}

	for scanner.Scan() {
		line := scanner.Text()
		wordSlice = append(wordSlice, line)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return wordSlice
}

func PartOne(fileName string) {
	wordSlice := ScanText(fileName)
	sum := 0

	for _, word := range wordSlice {
		firstDigit, lastDigit := "", ""
		for _, r := range word {
			if unicode.IsDigit(r) {
				if firstDigit == "" {
					firstDigit = string(r)
				}
				lastDigit = string(r)
			}
		}
		if firstDigit != "" && lastDigit != "" {
			calibrationValue, _ := strconv.Atoi(firstDigit + lastDigit)
			sum += calibrationValue
		}
	}

	fmt.Println("The sum of all calibration values is:", sum)
}

func PartTwo(fileName string) {
	wordSlice := ScanText(fileName)
	// sum := 0

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

	for key, value := range numMap {
		for _, word := range wordSlice {
			if strings.Contains(word, key) {
				fmt.Println(value)
				if firstDigit == "" {
					firstDigit = string(r)
				}
			}
		}
		fmt.Println("========================")
	}
}

// func PartTwoPractice(fileName string) {
// 	// look for the word two and nine in the string I give you
// 	//given string
// 	str := "hellofromeducative"

// 	//given substring
// 	substr := "educative"

// 	//check if str contains substr
// 	isContains := strings.Contains(str, substr)

// 	//print the result
// 	fmt.Println(isContains)
// }

func main() {
	PartOne("aoc_day1_input.txt")
	PartTwo("aoc_day1_test.txt")
}
