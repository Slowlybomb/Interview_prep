from datetime import datetime

def sort_orders(orders: list[tuple[str, str]]) -> list[str]:
    """
    Sort orders chronologically based on ISO 8601 timestamps.

    Args:
        orders: List of tuples (order_id, timestamp)

    Returns:
        List of order IDs sorted by timestamp
    """
    sorted_orders = sorted(orders, key=lambda order: datetime.fromisoformat(order[1]))
    return [order[0] for order in sorted_orders]

if __name__ == "__main__":
    orders = [("A100", "2025-05-20T10:00:00"), ("A101", "2025-05-19T22:00:00")]
    print(sort_orders(orders))
