package aoc

import (
	"fmt"
	"os"
	"strings"
)

func FileOpenLines(filename string) ([]string, error) {
	// Read the file
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return nil, err
	}

	// Split the content into lines
	lines := strings.Split(string(content), "\n")
	return lines, nil
}

func ExtractDigits(s string) []int {
	// Extract the digits from a string
	var digits []int
	for _, c := range s {
		if c >= '0' && c <= '9' {
			digits = append(digits, int(c-'0'))
		}
	}
	return digits
}
