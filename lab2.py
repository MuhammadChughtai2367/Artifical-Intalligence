# list = ["Apple", "Grapes", "Mango"]
# for i in list:
#     print(i)
# for i in range(len(list)):
#     print (list[i])

# s = "Muhammad"
# for i in s:
#     print(i)

# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
#     print(i)

# for letter in 'geeksforgeeks':
#     if letter=='e' or letter == 's':
#         continue
#     print('Current letter: ',letter)

# for letter in 'geeksforgeeks':
#     if letter=='e' or letter == 's':
#         break
#     print('Current letter: ',letter)


#Function in Python
# def My_Function(country = 'Pakistan'):
#     print("My country is: ",country)

# My_Function()
# My_Function("Brazil")

# def function(food):
#     for i in food:
#         print(i)
# list = ["Apple", "Grape", "Mango"]
# function(list)

# def my_function(x):
#     return 5*x
# print(my_function(10))
# print(my_function(43))

#keyword arguments
# def Function(child1 , child3 , child2):
#     print("The biggest Child is: ", child2)
# Function(child2 = "FAraz",child1="Rana", child3="Muhammad")

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def My_Function(self):
        print("My name is: ",self.name)
p1 = person("Muhammad",20)
print(p1.name)
print(p1.age)
p1.My_Function()