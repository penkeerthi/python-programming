first_name = "keerthi"
last_name = "p"
age=29

#this variable adds firstname and last name with space - This is called String Concatenation 
full_name = first_name + " " + last_name
#print(full_name) 

#String Interpolation -
# f is the format string 
print(f"Hello World,my name is {full_name} and i am {age} old")

# This is the old method where instead of f , we use .Format (map) this is before 3.7 
print("hello world my name is {}and im {} years old".format(full_name,age))



