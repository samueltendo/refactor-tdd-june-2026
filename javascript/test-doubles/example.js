class EmailService {
  send(to, subject, body) {
    console.log(`Sending '${subject}' to ${to}`);
  }
}

class OrderProcessor {
  constructor(emailService) {
    this.emailService = emailService;
  }

  calculateTotal(items) {
    // Note: this method never touches emailService at all
    return items.reduce((sum, item) => sum + item.price * item.qty, 0);
  }
}

test('calculateTotal sums correctly', () => {
  const dummyEmailService = null; // DUMMY — required by constructor, never used

  const processor = new OrderProcessor(dummyEmailService);
  const items = [
    { price: 10, qty: 2 },
    { price: 5, qty: 3 },
  ];

  const total = processor.calculateTotal(items);

  expect(total).toBe(35);
});

// Stub example
class WeatherApi {
  getTemperature(city) {
    // In real life: makes an HTTP call
    throw new Error("Real API call — don't use in tests");
  }
}

function getAlert(city, weatherApi) {
  const temp = weatherApi.getTemperature(city);
  if (temp > 35) return 'HIGH';
  if (temp < 10) return 'LOW';
  return 'NORMAL';
}

test('returns HIGH alert above 35', () => {
  const stubWeatherApi = { getTemperature: jest.fn().mockReturnValue(38) }; // STUB

  const alert = getAlert('London', stubWeatherApi);

  expect(alert).toBe('HIGH');
});

test('returns LOW alert below 10', () => {
  const stubWeatherApi = { getTemperature: jest.fn().mockReturnValue(7) };

  const alert = getAlert('London', stubWeatherApi);

  expect(alert).toBe('LOW');
});
