Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(username):
    print("Hello_" + username)

hello_name("USERNAME") 
  
Question 2
Print first 100 odd numbers in Python.

for value in range(1,201,2)
    print(value)


Question 3
Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
result=max(a_list);
    return result

                
Question 4
Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
leap_year = ((a_year%400==0) or (a_year%100!=0 and a_year%4 ==0));
    return leap_year

Question 5
Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
max = max(a_list)
min = min(a_list)
len = len(a_list)
consecutive = ((max - min + 1)== len);
print consecutive
