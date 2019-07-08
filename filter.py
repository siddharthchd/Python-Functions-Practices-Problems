def check_even(num):
    return num%2 == 0

nums = [0,1,2,3,4,5,6,7,8,9]
my_list = list(filter(check_even, nums))
# or for n in filter(check_even, nums)
#   print(n)
print(my_list)