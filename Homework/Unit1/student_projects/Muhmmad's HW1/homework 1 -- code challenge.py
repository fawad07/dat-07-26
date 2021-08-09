
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# # Project 1: Python Coding Exercises
# 
# _Authors: Joseph Nelson (DC) _
# 
# ---

# The following code challenges are drawn from common exercises used in technical interviews.
# 
# Please note that there may be several ways to approach each challenge. If you get stuck, try mapping out your approach in pseudocode first. Finally, while solutions to problems like these may be found online, remember that if you copy/paste code that you can't explain, you'll be missing out on the point of the project. The only way to truly learn a new skill is through practice, trial, and error - we can only help you improve by understanding where you are having trouble.
# 
# **Note:** To receive the highest credit, make sure your answers are wrapped up in functions that we can call!

# ### Challenge 1: Largest Palindrome
# A palindromic number reads the same both ways. For example, 1234321 is a palindrome. The largest palindrome made from the product of two two-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two three-digit numbers. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[2]:

'''
Parameter: list of int
return: list of int
Description: takes an empty list and fills with integers of length 3
'''
def get_product_of_three_digit_num(mylist):
    for i in range(100, 1000):
        for j in range(100, 1000):
            mylist.append(i*j)
    return mylist

'''
parameter: list of int
return: list of str
Description: takes a list of integers and converts them to a list of string
            because have to check the string from left to right and right to 
            left
'''
def conv_int_to_str(mylist):
    str_list=[]
    for i in mylist:
        str_list.append(str(i))
    return str_list

'''
parameter: list of str
return: list of palimdromes
Description: takes a list of strings and checks the string forwards with
               the string backwards to see if its a palimdrome
               and returns a string of palimdromes

'''
def all_palimdrome(alist):
    plist=[]
    for i in alist:
        if i == i[::-1]:
            plist.append(i)
    return plist
    
'''
parameter: list of str
return: list of int
Description: takes a list of palimdromes that are a string and converts tham to
            an integer. returns a new list of palimdromes that are integers
'''
def conv_str_to_int(alist):
    int_list=[]
    for i in alist:
        int_list.append(int(i))
    return int_list
    
'''
#parameters: list of palimdrome int
#return: maximum int palimdrome
Description: takes a list of palimdrome integers and returns the maximum
'''
def max_pal(alist):
    max_pal = max(alist)
    return max_pal
    
    
    
def main():
    
    #product of num in range 100 -1000
    mylist= []
    mylist = get_product_of_three_digit_num(mylist)
    
    #convert all int to str in list
    str_list=[]
    str_list = conv_int_to_str(mylist)
    
    #find palimdromes
    pal_list=[]
    pal_list = all_palimdrome(str_list)
    
    #convert str to int
    int_list = conv_str_to_int(pal_list)
    
    #find max palimdrome
    largest_pal = max_pal(int_list)
    print(largest_pal)
    
    
if __name__ == "__main__":
    main()


# 
# ### Challenge 2: Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below 2,000. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[4]:

'''
Parameter: int
return: bool
Description: takes an integer greater than 0 and 1
            loops through the integer and checks if integer is
            a prime number
            returns false if integer is 0 or 1 or not a prime number
            retruns true if number is prime
'''
def is_prime(n):
    #checks if number is greater than 1
    if n <= 1:
        return False;
    else:
        #loops from 2 - n
        for i in range(2, n):
            if n%i == 0:
                return False
    return True

#print(is_prime(5))   #DEBUGGING 
def main():
    num = 10    #last number --> 2000
    prime_sum=0

    for i in range(num+1):
        check_prime = is_prime(i)   #check if number is prime
        #print(check_prime)      #debuging statement
        #if prime than sum prime numbers
        if check_prime:
            prime_sum = prime_sum+i;     #sum of prime number
    print(prime_sum)

        
if __name__ == "__main__":
    main()


# ### Challenge 3: Multiples of 3 and 5
# If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 and 5 below 1,000. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[3]:

'''
Parameter: an int
return: bool
Description: takes an integer and checks if the integer 
            is divisible by 3
            returns true if yes otherwise false
'''
def is_mult_3(num):
    if num%3 != 0:
        return False
    return True

'''
Parameter: an int
return: bool
Description: takes an integer and checks if the integer 
            is divisible by 5
            returns true if yes otherwise false
'''
def is_mult_5(num):
    if num%5 != 0:
        return False
    return True

def main():
    sum = 0                  #stores the sum of numbers ONLY multiple of 3 and 5
    #loop through numbers between 0-1000
    for i in range(1000):
        mult_3 = is_mult_3(i)          #checks if current number multiple of 3
        mult_5 = is_mult_5(i)          #checks if current number multiple of 3
        #checks if currnet number multiple of 3 OR 5
        if mult_3 or mult_5:
            sum = sum + i              #add current number to the sum
    print(sum)


if __name__ == "__main__":
    main()


# ### Challenge 4: String Compressor
# Implement a method to perform basic string compression using the counts of repeated characters. (This is called run-length encoding.) For example, the string "aabcccccaaa" would become a2b1c5a3. If the “compressed” string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a–z). Specify whether your solution is case sensitive or case insensitive and what you would need to change to make it the other. Afterward, write a brief explanation walking through your code's logic in markdown.

# In[2]:

'''
Parameter: string
return: string
Description: takes an input string, counts the number of
            identical characters and compress them
            i.e aaabbbccc --> a3b3c3
'''
def compress(a_str):
    result_str = ' '      #compressed string
    count = 0             #counts number of identical characters
    temp_str = a_str[0]   #temperary character used to check the charcter at the current position
    
    #loop through the input string
    for i in range(0, len(a_str)):
        #check if the temp character is identical to the current character
        if temp_str == a_str[i]:
            count +=1                #increase count by one 
            temp_str = a_str[i]      #set temp char to current char
        else:
            #if temp char != to current char
            result_str=result_str + temp_str + str(count)           #combine the character and numbers into one
            count=1                    #reset count
            temp_str = a_str[i]
    return result_str
    
    
def main():
    str_in = "abbccd"      #input string
    print(compress(str_in))
    
if __name__ == "__main__":
    main()


# ### *BONUS* Challenge: FizzBuzz
# Write a program that prints all of the numbers from 1 to 100. For multiples of 3, instead of the number, print "Fizz;" for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz." Afterward, write a brief explanation walking through your code's logic in markdown.

# In[3]:

'''
Parameter: an int
return: bool
Description: takes an integer and checks if the integer 
            is divisible by 3
            returns true if yes otherwise false
'''
def is_mult_3(num):
    if num%3 != 0:
        return False
    return True

'''
Parameter: an int
return: bool
Description: takes an integer and checks if the integer 
            is divisible by 5
            returns true if yes otherwise false
'''
def is_mult_5(num):
    if num%5 != 0:
        return False
    return True


def main():
    #loops through a given number, number 100 cn be changed
    for i in range(100):
        mult_3 = is_mult_3(i)       #checks if current number is mutiple of 3
        mult_5 = is_mult_5(i)       #checks if current number is multiple of 5
        #checks if current number is multiple of BOTH 3 and 5
        if mult_3 and mult_5:
            print("FizzBuzz")
        #checks if number is multiple of ONLY 5
        elif mult_5:
            print("Buzz")
        #checks if current number is multiple of ONLY 3
        elif mult_3:
            print("Fizz")
        #if current number NOT a multiple of 3 and 5
        else:
            print(i)
            

if __name__ == "__main__":
    main()


# In[ ]:



