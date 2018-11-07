# 1 is default value.
# 1 step input some value
# 2 step input same value of 1 step
# 3 step input half value of 2 step
# 4 step infut half value of 3 step

# you have to make total 100 number with default value. Means result will be show 100.
print("**************** Improve Yourself **************")


default = 1
first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

third_number = int(input("Third Number: "))
fourth_number = int(input("Fourth Number: "))
result1 = first_number + second_number
result2 = second_number / 2
result3 = third_number / 2
main_result = default + result1 + result2 + result3
print(main_result)
if main_result != 100:
    print("It is not 100. Try again please")
else:
    print("Successful Result", main_result)


