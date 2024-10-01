# 1 . Given the string
s = 'Python'

# Use indexning to print the following:

# print(s[-2]) # 'o'
# print(s[:-2]) # 'Pyth'
# print(s[1:-2]) # 'yth'
# print(s[::-1]) # 'nohtyP'

# 2 . Given the nested list:
l = [3,7,[1,4,'hello']]

# Reassign "hello" to be "goodbye"
l[2][2] = "goodbye"
# print(l)

# 3 . Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

grab_d1 = d1["simple_key"]
grab_d2 = d2["k1"]["k2"]
grab_d3 = d3['k1'][0]['nest_key'][0]

# print(grab_d1)
# print(grab_d2)
# print(grab_d3)


# 4 . Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

unique = set(mylist)
# print(unique)

# 5. You are given two variables:
age = 4
name = "Sammy"
# Use print formatting to print the following string:
# "Hello my dog's name is Sammy and he is 4 years old"

print("Hello my dog's name is {} and he is {} years old".format(name, age))
# or
print(f"Hello my dog's name is {name} and he is {age} years old")