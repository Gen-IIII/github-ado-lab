def total_after_discount(subtotal: float, rate: float) -> float:
    """割引後の金額を小数第2位で丸めて返す。"""
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if not 0 <= rate <= 1:
        raise ValueError("rate must be between 0 and 1")

    # 負の subtotal を拒否していないのは、後で Bug として修正するため。
    return round(subtotal * (1 - rate), 2)
