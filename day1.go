package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/phantom903/AoC2023/internal/aoc"
)

func part1(lines []string) int {
	acc := 0
	for _, line := range lines {
		digs := aoc.ExtractDigits(line)
		if len(digs) == 0 {
			continue
		}
		blob := fmt.Sprintf("%d%d", digs[0], digs[len(digs)-1])
		val, err := strconv.Atoi(blob)
		if err != nil {
			panic(fmt.Sprintf("Error converting string to int: %v", err))
		}
		acc += val
	}
	return acc
}

func part2(lines []string) int {
	acc := 0
	for _, line := range lines {
		replacer := strings.NewReplacer("one", "o1e", "two", "t2o", "three", "t3e", "four", "f4r", "five", "f5e", "six", "s6x", "seven", "s7n", "eight", "e8t", "nine", "n9e")
		line = replacer.Replace(line)
		digs := aoc.ExtractDigits(line)
		blob := fmt.Sprintf("%d%d", digs[0], digs[len(digs)-1])
		val, err := strconv.Atoi(blob)
		if err != nil {
			panic(fmt.Sprintf("Error converting string to int: %v", err))
		}
		acc += val
	}
	return acc
}

func main() {
	lines, err := aoc.FileOpenLines("input/day1.txt")

	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println("Part 1:", part1(lines))
	fmt.Println("Part 2:", part2(lines))
}
