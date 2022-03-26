# sort() method         = used with list
# sort() function       = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

#students.sort()

sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)

print("====================")

students_score = [("Squidward", "F", 23),
                  ("Sandy", "A", 43),
                  ("Patrick", "C", 80),
                  ("Spongebob", "D", 99),
                  ("Mr. Krabs", "F", 100)]

age = lambda ages:ages[2]
students_score.sort(key=age)

for row in students_score:
    for colum in row:
        print(colum, end=" | ")
    print()

