fs = require('fs');


let puzzle_input = () => {
    "Return puzzle input as an array of integers."
    let data = fs.readFileSync("input.txt", "ascii");
    return data.toString()
               .trim()
               .split("")
               .map(c => parseInt(c));
};


let matchNext = (el, i, arr) => {
    "Return true if element is equal to next element in array."
    // The array is considered circular so we must much last to first.
    let j = (i + 1) % arr.length;
    return (el == arr[j]);
};


let matchHalfway = (el, i, arr) => {
    "Return true if element is equal to element halfway along array."
    // The array is considered circular. 
    let j = (i + arr.length/2) % arr.length;
    return (el == arr[j]);
};


let sum = (arr) => {
    "Return the sum of an array of Numbers."
    let total = 0;
    for (let i in arr) total += arr[i];
    return total;
};


let solve = (arr) => {
    let total = 0;
    let j = 0;
    for (let i = 0; i < arr.length; i++) {
        j = (i + 1) % arr.length;
        if (arr[i] == arr[j]) total += arr[i];
    }
    return total;
};


let solve2 = (arr) => {
    let total = 0;
    let j = 0;
    for (let i = 0; i < arr.length; i++) {
        j = (i + arr.length/2) % arr.length;
        if (arr[i] == arr[j]) total += arr[i];
    }
    return total;
};


let input = puzzle_input();

// imperative solutions
console.time("imperative");
console.log(solve(input));
console.log(solve2(input));
console.timeEnd("imperative");

// functional solutions
console.time("functional");
console.log(sum(input.filter(matchNext)));
console.log(sum(input.filter(matchHalfway)));
console.timeEnd("functional");
