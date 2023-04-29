"""
1. WAP sum of first n +ve integers
"""
n = int(input("Enter the No.:"))
sum=0
for i in range(0,n+1):
    sum=sum+i
    n=n-1
print("Sum:",sum)

"""
2. WAP to count occurrences of a substring in a string
"""
s = "Hello Python Programming"
print(s)
print(s.count("o"))

"""
3. WAP to count occurrence of each woprd in a given sentence
"""
s = "It's not okay to be okay"
r = input("Enter the word: ")
a=[]
count=0
a = s.split(" ")
for i in range(0,10):
    if(r==a[i]):
        count = count+1
print("Count of word is: ", count)
"""
4. WAP to get a single string from two given string, seperate by a space and swap the first two characters of each string.
"""
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")
print(s1)
print(s2)
s1,s2=s2,s1
print("After swapping String 1=", s1, "String 2=", s2)

"""
5. WAP to add 'ing' at the end of a given string (length should be at least 3).If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged
"""
def add_string(str1):
  length = len(str1)
  if length > 2:
    if str1[-3:] == "ing":
      str1 += "ly"
    else:
      str1 += "ing"
  return str1
print(add_string("dp"))
print(add_string("dpp"))
print(add_string("string"))

"""
6. WAP to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
"""
#Return the resulting string
def not_poor(s1):
  snot = s1.find('not')
  spoor = s1.find('poor')
  
  if spoor > snot and snot>0 and spoor>0:
    s1 = s1.replace(s1[snot:(spoor+4)], 'good')
    return s1
  else:
    return s1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
"""
7. WAP to find the greatest common divisor of two numbers
from math import gcd
"""
a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))
gcd(a,b)
print("The gcd of number1 and number2 is: ", gcd(a,b))

"""
8.WAP to check whether a list contains a sublist
"""
l1 = [0,1,2,3,4,5,6,7,8,9]
l2 = [2,4,6,18]
print(l1)
print(l2)
if (set(l2).issubset  (set(l1))):
    print("L2 is subset of L1")
else:
    print("L2 is not the subset of L1"

"""
9. WAP to find the second smallest number in a list
""
l1 = [100,101,102,103,104,105]
l1.sort()
print("Second smallest number: ", l1[1])


"""
10.write a python program to get a unique values from a list.
"""
#s={10,20,30,50,30,10,61,85,61}
#print(s)
          
"""
11.write a python program to unzip a list of tuples into individual lists.
"""
#t=(10,20,30,40,50)
#print(t)
#for iteam in t:
#   print(iteam)

"""
12.write a python program to convert of tuples into dictionary.
"""
#t=[("apple",1),("orange",2)]
#print(t)
#my_dict=dict(t)
#print(my_dict)

"""
13.write a python program to sort a dictionary(ascending/descending)by value
"""
#my_dict={"apple":10,"banna":5,"mango":15}
#asc=dict(sorted(my_dict.items(),key=lambda x:x[1]
#desc=dict(sorted(my_dict.items(),key=lambda x:x[1]
#print ("origanal dictioary:",my_dict)
#print("sorted dictionary(ascending):,(asc))
#print("sorted dictionary(descending):,(desc))

"""
14.write a python program to find the higgest 3 values in dictionary.
"""

my_dict={"a":10,"b":14,"c":60,"d":80,"e":55}
#sorted dictionry=sorted(my_dict.items(),key=lambda x:x[1],reverse=true)
#higest_value=[value for key,value in sorted_dict[:3]]
#print("the higest 3 values in the dictionary are:,higest_value)


"""
15.given a number n,write a python program to make and print the list of fibonacci series up to n.
input:n=7
hint:first 7 number in the series
excepted output:
first few fibonacci numbers are 0,1,,1,2,5,6,3,8,9,13
"""
 #def fibonacciseries(i):
     #if i<=1:
         #returni
         #else:
             #return(fibonacciseries(i-1)+fibonacciseries(i-2))
            #num=int(input("enter a number")
            #if num<=0:
                    
                #print("please enter a positive number")
                    #else:
                        #print("fibonacci series:",end=" ")
                        #for i in range(num)
                        #print(fibonacciseries(i),end=" ")
                        

             
"""
16.counting the frequencies in a list using a dictionary in python.
"""
l1=[,2,3,5,8,7,2,3,6,5,9,1]
freq={}
for (iteam in freq):
       freq[item]+=1
       else:
           freq[iteam]=1
           for key,value in freq.iteam():
               print("%d:%d"%(key,value))



               
"""
17.write a python program using function to finf the sum of odd series and even series
odd series:12/1! +32/3! +52/5! +


"""
18.write a program  to find factorail of number using recursion
"""
def factorial(n):
    if (n==1 or n==0):
        return 1
        else:
            return (n* factorial(n-1))
            print("number:",num)
            print("factrioal:",factrioal(num))


 """
 19.write a program  that takes a list  and returns a new  list with  unique elements of the first list.
"""
def unique_list(1):
    x=[]  
    for a  in x:
        x.append(a) 
        return x
        print(unique_list([1,1,2,2,2,3,3,3,5,6,8]))    

 """
 20. make a program  to gennerate  a strong  password using the input given by the user. to generate a password,
 randomly take some words from the user the user input and then  include nummbers,special characters and captical 
 letter to generate the password.also,keep a check that password lenght is more than 8 characters.
 """
 import array
 import random

 max_len=12
 digits=['0','1','2','3','4','5','6','7','8','9',] 
 locase_characters=['a','b','c','d','e','f','g','h','i','e','f','g','h','e','f','i','j','q','z','x','v','n','m','w','e',]   
 upcase_characters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
 symbols=['@','#','$",'%','^','&','*','<','.>,'?',]   
 cobined_list=digits+upcase_characters+locase_characters+symbols
 rand_digit=random.choice(digits)
 rand_upper=random.choice(upcase_characters)
 rand_lower=random.choice(locase_characters)
 rand_lower=random.choice(symobls)
 temp_pass=rand_digit+rand_upper+rand_lower+rand_symbol


 for x in range(max_len-4):
              temp_pass=temp_pass+random.choice(combined-liist)
              temp_pass_list=array.array('u',temp_pass)
              random.shuffle(temp_pass_list)
              password=""
              for x in temp_pass_list:
                                    password=password+x
                                    print(pasword)



  """                                  

      
      


    






