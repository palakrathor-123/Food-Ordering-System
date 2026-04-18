import json

with open("data/menu.json", "r") as f:
    menu = json.load(f)

def match_items(text):
    text = text.lower()
    results = []

    # burger → only one item
    if "burger" in text:
        results.append(next(item for item in menu if item["name"] == "Veggie Burger"))

    # coke → only one drink
    if "coke" in text or "cola" in text or "drink" in text:
        results.append(next(item for item in menu if item["name"] == "Diet Coke"))

    return results