# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print("hello_"+ user_name +"!")
hello_name("Heather")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1 -100 and returns nothing

def first_odds():
    for num in range(1, 101, 2):
        print(num)
first_odds()


# Question 3
# Write a python function, max_num_in_list to return the max number of a given list

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num
a_list = [-2.4, 3, 10, 0, 300, 56]
print(max_num_in_list(a_list))


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean type

def is_leap_year(a_year):
    if a_year % 4 ==0:
        if a_year % 100 ==0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False
    
print(is_leap_year(2000))
print(is_leap_year(2023))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example [2,3,4,5,6] are consecutive numbers but [1,2,4,5] are not.
# The return should be boolean type

def is_consecutive(a_list):
    if len(a_list) <= 1:
        return False
    
    for i in range(len(a_list)-1):
        if a_list[i+1] - a_list[i] != 1:
            return False
    return True

print(is_consecutive([2,3,4,5,6,7]))
print(is_consecutive([1,2,4,5]))
