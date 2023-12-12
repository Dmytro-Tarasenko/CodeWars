def sq_in_rect(lng: int, wdth: int) -> list:
    if lng == wdth:
        return

    res = []
    lng, wdth = max(lng, wdth), min(lng, wdth)

    while (lng - wdth) > 0:
        res.append(wdth)
        lng, wdth = max(wdth, lng - wdth), min(wdth, lng - wdth)

    return res

print(sq_in_rect(3, 5))
print(sq_in_rect(20, 14))