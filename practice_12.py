import random

# Task 1: "Quick Search"
print("Task 1: Quick Search")
cities = ["Kyiv", "Odesa", "Lviv", "Kharkiv", "Zhytomyr"]
city_set = set(cities)

city1 = "Odesa"
city2 = "Poltava"

if city1 in city_set:
    print(f"The city '{city1}' is present in the list.")
else:
    print(f"The city '{city1}' is not present in the list.")

if city2 in city_set:
    print(f"The city '{city2}' is present in the list.")
else:
    print(f"The city '{city2}' is not present in the list.")

print("-" * 20)

# Task 2: "Search by Dictionary"
print("Task 2: Search by Dictionary")
student_grades = {"Ivan": 80, "Maria": 95, "Oleg": 78, "Anna": 85}

student_name = input("Enter student's name: ")

try:
    grade = student_grades[student_name]
    print(f"The grade of student '{student_name}' is: {grade}")
except KeyError:
    print(f"Student with the name '{student_name}' not found.")

print("-" * 20)

# Task 3: "Optimization of Repetitions"
print("Task 3: Optimization of Repetitions")
large_list = [random.randint(1, 100) for _ in range(1000)] # Generate a list with repetitions

occurrence_counter = {}
for number in large_list:
    occurrence_counter[number] = occurrence_counter.get(number, 0) + 1

most_frequent_number = None
max_occurrence = 0

for number, count in occurrence_counter.items():
    if count > max_occurrence:
        max_occurrence = count
        most_frequent_number = number

print("The number that appears most often:", most_frequent_number)
print("Number of occurrences:", max_occurrence)