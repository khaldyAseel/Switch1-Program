# How would you make this work?
#  add(2, 5); // 7
#  add(2)(5); // 7 (edited) 


def add(num1):
    def sum_result(num2):
        sum = num1+ num2
        return sum
    return sum_result


print(add(2)(5))