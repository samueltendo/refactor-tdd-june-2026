# invoice.py
class InvoiceProcessor:
    def process(self, items, customer_type, state):
        total = 0
        for item in items:
            total = total + item["price"] * item["qty"]

        if customer_type == "member":
            total = total - (total * 0.10)
        elif customer_type == "vip":
            total = total - (total * 0.20)

        if state == "CA":
            total = total + (total * 0.0725)
        elif state == "NY":
            total = total + (total * 0.08875)
        else:
            total = total + (total * 0.05)

        if total < 50:
            total = total + 5.99
        elif total < 100:
            total = total + 2.99

        print("Receipt: $" + str(round(total, 2)))
        return round(total, 2)
