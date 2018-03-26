#! python3
# Counts odd numbers up to indicated value

cnum = 0
while cnum < 100:
    cnum += 1
    if cnum % 2 == 0:
        continue
    print(cnum)
