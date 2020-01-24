import sys
import math

numbers = []
with open(sys.argv[1]) as file:
    for number in file:
        numbers.append(int(number))

def get_percentil(nums, perc):
    nums.sort()
    d = (len(nums)-1) * perc/100
    # Округление до ближайшего меньшего числа
    prev = math.floor(d)
    # Округление до ближайшего большего числа
    next = math.ceil(d)
    # Если результат d был целым числом
    if prev == next:
        return nums[int(d)]
    #интерполяция промежуточного значения
    d_prev = nums[int(prev)] * (next-d)
    d_next = nums[int(next)] * (d-prev)
    d_sum = d_prev+d_next
    return d_sum

print("%.2f" %get_percentil(numbers,90))
print("%.2f" %get_percentil(numbers,50))
print("%.2f" %float(max(numbers)))
print("%.2f" %float(min(numbers)))
print("%.2f" %(sum(numbers)/len(numbers)))


