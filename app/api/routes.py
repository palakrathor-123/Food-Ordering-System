from fastapi import APIRouter
from services.matching_service import match_items
from services.order_service import extract_order, format_order

router = APIRouter()

@router.post("/match-order")
def match_order(data: dict):
    text = data.get("text")

    if not text:
        return {"error": "Text is required"}

    matched_items = match_items(text)

    order = extract_order(text, matched_items)
    summary, total_items, total_price = format_order(order)

    return {
        "input": text,
        "matched_items": [item["name"] for item in matched_items],
        "order_summary": summary,
        "total_items": total_items,
        "total_price": total_price
    }