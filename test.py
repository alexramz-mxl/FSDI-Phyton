# let varname = 1; 
varname = 2
varstring = "alexis"
variable = ""
varname = True

varstring = "alexis2"
print(varstring + str(varname))
# alexis2

# if(varsting == "alexis")
#{  
#}

age = 33
if age < 30:
    print("Youre young")
elif age > 30:
    print("no worries youre still young")
else:
    print("I dont know how you get here")

#array
#constcolors = ["red", "green", "blue"];
#list
colors = ["red", "green", "blue"]
print(colors)
colors.append("yellow")
print(colors)
colors.remove("red")
print(colors)
print(colors[2])

#for(int i=0; i <colors.length; i++){
# let color = colors[i]    
#}
#console.log(color)

for color in colors:
    print(color)
    
#dictionaries
me = {
    "first_name": "John",
    "last_last": "Doe",
    "age": 21,
}  

print(me)
#get a value
print(me["last_last"])

#functions 
def say_hello():
    print("Say hello")
#call functions 
say_hello()    

#functions
def print_menu():
    print("1-Sum")
    print("2-Substraction")
    print("3-Multiplication")
    print("4-Division")
    
#instruction
print_menu()
opt = int(input("Choose an option:"))
num1 = float(input("Please enter the first number:"))
num2 = float(input("Please enter the second number:"))

if opt == 1:    
    total = num1 + num2
    print("The sum result is:"+str(total))
    
elif opt == 2:    
    total = num1 - num2
    print("The substraction result is:"+str(total))

elif opt == 3:    
    total = num1 * num2
    print("The multiplication result is:"+str(total))

elif opt == 4:  
    total = num1 / num2
    print("The division result is:"+str(total))        