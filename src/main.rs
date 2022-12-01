use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::thread::current;
use std::vec;

fn main() {
    day1();
}

fn day1() {

    if let Ok(lines) = read_lines("./day1.input")
    {
        // results
        let mut calories_per_elf = Vec::<i32>::new();

        let mut current_sum: i32 = 0;
        let mut line_count: i32 = 0;
        let mut most_calories: i32 = 0;

        for line in lines
        {
            if let Ok(lstr) = line {
                if let Ok(calorie) = lstr.parse::<i32>(){
                    current_sum += calorie;
                    println!("+ {} currentSum = {}", calorie, current_sum);
                }
                else {
                    calories_per_elf.push(current_sum);
                    if current_sum > most_calories {
                        most_calories = current_sum;
                    }
                    current_sum = 0;
                    println!("LINE BREAK!");
                }
            }
            line_count += 1;
        }
        calories_per_elf.push(current_sum);
        if current_sum > most_calories {
            most_calories = current_sum;
        }
        current_sum = 0;

        calories_per_elf.sort();
        calories_per_elf.reverse();

        for elf_calories in &calories_per_elf
        {
            println!("calorie: {}", elf_calories);
        }
        println!("lines total: {} elves_total: {} most calories: {}", line_count, calories_per_elf.len(), most_calories);
        println!("sum of top 3: {}", calories_per_elf[0] + calories_per_elf[1] + calories_per_elf[2]);
    }

    println!("Hello, world!");
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}