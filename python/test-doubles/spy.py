from unittest.mock import patch
import logging

logger = logging.getLogger("app")

def warn(message):
    logger.warning(message)

def process_input(input_value):
    if input_value is None:
        warn('Invalid input received')
        return None
    return input_value.upper()


def test_logs_warning_for_bad_input():
    with patch('__main__.warn', wraps=warn) as spy:  # SPY — real warn() still runs
        process_input(None)

        spy.assert_called_once_with('Invalid input received')


def test_no_warning_for_valid_input():
    with patch('__main__.warn', wraps=warn) as spy:
        result = process_input('hello')

        assert result == 'HELLO'
        spy.assert_not_called()
