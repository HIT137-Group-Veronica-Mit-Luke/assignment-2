#Question 3: Part 1: a) Use AI to converse the bottom image to text, adding 2 print functions at the end.

#Input
total = 0
for i in range (5):
    for j in range (3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j
counter = 0
while counter <5:
    if total < 13:
        total +=1
    elif total >13:
        total -=1
    else:
        counter +=2
print(total)
print(counter)

##Question 3: Part 1: b) There are 2 keys to try: 13 and 6
"""
#Output
PS C:\Users\Mit> & C:/Users/Mit/AppData/Local/Programs/Python/Python312/python.exe "d:/S124 HIT137/ASSIGNMENT 2/test.py"
13
6
"""

#Question 3: Part 2: a) Below is the decrypted code with key = 13 (with key=6, code can not be translated)
#and the text is conversed from the above right image.
#and adding \n for output to enter a new line, thanks AI for the productivity.

#Input
def decrypt(text, key):
  
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)    
        else:
            decrypted_text += char
    return decrypted_text
original_code = "tybony_inevnoyr = 100\nzl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xr13': 'inyhr3'}\n\nqrs cebprff_ahzoref():\n    tybony tybony_inevnoyr\n\n    ybpny_inevnoyr = 5\n    ahzoref = [1, 2, 3, 4, 5]\n\n    juvyr ybpny_inevnoyr > 0:\n        vs ybpny_inevnoyr % 2 == 0:\n            ybpny_inevnoyr -= 1\n            ahzoref.erzbir(ybpny_inevnoyr)\n\n    erghea ahzoref\n\nzl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}\nerfhyg = cebprff_ahzoref(ahzoref=zl_frg)\n\nqrs zbqvsl_qvpg():\n    ybpny_inevnoyr = 10\n\n    zl_qvpg['xr14'] = ybpny_inevnoyr\n\nzbqvsl_qvpg(5)\n\nqrs hcqngr_tybony():\n    tybony tybony_inevnoyr\n    tybony_inevnoyr += 10\n\nsbe v va enatr (5):\n    cevag(v)\n\n    v += 1\n\nvs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10:\n    cevag(Pbaqvgvba zrg!)\n\nvs 5 abg va zl_qvpg:\n    cevag(5 abg sbhaq va gur qvpgvbanel!)\n\ncevag(tybony_inevnoyr)\ncevag(zl_qvpg)\n\ncevag(zl_frg)\n"
key = 13
decrypted_code = decrypt(original_code,key)
print(decrypted_code)

#Question 3: Part 2: b)Output with a bit edit in the string ""
"""
PS C:\Users\Mit> & C:/Users/Mit/AppData/Local/Programs/Python/Python312/python.exe "d:/S124 HIT137/ASSIGNMENT 2/test.py"
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'ke13': 'value3'}

def process_numbers():
    global global_variable

    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            local_variable -= 1
            numbers.remove(local_variable)

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)

def modify_dict():
    local_variable = 10

    my_dict['ke14'] = local_variable

modify_dict(5)

def update_global():
    global global_variable
    global_variable += 10

for i in range (5):
    print(i)

    i += 1

if my_set is not None and my_dict['ke14'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)

print(my_set)
"""

#Question 3: Part 3: a) Firstly, comment on each line about syntax and general purposes.

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'ke13': 'value3'}

def process_numbers(): #Should have a parameter as an input for this function
    global global_variable

    local_variable = 5 #No relevant for in this function
    numbers = [1, 2, 3, 4, 5] #Should be outside of this function

    while local_variable > 0: #Should use "for" loops instead of "while" loops because of limit loops in the list numbers
        if local_variable % 2 == 0: #find the even numbers
            local_variable -= 1 #why assign -1 to this variable?
            numbers.remove(local_variable) #to remove even numbers out of list numbers, but if local_variable is -1 and in list numbers doesn't have any value -1, it will show value error.
#Better to create new empty list and append all the odd numbers in, not modifying the old list numbers
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} #Eventhough we declare this set with duplicates but Python will understand this set have no duplicates
result = process_numbers(numbers=my_set) #Syntax error, to change the set to list use list(my_set) and also change result to my_set because of the print function at the end

def modify_dict(): #This function is defined with no arguments for my_dict
    local_variable = 10

    my_dict['ke14'] = local_variable #Assign value 10 to key 'ke14' in the dictionary my_dict

modify_dict(5) #but it's called with an argument(5), Error because the function doesn't expect any arguments

def update_global():
    global global_variable
    global_variable += 10 #Need a return statement is the result of this function call at the end of this function body
#Need a call out function before print 
for i in range (5): #This for loops is correct syntax with 5 times loops 
    print(i) #but doesn't have any meaning relating to other parts of this code, better to delete this for loop

    i += 1

if my_set is not None and my_dict['ke14'] == 10:
    print("Condition met!")

if 5 not in my_dict: #The if statement checks if the key 5 is in my_dict. However, dictionary keys must be unique and immutable (unchangeable) so they typically cannot be numbers. Better to use string "5". Anyway, this check is always true.
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)

print(my_set)

#Question 3: Part 3: b) Secondly, edit and organise the code after analysis with a strategy based on the 3 print functions at the end.

#Question 3: Part 3: b1) Below code is for print(global_variable)

global_variable = 100
def update_global(global_variable):
    global_variable +=10
    return global_variable

global_variable = update_global(global_variable)
print(global_variable)

#Question 3: Part 3: b2) Below code is for print(my_set)

numbers = [1, 2, 3, 4, 5]
def process_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
my_set = process_numbers(list(my_set))
print(my_set)

#Question 3: Part 3: b3) Below code is for print(my_dict)


numbers = [1, 2, 3, 4, 5]
def process_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
my_set = process_numbers(list(my_set))

my_dict = {'key1': 'value1', 'key2': 'value2', 'ke13': 'value3'}
def modify_dict():
    local_variable = 10
    my_dict['ke14'] = local_variable
modify_dict()

if my_set is not None and my_dict['ke14'] == 10:
    print("Condition met!")
if "5" not in my_dict:
    print("5 not found in the dictionary!")

print(my_dict)


#Question 3: Part 3: c) Thirdly, running above code to see the final output: 5 prints out.
"""
PS C:\Users\Mit> & C:/Users/Mit/AppData/Local/Programs/Python/Python312/python.exe "d:/S124 HIT137/ASSIGNMENT 2/test.py"
110
[1, 3, 5]
Condition met!
5 not found in the dictionary!
{'key1': 'value1', 'key2': 'value2', 'ke13': 'value3', 'ke14': 10}
"""