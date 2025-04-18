even_sum = 0
odd_sum = 0

for num in range(1, 11):
    if num % 2 == 0:
        print(f"Even Num: {num}")
        even_sum += num
    else:
        print(f"Odd Num: {num}")
        odd_sum += num

print(f"Total Even: {even_sum}")
print(f"Total Odd : {odd_sum}")
