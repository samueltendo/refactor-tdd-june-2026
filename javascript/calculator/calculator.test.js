const add = require('./calculator')

test('the sum of 5 and 6 ', () => {
    expect(add(5, 6)).toBe(11)
});

test('the sum of 11 and 20 ', () => {
    expect(add(11, 20)).toBe(31)
});
