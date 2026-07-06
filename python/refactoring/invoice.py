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
        subtotal = self._calculate_subtotal(items)
        discounted = self._apply_discount(subtotal, customer_type)
        taxed = self._apply_tax(discounted, state)
        final_total = self._apply_shipping(taxed)
        print("Receipt: $" + str(round(final_total, 2)))
        return round(final_total, 2)
    
    def _calculate_subtotal(self, items):
        subtotal = 0
        for item in items:
            subtotal = subtotal + item["price"] * item['qty']
        return subtotal
            
    def _apply_discount(self, amount, customer_type):
        if customer_type == "member":
            return amount - (amount * self.MEMBER_DISCOUNT)
        elif customer_type == "vip":
            return amount - (amount * self.VIP_DISCOUNT)
        return amount
    
    def _apply_tax(self, amount, state):
        if state == "CA":
            return amount + (amount * self.CA_TAX_RATE)
        elif state == "NY":
            return amount + (amount * self.NY_TAX_RATE)
        return amount + (amount * self.DEFAULT_TAX_RATE)
        
    def _apply_shipping(self, amount):
        if amount < self.LOW_ORDER_THRESHOLD:
            return amount + self.LOW_ORDER_SHIPPING
        elif amount < self.MID_ORDER_THRESHOLD:
            return amount + self.MID_ORDER_SHIPPING
        return amount
