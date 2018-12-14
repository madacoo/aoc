# Can AOC's Day 5 problem be solved in a functional style?

For day 5 in Advent of Code 2017, we are asked to help a CPU escape a maze of jump instructions. We are given a message listing all the jump instructions offsets and the goal is to follow those jumps until one of the jumps leads outside the list.

We must also mutate the offsets as we go. In part A, we simply increment each jump after using its value to change position. In part A we either increment, or decrement if the offset is greater than or equal to 2.

To solve the puzzle we must count the number of steps it takes to escape from the maze.

The puzzle input can be conceived of most naturally as an array.

    [0, 3, 0, 1 -3]

In this example, as given, it takes 5 steps to exit.

Here are my initial solutions to part A and B.

## Part A

    def solve(instructions):
        index = steps = 0
        length = len(instructions)
        while (0 <= index < length):
            offset = instructions[index]
            instructions[index] += 1
            index += offset
            steps += 1
        return steps

## Part B

    def solve2(instructions):
        index = steps = 0
        length = len(instructions)
        while (0 <= index < length):
            offset = instructions[index]
            increment = 1
            if offset >= 3:
                increment = -1
            instructions[index] += increment
            index += offset
            steps += 1
        return steps


These solutions are probably fairly typical of how most people would approach them. There's nothing particularly wrong with them. They find the correct solutions. Although in Python, part B does take a few seconds to complete. But if we wanted to do this efficiently, we should use a language other than Python.

There are a couple of things that bother me about these solutions, however.

- solve2 is basically identical to solve except it has one extra variable, 'increment' and it checks the value of 'offset' with an if statement. So we have lots of repeated code. Yuck.
- in both functions, we have iteration, mutation and counting all going on all at once and this makes the code very loud and ugly to look at.


rewriting in a functional style made the code more readable and more reusable since I could pass a mutation\_rule to the solve function

But it made it slower because I'm making more function calls, which are inherently expensive in Python. This could be mitigated to some extent by replacing the jump function with something like:

    instructions[i], i = mutate_rule(instructions[i]), i + instructions[i]

But then we lose some of the readability advantages. And we still have more function calls so it will still be slower.

Probably we should step away from Python altogether if we want to do this in a properly functional way.
