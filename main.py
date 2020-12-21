import timeit

import day1.main as day1
import day2.main as day2
import day3.main as day3
import day4.main as day4
import day5.main as day5
import day6.main as day6
import day7.main as day7
import day8.main as day8
import day9.main as day9
import day10.main as day10
import day11.main as day11
import day12.main as day12
import day13.main as day13
import day14.main as day14
import day15.main as day15
import day16.main as day16
import day17.main as day17
import day18.main as day18
import day19.main as day19
import day20.main as day20
import day21.main as day21

if __name__ == '__main__':
    print("🎄 Advent of Code 2020 🎄")
    for i in range(1, 22):
        print("=== DAY {} ===".format(i))
        print("{} secs".format(
            timeit.timeit("day{}.solution()".format(i), setup="from __main__ import day{}".format(i), number=1)))
