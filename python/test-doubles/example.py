# Example of a dummy

class EmailService:
    def send(self, to, subject, body):
        print(f"Sending '{subject}' to {to}")

class OrderProcessor:
    def __init__(self, email_service):
        self.email_service = email_service

    def calculate_total(self, items):
        # Note: this method never touches email_service at all
        return sum(item['price'] * item['qty'] for item in items)


def test_calculate_total_sums_correctly():
    dummy_email_service = None  # DUMMY — required by constructor, never used

    processor = OrderProcessor(email_service=dummy_email_service)
    items = [{'price': 10, 'qty': 2}, {'price': 5, 'qty': 3}]

    total = processor.calculate_total(items)

    assert total == 35

# Example of a Stub

from unittest.mock import MagicMock
class WeatherApi:
    def get_temperature(self, city):
        # In real life: makes an HTTP call
        raise NotImplementedError("Real API call — don't use in tests")

def get_alert(city, weather_api):
    temp = weather_api.get_temperature(city)
    if temp > 35:
        return 'HIGH'
    elif temp < 10:
        return 'LOW'
    return 'NORMAL'


def test_high_alert_above_35():
    stub_weather_api = MagicMock()
    stub_weather_api.get_temperature.return_value = 38  # STUB — canned answer

    alert = get_alert('London', stub_weather_api)

    assert alert == 'HIGH'


def test_low_alert_below_10():
    stub_weather_api = MagicMock()
    stub_weather_api.get_temperature.return_value = 7

    alert = get_alert('London', stub_weather_api)

    assert alert == 'LOW'
