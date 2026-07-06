// invoice.js
class InvoiceProcessor {
  process(items, customerType, state) {
    let total = 0;
    for (let i = 0; i < items.length; i++) {
      total = total + items[i].price * items[i].qty;
    }

    if (customerType === "member") {
      total = total - total * 0.10;
    } else if (customerType === "vip") {
      total = total - total * 0.20;
    }

    if (state === "CA") {
      total = total + total * 0.0725;
    } else if (state === "NY") {
      total = total + total * 0.08875;
    } else {
      total = total + total * 0.05;
    }

    if (total < 50) {
      total = total + 5.99;
    } else if (total < 100) {
      total = total + 2.99;
    }

    console.log("Receipt: $" + total.toFixed(2));
    return Math.round(total * 100) / 100;
  }
}

module.exports = { InvoiceProcessor };
