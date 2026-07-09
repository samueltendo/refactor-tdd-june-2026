from unittest.mock import MagicMock

class EmailService:
    def send(self, to, subject, body):
        raise NotImplementedError("Real email send — don't use in tests")

def place_order(user_email, item, email_service):
    if user_email is None:
        return False
    email_service.send(user_email, f"Order confirmed: {item}", "Thanks for your order!")
    return True


def test_sends_confirmation_email_on_order():
    mock_email_service = MagicMock()  # MOCK — replaces real behavior entirely

    place_order('alice@test.com', 'Book', mock_email_service)

    mock_email_service.send.assert_called_once_with(
        'alice@test.com',
        'Order confirmed: Book',
        'Thanks for your order!',
    )


def test_does_not_email_on_failed_order():
    mock_email_service = MagicMock()

    place_order(None, 'Book', mock_email_service)

    mock_email_service.send.assert_not_called()
