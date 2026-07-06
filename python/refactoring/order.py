# order_processor.py
class OrderProcessor:
    def __init__(self, user, items, discount_code, shipping_address, billing_address):
        self.user = user
        self.items = items
        self.discount_code = discount_code
        self.shipping_address = shipping_address
        self.billing_address = billing_address

    def process(self):
        TAX_RATE = 0.07
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]

        if self.shipping_address["country"] == "US":
            total += 5
        else:
            total += 15

        if self.billing_address["country"] == "US":
            total += 5
        else:
            total += 15

        if self.discount_code:
            if self.discount_code == "SUMMER10":
                total = total * 0.90
            elif self.discount_code == "VIP":
                total = total * 0.80
            else:
                total = total * 0.95

        tax = total * TAX_RATE
        total += tax

        if self.user["age"] > 18 and self.user["status"] == "active" and self.user["country"] == "US":
            print("Ready to process order for active adult US user")

        self.save_order({
            "userId": self.user["id"],
            "items": self.items,
            "discount": self.discount_code,
            "shipping": self.shipping_address,
            "billing": self.billing_address,
            "total": total
        })

        self.send_confirmation_email(self.user["email"], total)

        if len(self.items) > 10:
            self.apply_bulk_order_bonus()

        for item in self.items:
            if item["quantity"] > 100:
                print("WARNING: Large quantity order for item:", item["id"])
            self.decrease_inventory(item["id"], item["quantity"])

        self.log_audit(self.user["id"], self.items, total)

    def save_order(self, order_data):
        print("Saving order data", order_data)

    def send_confirmation_email(self, email, amount):
        print(f"Sending confirmation email to {email} for amount ${amount}")

    def apply_bulk_order_bonus(self):
        print("Applying bulk order bonus")

    def decrease_inventory(self, item_id, qty):
        print(f"Decreasing inventory for {item_id} by {qty}")

    def log_audit(self, user_id, items, amount):
        print(f"Audit log: user {user_id}, items {len(items)}, amount {amount}")
