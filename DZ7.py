# def print_operation_table(operation, num_rows=6, num_columns=6):
#     l = [[operation(i, j)  for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in l:
#         print(*[f"{k:3}" for k in i])


# print_operation_table(lambda x, y: x * y)


# rythm = [len([i for i in el if i.lower() in "уеёэоаыяию"]) for el in input().split()]
# if all([i == rythm[0] for i in rythm]):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

