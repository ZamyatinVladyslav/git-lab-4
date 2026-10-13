def late_fee(days, daily):
    if days < 0:
        raise ValueError("Кількість днів не може бути від'ємною")

    if not isinstance(days, int):
        raise ValueError("Кількість днів має бути цілим числом")

    if daily < 0:
        raise ValueError("Денний тариф не може бути від'ємним")

    return min(days * daily, 100)