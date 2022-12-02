total = 0
calorie_list = []
total_calories_list = []

with open("input.txt", "r") as f:
    for line in f:
        calorie_list = [line.strip() for line in f]

for i in calorie_list:
    if i != '':
        total += int(i)
    else:
        total_calories_list.append(total)
        total = 0

total_calories_list.sort(reverse=True)
three_highest_calories = total_calories_list[0] + total_calories_list[1] + total_calories_list[2]

print("Part 1:", max(total_calories_list))
print("Part 2:", three_highest_calories)