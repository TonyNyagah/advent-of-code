package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"unicode"
)

func PartOne(fileName string) {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	sum := 0

	for scanner.Scan() {
		line := scanner.Text()
		// fmt.Println(line)
		firstDigit, lastDigit := "", ""
		for _, r := range line {
			if unicode.IsDigit(r) {
				if firstDigit == "" {
					firstDigit = string(r)
				}
				lastDigit = string(r)
				// fmt.Println(firstDigit, lastDigit)
			}
		}
		if firstDigit != "" && lastDigit != "" {
			calibrationValue, _ := strconv.Atoi(firstDigit + lastDigit)
			sum += calibrationValue
		}
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("The sum of all calibration values is:", sum)
}

func PartTwo(fileName string) {
	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
}

func PartTwoPractice(fileName string) {
	// look for the word two and nine in the string I give you

}

func main() {
	PartOne("aoc_day1_input.txt")
}
