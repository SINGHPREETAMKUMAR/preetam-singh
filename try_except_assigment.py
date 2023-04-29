
"""
.explain exception handling?what is an error in python.
"""
which disturb the normal fkow of the program,exception which is handle by try and except block its called exception handling.
error can be defined as the problems that occur in program due to any illogical operation performed by user or by fault of a program.

"""
2. how many except statements can a try except block have? name dome built in exception clesses.
"""
e.g:
1.valueError
2.zerodivisionError
3.keyerror
4.syntaxerror
5.indexerror
6.typeerror

"""
3.when will the else part of try _except_else be executed?
the else part is excuted when no exception occurs.
"""
try:
    exception block
    except:
               after exception executable statement
   else:
    without exception




"""
4.can one block  of except statements handle multiple exception?
"""
yes

"""
5.when is the finally block executed?
"""
always.



""""
6.whar happen when ,,1"==1 is executed?
"""
it will evaluted false and does not raise any exception.

"""
7.how do you handle exception with try/except/finally in python?explain with coding snippets.
"""
try:
    exception block
    except:
           after exception executable statement
   else:
        without exception
   finally:
           it always occur
  try:
    # varible defination
    # a=10
    # b=20
    # ans=a+b
    # print(ans) 
    # except:
    #         print("invalid input")
       else:
              print("welcome  to math world")
              finally:
                print("thanku for using this application")

"""
8. write a python  program  that user  to enter  only  odd numbers,else will raise an exception.
"""

n1=int(input("enter number 1:"))
n2=int(input("enter a number2"))
ans=n1+n2
print(ans)
































































