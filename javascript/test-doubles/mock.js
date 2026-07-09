class EmailService {
  send(to, subject, body) {
    throw new Error("Real email send — don't use in tests");
  }
}

function placeOrder(userEmail, item, emailService) {
  if (userEmail === null) return false;
  emailService.send(userEmail, `Order confirmed: ${item}`, 'Thanks for your order!');
  return true;
}

test('sends confirmation email on order', () => {
  const mockEmailService = { send: jest.fn() }; // MOCK — replaces real behavior entirely

  placeOrder('alice@test.com', 'Book', mockEmailService);

  expect(mockEmailService.send).toHaveBeenCalledWith(
    'alice@test.com',
    'Order confirmed: Book',
    'Thanks for your order!'
  );
});

test('does not email on failed order', () => {
  const mockEmailService = { send: jest.fn() };

  placeOrder(null, 'Book', mockEmailService);

  expect(mockEmailService.send).not.toHaveBeenCalled();
});
