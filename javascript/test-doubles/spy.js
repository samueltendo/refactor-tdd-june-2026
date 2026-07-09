const logger = {
  warn(message) {
    console.log(`[WARN] ${message}`);
  },
};

function processInput(input) {
  if (input === null) {
    logger.warn('Invalid input received');
    return;
  }
  return input.toUpperCase();
}

test('logs a warning for bad input', () => {
  const spy = jest.spyOn(logger, 'warn'); // SPY — real warn() still runs

  processInput(null);

  expect(spy).toHaveBeenCalledTimes(1);
  expect(spy).toHaveBeenCalledWith('Invalid input received');

  spy.mockRestore(); // always restore — otherwise the spy leaks into other tests
});

test('does not log a warning for valid input', () => {
  const spy = jest.spyOn(logger, 'warn');

  const result = processInput('hello');

  expect(result).toBe('HELLO');
  expect(spy).not.toHaveBeenCalled();

  spy.mockRestore();
});
