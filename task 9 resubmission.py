###What is the expected output of the following python code given below:
###data= [10,501,22,37,100,999,87,351]
###result= filter(lambda x:x >4,data)

data= [10,501,22,37,100,999,87,351]
result= filter(lambda x:x >4,data)
print(list(result))

##Using a python Lambda function create a fibonacci series from 1 to 50 elements?
def fibonacci(count):
    fib_list=[0,1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
            range(2, count)))
    return fib_list[:count]
print(fibonacci(50))


##Write a python function to validate Regular Expressions for the following:
##a.Email Adress
##b.Mobile number of bangladesh
##c.Telephone numbers of USA
##d.16 characters Alpha-numeric password,composed of alphabets of upper case,lower case,Special characters,numbers..
1.
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("enter you Email: ")
if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")
    2.
import re
number=input("enter your mobile number: ")
pattern=re.compile("(880)?[-\s]?[6-9][0-9]{9}")
if pattern.match(number):
    print(f"{number} is valid number for bangladesh")
else:
    print(f"{number} is invalid number for bangladesh")
3.
import re
number=input("enter your mobile number: ")
pattern=re.compile("(1)?[-\s]?[6-9][0-9]{9}")
if pattern.match(number):
    print(f"{number} is valid number for USA")
else:
    print(f"{number} is invalid number for USA")\
    
    4.
import re
password=input("enter the password: ")
if (len(password)<16):
    print("password must be 16 characters long")
elif re.search(r"[!@#$%&]",password) is None:
    print("password must contain atleast one special character")
elif re.search(r"\d",password) is None:
    print("password must contain atleast one digit")
elif re.search ("[A-Z]",password) is None:
    print("password must contain one capital letter")
elif re.match(r"[a-z A-Z 0-9 !@#$%&]{16}",password):
    pattern=re.compile(r"[a-z A-Z 0-9 !@#$%&]{16}")
    result=pattern.match(password)
    print("password is correct")
    breakpoint()
else:
    print("password is invalid")
    



      



