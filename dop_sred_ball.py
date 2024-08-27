grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
dict_average_score = {}
i = 0
while i < 5:
    n1 = sum(grades[i]) / len(grades[i])
    dict_average_score.update({students[i]: n1})
    i += 1

print(dict_average_score)
