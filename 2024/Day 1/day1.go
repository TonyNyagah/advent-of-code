package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// Input represents a pair of numbers from the input
type Input struct {
	left, right int
}

// parseInput reads and parses the input file
func parseInput(filename string) ([]Input, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, fmt.Errorf("opening file: %w", err)
	}
	defer file.Close()

	var inputs []Input
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		parts := strings.Fields(scanner.Text())
		if len(parts) != 2 {
			continue
		}

		left, errLeft := strconv.Atoi(parts[0])
		right, errRight := strconv.Atoi(parts[1])

		if errLeft != nil || errRight != nil {
			return nil, fmt.Errorf("converting numbers: %v %v", errLeft, errRight)
		}

		inputs = append(inputs, Input{left: left, right: right})
	}

	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("scanning file: %w", err)
	}

	return inputs, nil
}

// Part1 calculates the total distance between sorted lists
func Part1(inputs []Input) int {
	var left, right []int
	for _, input := range inputs {
		left = append(left, input.left)
		right = append(right, input.right)
	}

	sort.Ints(left)
	sort.Ints(right)

	total := 0
	for i := range left {
		total += abs(left[i] - right[i])
	}

	return total
}

// Part2 calculates the similarity score
func Part2(inputs []Input) int {
	rightFreq := make(map[int]int)
	var left []int

	for _, input := range inputs {
		rightFreq[input.right]++
		left = append(left, input.left)
	}

	total := 0
	for _, num := range left {
		total += num * rightFreq[num]
	}

	return total
}

// abs returns the absolute value of an integer
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	inputs, err := parseInput("day1_input.txt")
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}

	fmt.Println(Part1(inputs))
	fmt.Println(Part2(inputs))
}
