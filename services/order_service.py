import re

def word_to_number(word):
    mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }
    return mapping.get(word, None)


def extract_order(text, matched_items):
    text = text.lower()
    order = {}

    # regex to capture: quantity + item
    pattern = r'(\d+|one|two|three|four|five)\s+(\w+)'
    matches = re.findall(pattern, text)

    for qty_word, item_word in matches:

        # convert quantity
        if qty_word.isdigit():
            qty = int(qty_word)
        else:
            qty = word_to_number(qty_word)

        for item in matched_items:
            if item_word in item["name"].lower():
                order[item["name"]] = {
                    "qty": qty,
                    "price": item["price"]
                }

    # fallback (if something missed)
    for item in matched_items:
        if item["name"] not in order:
            order[item["name"]] = {
                "qty": 1,
                "price": item["price"]
            }

    return order


def format_order(order):
    summary = []
    total_items = 0
    total_price = 0

    for item, data in order.items():
        qty = data["qty"]
        price = data["price"]

        summary.append(f"{item} x{qty} = ₹{qty * price}")

        total_items += qty
        total_price += qty * price

    return summary, total_items, total_price