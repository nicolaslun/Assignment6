import sys

user_inputs = sys.argv[1:-1]
threshold = int(sys.argv[-1])

try:
    numbers = [int(value) for value in user_inputs]
except ValueError:
    print("Error - All inputs must be integers")
    sys.exti(1)

if numbers:
    and_result = numbers[0]
    or_result = numbers[0]
    xor_result = numbers[0]
    for num in numbers:
        and_result &= num
        or_result |= num
        xor_result ^= num
    print(f"bitwise AND result: {and_result}")
    print(f"bitwise OR result:{or_result}")
    print(f"bitwise XOR result:{xor_result}")

try:
    threshold = int(input("Enter a threshold value: "))
    filtered_numbers = []
    for num in numbers:
        if num > threshold:
            filtered_numbers.append(num)
    print(f"Numbers greater than {threshold}: {filtered_numbers}")
except ValueError:
    print("Error: Threshold must be an Integer.")