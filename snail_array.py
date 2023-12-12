array_data = [[1, 2, 3, 4, 5],
              [16, 17, 18, 19, 6],
              [15, 24, 25, 20, 7],
              [14, 23, 22, 21, 8],
              [13, 12, 11, 10, 9]]

def rotate(data: list) -> list:
    if len(data) == 0:
        return []
    res = []
    x_lim = len(data)
    y_lim = len(data[0])
    if y_lim == 0:
        return []
    for col in range(y_lim):
        row = [data[x][y_lim-col-1] for x in range(x_lim)]
        res.append(row)
    return res


snailed = []
for _ in range(2*(len(array_data))-1):
    snailed.extend(array_data.pop(0))
    array_data = rotate(array_data)

print(snailed)