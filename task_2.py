"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""

test_list = [1, 2, 2, 3, 4, 5, 5, 5, 6, 4, 1, 0, 9, 9]

filt_dubl = set()
result = set()

for numb in test_list:
    if numb in filt_dubl: result.add(numb)
    filt_dubl.add(numb)

print(result)
