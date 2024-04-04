
def find_sum(*number_list):
    total_sum = 0
    for num in number_list:
        total_sum += num
    return total_sum

result = find_sum(1, 2, 3)
print(result)
