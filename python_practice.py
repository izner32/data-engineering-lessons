#LESSON 3.17 GITBASH COMMANDS

#ls - list
#cd Desktop - change directory to Desktop
#mkdir fileName - make directory/folder
#touch test.py - create py file
#nano test.py - go inside the file and create content for python
#python test.py - running the script

#LESSON 4.26 - COMMENTS
#'#' Use this hashtag for single line comments. Python doesn't support multi line comments :(

#LESSON 4. 27 - DATATYPES - has a lot of differentiation from c++ and java
a = 10 #int, no ';' semicolon at the end, new line means end of statement
b = 10.1 #float, there is no double in python
c = 10j #complex datatype (only used for complex numbers)
d = "sample string" #string datatype
e = True #boolean datatype
f = ["a","b","c"] #list datatype, somehow the equivalent of vector in c++ | changeable values and allows duplicate 
g = ("a","b","c") #tuple datatype | a collection which is ordered and unchangeable
h = range(10) #range, idk if this is datatype | RESEARCH MORE
i = {"name" : "Renz", "age" : 19} #dictionary container | unordered and changeable
j = {1,2,3} #set container | unordered and unindexed and no duplicate members
k = ({1,2,3,4,5}) #frozen set container
l = b"Hello" #byte datatype, idk what this does | RESEARCH MORE
m = bytearray(2) #bytearray, idk what this does | RESEARCH MORE
n = memoryview(bytes(1)) #memoryview, idk again what this does | RESEARCH MORE

#LESSON 4.27 A - LIMITATION OF PRINT FUNCTION
#print(a+b+d) #you can't mix a numerical value and string value when printing

#LESSON 4.27 B - KNOWING A VARIABLES DATATYPE
print(type(a)) #type(variable) is a function to know what datatype the variable is 

#LESSON 4.28 - NUMBERS (TYPECASTING)
aN = int(4.6) #convert 4.6 into an integer
bN = float(2) #convert 2 into a float
cN = complex(a) #convert 3 into a complex number

#LESSON 4.30 - BOOLEANS | ANYTHING WITH A VALUE IS TRUE JUST LIKE IN C++ BUT UNLIKE WITH JAVA
aBool = True
bBool = False
cBool = bool(123213) #since this has a value, this is automatically true
dBool = bool("") #this is 0, or no value, this is false

#application of boolean in if statements
if aBool:
    print("abool is true")
else:
    print("abool is false")

