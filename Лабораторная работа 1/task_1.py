numbers = [2, -93, -2, 8, 0, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_ = 4
sum_of_numbers = sum(numbers[:index_]) + sum(numbers[index_:])
numbers[4] = sum_of_numbers / len(numbers)

print("Измененный список:", numbers)
