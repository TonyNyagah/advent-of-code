package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
	// "strings"
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

func Calibration(dataSlice []string) int {
	sum := 0
	re := regexp.MustCompile("[0-9]+")
	digitSlice := []int{}

	for _, word := range dataSlice {
		result := re.FindAllString(word, -1)
		merged := strings.Join(result, "")
		split := strings.Split(merged, "")
		digit, _ := strconv.Atoi(split[0] + split[len(split)-1])
		digitSlice = append(digitSlice, digit)
	}

	for _, number := range digitSlice {
		sum += number
	}

	return sum
}

func main() {
	dataSlice := ScanText("aoc_day1_input.txt")
	replacements := map[string]string{
		"one":   "one1one",
		"two":   "two2two",
		"three": "three3three",
		"four":  "four4four",
		"five":  "five5five",
		"six":   "six6six",
		"seven": "seven7seven",
		"eight": "eight8eight",
		"nine":  "nine9nine",
	}

	fmt.Println("Part 1: ", Calibration(dataSlice))

	for i, _ := range dataSlice {
		for old, new := range replacements {
			dataSlice[i] = strings.ReplaceAll(dataSlice[i], old, new)
		}
	}

	fmt.Println("Part 2: ", Calibration(dataSlice))
}
