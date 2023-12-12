use std::collections::HashMap;

fn main() {
    let input = include_str!("aoc_day1_test.txt");
    println!("{}", part_1(input));
    println!("{}", part_2(input));
}


fn part_1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            let first = line.chars().find_map(|c| c.to_digit(10)).unwrap();
            let last = line.chars().rev().find_map(|c| c.to_digit(10)).unwrap();
            10 * first + last
        })
        .sum()
}

fn part_2(input: &str) -> u32 {
    let mut nums = HashMap::new();
    nums.insert("1", 1);
    nums.insert("2", 2);
    nums.insert("3", 3);
    nums.insert("4", 4);
    nums.insert("5", 5);
    nums.insert("6", 6);
    nums.insert("7", 7);
    nums.insert("8", 8);
    nums.insert("9", 9);
    nums.insert("one", 1);
    nums.insert("two", 2);
    nums.insert("three", 3);
    nums.insert("four", 4);
    nums.insert("five", 5);
    nums.insert("six", 6);
    nums.insert("seven", 7);
    nums.insert("eight", 8);
    nums.insert("nine", 9);

    let mut sum = 0;
    for line in input.lines() {
        let mut forwards = line;
        let mut backwards = line;

        let first = 'outer: loop {
            for (prefix, num) in nums.iter() {
                if forwards.starts_with(prefix) {
                    break 'outer num;
                }
            }
            forwards = &forwards[1..];
        };

        let last = 'outer: loop {
            for (suffix, num) in nums.iter() {
                if backwards.ends_with(suffix) {
                    break 'outer num;
                }
            }
            backwards = &backwards[..backwards.len() - 1];
        };

        let num = first * 10 + last;
        sum += num;
    }

    sum
}
