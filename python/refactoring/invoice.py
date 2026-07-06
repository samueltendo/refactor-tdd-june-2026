# invoice.py
class InvoiceProcessor:
    # Discounts
    MEMBER_DISCOUNT = 0.10
    VIP_DISCOUNT = 0.20
    
    # Tax rates
    DEFAULT_TAX_RATE=0.05
    CA_TAX_RATE = 0.0725
    NY_TAX_RATE = 0.08875
    
    # Order Thresholds
    LOW_ORDER_THRESHOLD = 50
    MID_ORDER_THRESHOLD = 100
    
    # Shipping rate by threshold
    LOW_ORDER_SHIPPING = 5.99
    MID_ORDER_SHIPPING = 2.99
    MAX_ORDER_SHIPPING = 0
    
    def process(self, items, customer_type, state):
        total = 0
        for item in items:
            total = total + (item["price"] * item["qty"])

        if customer_type == "member":
            total = total - (total * self.MEMBER_DISCOUNT)
        elif customer_type == "vip":
            total = total - (total * self.VIP_DISCOUNT)

        if state == "CA":
            total = total + (total * self.CA_TAX_RATE)
        elif state == "NY":
            total = total + (total * self.NY_TAX_RATE)
        else:
            total = total + (total * self.DEFAULT_TAX_RATE)

        if total < self.LOW_ORDER_THRESHOLD:
            total = total + self.LOW_ORDER_SHIPPING
        elif total < self.MID_ORDER_THRESHOLD:
            total = total + self.MID_ORDER_SHIPPING
        else:
            total = total + self.MAX_ORDER_SHIPPING

        print("Receipt: $" + str(round(total, 2)))
        return round(total, 2)