#LESSON 4.31 - OPERATORS
def operators() :
    #arithmetic operators
    a = 10
    b = 20
    result = a + b #addition
    result = a - b #subtraction
    result = a * b #multiplication
    result = a % b #modulus | get the remainder
    result = int(a / b) #division
    result = int(a ** b) #exponentation
    result = int(a // b) #floor division

    #assignment operators
    #l value = r value
    i = 123; #we are assigning the value of 123 to variable 'i'
    j = 10; #binary value: 01010
    k = 20; #binary value: 10100
    l = 30; #binary value: 011110
    m = 40; #binary value: 101000
    i += 123; #this is equal to i = i + 123
    i -= 123; #this is equal to i = i - 123
    i *= 123; #this is equal to i = i * 123 (multiply)
    j /= 123; #this is equal to j = j / 123 (division)
    k %= 123; #this is equal to k = k % 123 (remainder)
    i **= 100 #this is equal to i = i ** 100 (exponentation)
    l //= 1 # this is eqaul to l = l // 1 (floor division)
        
    #reassigning the values back to the default
    i = 123; #we are assigning the value of 123 to variable 'i'
    j = 10; #binary value: 01010
    k = 20; #binary value: 10100
    l = 30; #binary value: 011110

    #BITWISE ASSIGNMENT OPERATORS & BITWISE OPERATORS
    j &= k; #this is equal to i = i & k | & - both binary must be 1 to be 1 | resulting binary: 00000
    j ^= k; #this is equal to i = i ^ k | ^ - only 1 of the binary must be 1 to be 1 | resulting binary: 11110
    j |= k; #this is equal to i = i | k | | - only 1 of the binary can be 1 and it would be 1 | resulting binary: 11110
    l <<= 1; #this is equal to i = i << k | << - shift the binary value right | resulting binary: 111100
    m >>= 1; #this is equal to i = i >> k | >> - shift the binary value left | resulting binary: 010100

    #COMPARISON OPERATOR
    a = 1
    b = 2
    c = 0
    if a > b: #a is greater than b
        c = 1
    elif a < b: #a is less than b
        c = 2
    elif a == b: #a is equal to b | can also use 'is'
        c = 3
    
    d = 10
    e = 20
    if d >= e: #d is greater than or equal to e
        c = 4
    elif d <= e: #d is less than or equal to e
        c = 5
    elif d != e: #d is not equal to e | this would not get executed since d <= e is already true | can also use 'is not'
        c = 6
    elif a > b and d > e: #and = both statement must be true 
        c = 7
    elif a < b or d < e: #or = one statement must be true
        c = 8
    elif not(a == b and d > e): #it reverses the result, if result is true then this becomes false
        c = 9

    #MEMBERSHIP OPERATORS
    f = {1,2,3}
    g = 1
    if g in f: #if the value of g is in f then it is true
        c = 10
    elif g not in f: #if the value of is is not in f then it is false
        c = 11

#LESSON 4.32 - IF STATEMENTS - NO DIFF WITH C++ AND JAVA EXCEPT FOR ELSE IF, ELIF(FOR PYTHON)
def ifStatements () :
    a = 10
    b = 30
    c = False
    if a < b:
        False
    elif a > b: 
        True
    else:
        b = 5

#LESSON 4.33 - WHILE LOOP | PYTHON ONLY HAS THESE 2 KINDS OF LOOPS (FOR AND WHILE) UNLIKE C++ AND JAVA
def whileLoop() :
    boolVar = False
    a = 0
    while boolVar: #while true, do this
        a += 1
        boolVar = True
    
#LESSON 4.33A - BREAK AND CONTINUE STATEMENTS
def breakAndContinue () :
    a = 1
    MAX = 10
    while a <= MAX:
        a += 1
        if a == 3:
            continue #stop and go at the start of the loop again
        elif a == 6:
            break #stop the loop when this has been reached
        print(a)
        

#LESSON 4.34 - FOR LOOP
#this is the range based for loop example for python,only used with containers(data structure)
def rangeBasedForLoop () :
    a = [1,2,3]
    for x in a: #automatically incremets just like any other range based for loops
        print(x)
    for i in range(1,5):
        print(i)
    
#LESSON 4.35 - FUNCTION
#concept has no difference with c++ except you're like passing a template function <typename T> since you do not indicate the datatype which is weird
def sampleFunction (sampleParameter,**kwargs): #
    print("this is a sample function with a " + sampleParameter)
sampleArgument = "sample argument"
sampleFunction(sampleArgument) #argument is when passing value, it could be an l/r value
sampleFunction("abcds",sampleArgument = "sampleKeywordArgument") #this is the syntax for a sample keyword argument

def sampleFunctionWithReturn (x):
    return x * 5 #this would multiply by 5 whatever the value of x is
sampleFunctionWithReturn(100)

#LESSON 4.35A - MULTIPLE ARGUMENTS
def sampleArgs (*args): #this is not a pointer, this is an args which means you're passing multiple arguments. This is the equivalent of '...' in c++
    print(args)
    print(args[2]) #since args is a contigous block of memory you could do this just like in c++
sampleArgs("Renz"," Carillo"," is"," myName")

#LESSON 4.35B - MULTIPLE KEYWORD ARGUMENTS
def sampleKwargs (**kwargs): #this is not a pointer to a pointer, the purpose of this is the same for *args but explicitly for keywords
    print(kwargs)
sampleKwargs(a=1,b=2,c=3,d=4,e=5)

#LESSON 4.35C - PASSING LISTS AS AN ARGUMENT
#the default for loops is a range based for loops (catered for containers), for loops in python was specifically made for this
def sampleListArg (list): #idk if only the first element is getting passed and it's just getting incremented (list[i]) but i think it is since this is the case for other programming languages
    for x in list:
        print(x)

x = [1,2,3,4,5]
sampleListArg(x)
    
#LESSON 4.35D - PASS STATEMENT | when you're creating a function that's needed to be coded in the future
def funcPass ():
    pass

#LESSON 4.35E - RECURSION | same concept with c++
def recursionFunc (x,y):
    if x > 0:
        print("recursion[" + str(y) + "] = " + str(x))
        recursionFunc(x-10,y+1)
recursionFunc(100,1)

#LESSON 4.36 - LAMBDA | GENERIC PROGRAMMING
#lambda in python is a one liner function only, it is only useful in a disposable function, it can take many arguments
def funcLambda (x):
    return x + x

#var    = lambda var: (do something)
funLambda = lambda x: x + x #this is the equivalent of the function above
funLambda(5) #calling lambda function that was created, it is called like a regular function

#LESSON 4.37 - ARRAYS | there's no array in python, it's called list and it's the equivalent of vector in c++
#in c++ calling the var name of the array means you're referring to the first element thus you cannot change every value it holds on the way you declare them but in python it is somehow possible
arr = [1,2,3] 
#array method, there's a lot but here's a few, just check the documentation
arr.append(4) #add at the end of the list
arr.pop() #remove the last, it could also be pop(0) to remove the first element
print(arr[0]) #dereferencing the first element of the list

#LESSON 4.38 - CLASS 
#python's class is weird, it does not have data members, you declare data members outside the class and it just contains functions, 
#all functions are considered as static method for other languages such as c++ and java since you can call them even without creating an object

class SampleClass:
    #syntax for constructor, weird right?
    def __init__(self,firstName,lastName,age):#self is the equivalent of 'this' and it is required as parameter when using the functionality of 'this'
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    def print(self): #yeah we still need to pass self here since we would be using it
        print("Hello, " + self.firstName)
    
#obj = constructor | again, the syntax is really weird compared to c++ and java
obj = SampleClass("Renz","Carillo",19)
print(obj.age) #we're accessing the attribute 'age'
#SampleClass.print(obj) #here we're accessing it like it's a static method in c++

#LESSON 4.39 - INHERITANCE 
class DerivedClass (SampleClass): #this is the syntax for inheritance
    pass

#LESSON 4.39A - SUPER KEYWORD
#in java, super can be used to call the base's constructor,overriden method, or instance variable/data members, but in python only calling of base constructor is possible
class DerivedClass1 (SampleClass):
    def __init__ (self):
        print("Derived class has this and the one below")
        super().__init__("Markagne","Lazo",11) #in here we called the constructor of the base class using super

obj1 = DerivedClass1()
print(obj1.age)

#LESSON 4.40 - ITERATORS
#iterator is used for container that could be counted, e.g. array,string(technically it is an array of char),vector,stack,deque,etc. | it is like a pointer, when calling the array
nums = [1,2,3] #this is a list, which is a container, this is iterable
it = nums.__iter__() #another syntax for assigning this as an iterator is - it = iter(nums)
print(next(it)) #next(iterator) is the syntax for calling the next element in the array 

#creating your own iterator object class
class MyClass:
    def __init__ (self,start,end): #initializing the constructor
        self.start = start
        self.end = end
    def __iter__ (self): #this is required when creating ur own iterator
        return self
    def __next__ (self): #this is also required
        value = self.start
        self.start += 1
        return value

obj = MyClass(1,10)
print(obj.__next__())

#LESSON 4.41 - SCOPE | this is super ez but im gonna include it anyways since it's part of the learning path
y = 200 #this is a global variable, it could be used at any functions
def func():
    x = 100 #this is a local variable, its lifetime ends when the function ends, its scope is only inside this function

#LESSON 4.42 - MODULE | this is a collection of functions in a different file, a collection of module is library
import calcu #this is the equivalent of include <file.h> in c++
#import calcu as alias | 'as alias' means you could call this module as alias
#from calcu import * | do this if you dont want to call the import name everytime, import name in this instance is calcu
#syntax : (name of import).(class name).(method)
calcu.Calcu.add(5,10)
calcu.outsideClassFunction() #this is a function outside the class thus no need to call the class name

#LESSON 4.43 - DATES MODULE | this is a basic module to learn to access datetime
import datetime as dt
obj = dt.date(2021,5,8) #we are assigning this value to the constructor date class
print(obj.year) #access the year
print(obj.month) #access the month
print(obj.day) #access the day
objToday = dt.date.today() #we are assigning this variable to the method today()
print(objToday)
objTime = dt.time(1,2,3,4)
#there are a lot into this just look at the documentation

#LESSON 4.44 - MATH MODULE | basic collection of functions/method for math 
import math 
a = min(1,10) #find the minimum between the given set of number
b = max(10, 20) #opposite of min
c = pow(1,5) #power, seriously i dont need to explain this
d = math.sqrt(100)
#just look at the documentation for additional fucntions

#LESSON 4.45 - JSON MODULE | i dont think id be needing this soon since this requires javascript and probably only used for web development

#LESSON 4.46 - REGEX | Regular Expression, this is the equivalent of ctrl+f in an ide, it is used to find
# ^ - start
# $ - end
# \s - whitespace
# \S - non whitespace
# [abc] - look at the set that has matching letter
# [^abc] - look at the set that is not matching the letter
# . - any character
# * - match one character 0+ time
# + - match one character 1+ time
# ? - non greedy
import re as regex #re is the name of the module regex
sampleString = "my email is renzcarillo32@gmail.com"

#this would all find the matching keyword you specify
result0 = regex.findall("em", sampleString)
if result0:
    print(result0)
#this would search for all matching the keyword 'my email'
result = regex.search("^my.^email$", sampleString)
if result: #reminder: anything with a value is true
    print("yeah, there's a match")

#this would look at what position does the indicated pattern is from
result1 = regex.search("\s", sampleString)
if result1:
    print("first whitespace is located at position: " , result1.start()) #with (,) comma inside print, you explicitly convert int to str so it is much better to use than '+'

#since i specified whitespace, it would split every whitespace in the text sampleString
result2 = regex.split("\s", sampleString)
if result2:
    print(result2)

#substitute the indicated pattern with the one you'd like
result3 = regex.sub("s",".",sampleString)
if result3: 
    print(result3)

#LESSON 4.47 - PIP | Package manager for python packages and modules, used to install packages
#commands for command line for pip
#pip install pip - this is one time | install pip
#pip --version - check the version of pip
#pip install camelcase - download the 'camelcase' package | you can now use this package on python
#pip uninstall camelcase - uninstall the package 
#pip list -list the packages of pip
import camelcase as cc
c = cc.CamelCase()
txt = "capitalize the first letter of each word"
print(c.hump(txt)) #this method capitalizes the first letter of each word
#you could find more packages and documentation of each package at 'pypi.org'

#LESSON 4.48 - TRY EXCEPT | do this, if error do this
try: #do this
    inp = int(input())
#except: | this is not a good practice since it is too broad in every error this would appear, it is better to be specific at error
except ZeroDivisionError as zd: #if this error occured
    print(zd)
except: #this is like else if
    print("wrong input")
else: #else is if all except wasn't executed
    print("yo, it was a success")
finally: #this always execute
    print("finally is always present")

#LESSON 4.49 - INPUT | equivalent of std::cin in c++
user = input("Enter your username")
print("Hello ", user)

#LESSON 4.50 - STRING FORMAT | this is to format the string text that is out of your control e.g. they're in database
                                     #0 - element no. | : | .3f - make it decimal to to 3 points
text001 = "here is a sample string no. {0:.3f}" #'{}' is the placeholder used for string formatting
number = 1
print(text001.format(number))
                                    #you could also leave '{}' but it is not a good practice
text001 = "here is a sample string no. {} and not {1}"
number = 1
secondNumber = 2

text002 = "print text like this {carname}"
print(text002.format(carname = "Ford")) #you could also define the formatted string inside the argument

#LESSON 5.51 - VARIABLES 
a = 10 #variables cannot be declared in python, only initialized

#LESSON 5.54 - UNPACKING VARIABLES | other programming languages has an equivalent of this one
a,b,c = 1,2,3 #here is a way
d = e = f = 5 #another weird way (im not sure if this is possible in c++ and java)
arrArrArr = [1,2,3,4,5]
g,h,i,j,k = arrArrArr #assigning the values  of arrArrArr to g,h,i,j,k, it's like doing g = arrArrArr[0], h = arrArrArr[1], etc.

#LESSON 5.54.5 - UNPACKING WITH ASTERISK OPERATORS | JUST LIKE SPREAD OPERATOR 
def my_sum(a,b,c):
    return (a+b+c)
my_list = [1,2,3]
my_sum(*my_list) # this is equivalent to passing my_sum(1,2,3) like in spread operator 


#LESSON 5.55 - OUTPUT | equivalent to std::cout << in c++ and System.out.println() in java, but srsly why is this only covered later on the course?
print("just print this")

#LESSON 5.56 - GLOBAL VARIABLES | this is a little feature that differs with c++ since reassigning and initializing has the same syntax in python
x = 10
y = 5
def funcfuncfunc():
    global x #we are calling the global variable x
    x = 50 #if we do this are we assigning or initializing? we're initializing thus a variable x for global and local scope is created, it is not reassigned and this two x are two different x
    #here is an example when the problem arises
    #y += 1 #this would produce an error because the python thought you are initializing | this is equal to y = y+1, its only good for reassigning
    print(x)

#LESSON 6.58 - STRING
#example of multiline string, use 3 """
strString = """ a b c d
e f g h """ 
string0001 = "access it like this"
print(string0001[0]) #the way you access it is the same with c++ and java

#LESSON 6.58A - USE OF IN AND NOT IN | it is used if an element is inside the container, it returns true or false
if "a" in string0001:
    print("a is in stringVar")
if "x" not in string0001:
    print("x is not in stringVar")

#LESSON 6.59 - SLICING STRINGS
sampleStringString = "hello hello world"
print(sampleStringString[2:8]) #start the slicing at element 2 which is 'l' and end it with element 8 which is 'l'
print(sampleStringString[:3]) #it could be like this and vice versa, if like this it starts with 'h' and ends with 'l'

#LESSON 6.60 - STRING METHODS
stringtring = "abdDsF"
print(stringtring.upper()) #this means capitalize every letter
print(stringtring.lower()) #lower all of the capital letters
#just look at the documentation for more different methods

#LESSON 6.63 - ESCAPE CHARACTERS
#this is used to use illegal characters inside string literals
print("here is an example use of escape \n character \" ") #use backslash followed by whatever character you want

#LESSON 7.67 - LIST |it is the most flexible among dictionary,set,and tuple, it's like vector in c++ except vector cant hold both numerical and alpha characters at the same time, it is ordered ang changeable
listSample = [1,2,3,4,5,6]

#this is how to access a list
print(listSample[0]) #access first index like an array
print(listSample[-1]) #access last index of the list

#access specific part of the list only
print(listSample[1:3]) #this means start the access at the second index element and end it with the 4th index element

#you could change all items in the list at once, which is impossible to do at c++ and java, you could only select specific part
listSample = [6,5,4,3,2,1] #you are changing the whole list, this is impossible in c++ and java
listSample[1:3] = [20,30,50] #you are changing the 2nd index element up to 4th index element, also impossible in c++ and java

#insert item at list (just like vector)
listSample.insert(0,1231231)

#add items at the end (just like in vector)
listSample.append(9000)

#combine a list into another list
combineThisList = [69,79,89]
combineThisTuple = (70000,80000,60000)
listSample.extend(combineThisList) #congrats, you just combined these two lists
listSample.extend(combineThisTuple) #you could even combine different collections/container
#or you could do this
listSample3 = listSample + combineThisList #in c++ an overloaded operator for '+' shall be used 

#delete,pop,remove,clear | delete and pop are basically the same with different syntax
listSample.remove(70000) #we have removed the 70000 from the list
listSample.pop(0) #we have removed the first index element, leaving the argument blank would mean remove the last item of the list
del listSample[0] #remove the first index element, 'del listSample' means deleting all of the content of the list or the list itself?
listSample.clear() #we removed the content of the list but the list is still there

#looping through list, default range based for loop is the best practice
loopThisList = ["Facebook","YouTube","Google","Instagram"]
for i in loopThisList: #best practice to loop a colleciton/container
    print(i)

for i in range(len(loopThisList)): #another weird way to loop
    print(loopThisList[i])

i = 0
while i < len(loopThisList): #just a regular while loop
    print(loopThisList[i])
    i = i + 1

[print(x) for x in loopThisList] #very weird way to loop but it is a one liner, it is also called as list comprehension

#LESSON 7.72 - LIST COMPREHENSION | this is a one liner for loop
listCompre = [1,2,3,4,5,6,7]
[print(x) for x in listCompre] #syntax: content for var in listToLoop | you could also do double for loop just add another for var in listToLoop

#this is the equivalent of the code above
listCompre = [1,2,3,4,5,6,7]
for x in listCompre:
    print(x)

#LESSON 7.73 - SORTING LIST
print(listCompre.sort()) #sort them from smallest to biggest
print(listCompre.reverse()) #reverse the order
print(listCompre.sort(reverse = True)) #start from biggest to smallest

#copying list
myCopyList = listCompre.copy() #use the method .copy() to copy and assign list into myCopyList

#LESSON 8.78 - TUPLES | this is basically a list but you cannot modify the values
sampleTuple = ("a","b","c") #the syntax for tuple uses '()' parentheses

#this is how to access a tuple
print(sampleTuple[0]) #access first index like an array
print(sampleTuple[-1]) #access last index of the tuple

#access specific part of the list only
print(sampleTuple[1:3]) #this means start the access at the second index element and end it with the 4th index element

#adding from tuple | this is more of a hack, we first convert it into list then convert it into tuple
convertList = list(sampleTuple)
convertList.append("d") #here i have added a d, i was able to add since this is currently a list
sampleTuple = tuple(convertList) #i have converted it back to tuple, now the collection cannot be modified again

#removing from tuple | just the same with adding
convertList = list(sampleTuple)
convertList.append("d") #here i have added a d, i was able to remove since this is currently a list
sampleTuple = tuple(convertList) #i have converted it back to tuple, now the collection cannot be modified again

#deleting tuple, just the same with deleting list
del sampleTuple

#LESSON 8.81 - UNPACKING TUPLES | its like a dictionary in some way
unpackTuple = ("green","blue","yellow") #here we are creating a tuple
(var1,var2,var3) = unpackTuple #here we are saying var1 = "green", var2 ="blue", var3 = "yellow"
print(var1)

#looping tuples, just the same as looping list
loopThisTuple = ["Facebook","YouTube","Google","Instagram"]
for i in loopThisTuple: #best practice to loop a colleciton/container
    print(i)

for i in range(len(loopThisTuple)): #another weird way to loop
    print(loopThisTuple[i])

i = 0
while i < len(loopThisTuple): #just a regular while loop
    print(loopThisTuple[i])
    i = i + 1

#joining tuples, everything is actually just the same with list why am i still doing this
tuples1 = (1,2,3)
tuples2 = ("a","b")
tuples3 = tuples1 + tuples2 #this uses overloaded operator on c++
print(tuples3)
tuples4 = tuples1 * 3 #yeah you could even multiply the content of tuples 1
print(tuples4)

#tuple methods | it has two methods which is count() and index(), a list has alot more
tupleTuple = (1,2,3,5423,23,2353461,4523,536,54,36,34,1345,23)
tupleCount = tupleTuple.count(23) #it counts how many '23' are there in this tuple
tupleIndex = tupleTuple.index(23) #it returns what is the index value of the argument '23'
print(tupleCount)
print(tupleIndex)

#LESSON 9.86 - SETS | the content must be unique only and it is ordered(for numbers only), the numerical characters are automatically ordered while alpha characters aren't, it is also unindexed
sampleSet = {4,2,3,1} #its syntax is like array in c++ and java but it's not and the difference are huge

#access set items, you cannot access it like the way you access list and tuple, you can only access it through for loop using in
for x in sampleSet:
    print(x)

#modify set items
sampleSet.add(5) #obviously add a value
addThisSet = {"a","b","c"}
sampleSet.update(addThisSet) #combine two sets, or any other collections such as list,dictionary,tuple

#to remove an item you can use discard or remove
sampleSet.remove(5) #we removed the value of 5 in this set
sampleSet.discard("a") #idk whats the purpose of putting two methods that does the exact same thing
sampleSet.pop() #we are removing the last value index element, this isnt a good idea since set is automatically organized thus we do not know what is getting removed
sampleSet.clear() #remove all of the contents
del sampleSet #completely remove this set
sampleSet = {1,2,3,4}
sampleSet2nd = {5,6,7,8}
sampleSet3rd = sampleSet.union(sampleSet2nd) #combine sampleSet and sampleSet2nd | this is the same with update or idk
#just look at the documentation for more methods

#LESSON 10.94 - DICTIONARY | this is a collection of key value pairs
sampleDictionary = {
#key   : value
"var1" : "abc",
"var2": 123,
"var3": "efg"
}

#access dictionary
print(sampleDictionary["var1"]) #this would print abc, this is the best practice
print(sampleDictionary.get("var1")) #equivalent of the syntax above

#adding item to the dictionary
sampleDictionary["var4"] = "asdgfasdf" #syntax for adding item

#printing values and key:value pair
print(sampleDictionary) #in here we are only printing the values
print(sampleDictionary.keys()) #we are printing the keys with its value pair too!
print(sampleDictionary.items()) #idk really what this does but it seems to convert everything into an item of each on their own including the keys

#modifying dictionary
sampleDictionary["var4"] = 123 #here i have modified the content of var4
sampleDictionary.update(var4 = 321) #it could be like this but this is honestly weird, just use the one above
sampleDictionary.pop("var4") #remove a pair, input the key as an argument
sampleDictionary.popitem() #remove the last pair
sampleDictionary.clear() #clear all of the contents
del sampleDictionary #delete the existence of this sampleDictionary

#looping dictionary
sampleDictionary = {"var1": 123, "var2": "abc", "var3": 321 }

#this would only print the keys
for x in sampleDictionary: #you could do 'in sampleDictionary.keys() and this would do the same thing
    print(x)

for x in sampleDictionary.values(): #this would print the values
    print(x)

for x,y in sampleDictionary.items(): #this would print both the keys and values
    print(x,y)

referenceDictionary = sampleDictionary #this is the syntax for referencing, every changes made in referenceDictionary would affect the sampleDictionary
copyDictionary = sampleDictionary.copy() #this would copy the values of sample Dictionary
copyDictionaryAgain = dict(sampleDictionary) #this would do the same

print(copyDictionaryAgain)

#nested dictionary
progLanguages = {
    "java" : {
        "difficulty" : "medium",
        "oop" : True
    },
    "c++" : {
        "difficulty" : "hard",
        "oop" : True
    },
    "python" : {
        "difficulty" : "easy",
        "oops" : True
    }
}

#-------------------------------------------------------------------------------------------------------------
#LESSON S.1 - DUNDER METHODS | special methods in class
class SampleDunderClass:
    def __init__(self): #constructor
        self.x = x
    def __repr__(self): ##this is displayed to the end user when an object of this class is called but the display is overriden when u use __str__, this is meant for developers
        return "SampleDunderClass({})".format(self.x)
    def __str__(self): #this is displayed to the end user when an object of this class is called
        return "The x of SampleDunderClass is {}".format(self.x)
    def __add__(self,other): #this is the equivalent of 'class operator+()'/overloaded operator in c++
        return self.x + other.x


#LESSON S.2 - DECORATORS | modify the functionality of a function without changing the code, only usede when passing a function as argument
def outsideFunc(func):
    def insideFunc(): #yes, function inside a function is possible in python but not in c++ and java
        print("Executing Inside Function")
        func()
        print("End Inside Function")
    return insideFunc #it's returning the memory address of insideFunc

#instead of doing this thing below we could just write it with decorators --------------------------
#def printer():
#    print("Hello World")

#display = outsideFunc(printer) #this is equivalent to writing display = insideFunc, now if we want to call the inside func we could write this as outsideFunc(printer)()
#display() #this is equivalent to writing outsideFunc(printer)()
#---------------------------------------------------------------------------------------------------
@outsideFunc #this is equivalent to writing outsideFunc(printer), we are like passing printer to outsideFunc
def printer():
    print("Hello World")

printer() #we could just do this instead, it is equivalent to outsideFunc(printer)(), since it has a decorator it's like we're calling it's decorator function and passing this function as an argument

#LESSON S.3 - EVERYTHING IS AN OBJECT even functions, functions are first class objects which could be pass around like a variable
def funcFunc():
    return 5
def funcFunc000(functionPass):
    return functionPass() + 5 #since functionPass is a reference to funcFunc we must add '()' parentheses | if you cannot understand read the text below first | syntax for reference is object = object1, in c++ it is int& object = object1
print(funcFunc000(funcFunc)) #here because we have written functionPass = funcFunc, functionPass becomes a reference to function funcFunc, if we wanted to grab it by value then we must do functionPass = funcFunc()

#LESSON S.4 - ANY AND ALL | any - if one of the iterable is true then it returns true, if empty return false | all - every iterable must be true or empty to return true
any(["abc",False,1]) #this would return true since it has two values that is true
all({}) #it has no value so it must be true
boolVar = any([x == "a" for x in "rango"]) #example usage of any in a list comprehension
print(boolVar)

#LESSON S.5 - WITH KEYWORD - to make writing codes cleaner, it's like a way to make substitute name for a function(yes, just like assigning variable lmao)
# without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')

#LESSON S.6 - ASSERT KEYWORD - to check if the the "==" is true 
assert 1 == 1  # does not raise an error
assert False  # raises AssertionError
assert 1 + 1 == 3 # raises AssertionError







































        

    

    
    





