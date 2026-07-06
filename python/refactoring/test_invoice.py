from invoice import InvoiceProcessor

def test_regular_customer_default_state_small_order():
    items = [{"price": 10, "qty": 2}]  # subtotal = 20
    result = InvoiceProcessor().process(items, "regular", "TX")
    assert result == 26.99 # 20 -> +5% tax = 21.0 -> +5.99 shipping


def test_member_customer_ca_mid_order():
    items = [{"price": 20, "qty": 3}]  # subtotal = 60
    result = InvoiceProcessor().process(items, "member", "CA")
    assert result == 60.91  # 60 -> -10% = 54 -> +7.25% tax = 57.915 -> +2.99 shipping


def test_vip_customer_ny_large_order_no_shipping_fee():
    items = [{"price": 50, "qty": 3}]  # subtotal = 150
    result = InvoiceProcessor().process(items, "vip", "NY")
    assert result == 130.65
