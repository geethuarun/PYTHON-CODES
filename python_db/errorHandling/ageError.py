# custom made error using raise

# age=int(input("enter age"))


# if age<18:
#     raise Exception("invalid age")
# else:
#     print("valid")

# 
num=input("enter number")


if type(num)==int:
    print(num**3)
else:
    raise Exception("operand must be integer")

co