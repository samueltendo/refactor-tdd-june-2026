function fizzBuzz(n) {
    if (typeof n !== 'number' || !Number.isInteger(n)) {
        throw new TypeError(`Expected an integer, got ${typeof n}`);
    }
    if (n % 3 === 0 && n % 5 === 0) return "FizzBuzz";
    if (n % 3 === 0) return "Fizz";
    if (n % 5 === 0) return "Buzz";
    return n.toString();
}

module.exports = fizzBuzz;
