filepath = 'C:/Users/peter/Curators/1.txt'
with open(filepath) as file:
    n = int(file.readline())
    rows = {}
    for line in file:
        row, number = line.split(' ')
        if '9' in number:
            if rows.get(row):
                rows[row] += 1
            else:
                rows[row] = 1
    max_key = max(rows, key=lambda x: rows[x])
    print(max_key, rows[max_key])
