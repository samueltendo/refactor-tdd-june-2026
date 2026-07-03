const fizzBuzz = require('./fizzbuzz')

test('returns number as a string', () => {
    expect(fizzBuzz(1)).toBe("1");
})
test('returns Fizz for multiples of 3', () => {
    expect(fizzBuzz(3)).toBe("Fizz");
});

test('returns Buzz for multiples of 5', () => {
    expect(fizzBuzz(5)).toBe("Buzz");
});

test('returns FizzBuzz for multiples of 15', () => {
    expect(fizzBuzz(15)).toBe("FizzBuzz");
});

test('returns Fizz for another multiple of 3', () => {
    expect(fizzBuzz(9)).toBe("Fizz");
});

test('returns Buzz for another multiple of 5', () => {
    expect(fizzBuzz(10)).toBe("Buzz");
});

test('throws TypeError for float input', () => {
    expect(() => fizzBuzz(1.5)).toThrow(TypeError);
});
