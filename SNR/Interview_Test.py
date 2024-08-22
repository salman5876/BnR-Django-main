
#################################Question1 #################################################
# Implement the function sort_by_price_ascending, which:
# Accepts a string in JSON format, as in the example below.
# Orders items by price in ascending order.
# If two products have the same price, it orders them by their name in alphabetical order.
# Returns a string in JSON format that is equivalent to the one in the input format.
# For example, the call
# sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]');
# should return
# '[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'.
import  json
def sort_by_price_ascending(val):
    val=json.loads(val)
    val=sorted(val,key=lambda i:(i['price'],i['name']))
    val=json.dumps(val)

    print(type(val))
    print(val)
    ###### dumps convert json into string but not showing into braces format. that Concatenate ' '
    val=str("'"+val+"'")
    return val

sort=sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
print(sort)





######################### Question4 ###################################
# Write the function to slice the tuple between the given start (inclusive)
# and end (exclusive) indexes, and join the resulting range of values as a comma delimited string.
# For example, tuple_slice(1, 4, (76, 34, 13, 64, 12)) should return "34,13,64".

def tuple(val):
    string='"'
    slice=val[2][1:4]
    for x in slice:
        string=string+str(x)+','
    string=string[0:len(string)-1]
    string=string+'"'
    return string
tuple_slice=(1, 4, (76, 34, 13, 64, 12))
print(tuple(tuple_slice))

######################### Question2 ################################
# Create a class LanguageStudent with:
# property languages - returns all languages, as a list, that the student  knows.
# method add_language(language) - adds a new language to the list of languages.
# Create a class LanguageTeacher that inherits LanguageStudent and has one additional public method:
# teach(student, language) - if LanguageTeacher knows the required language, it teaches LanguageStudent and returns true; otherwise it returns false.
# For example, the following code shows how LanguageTeacher teaches LanguageStudent the new language ('English'):
# teacher = LanguageTeacher()
# teacher.add_language('English')
# student = LanguageStudent()
# teacher.teach(student, 'English')
# print(student.languages)

class LanguageStudent():
    def __init__(self):
        self.languages=list()
    # def languages(self):
    #     return self.languages()
    def add_language(self,language):
        self.languages.append(language)
        print(self.languages)
class LanguageTeacher(LanguageStudent):
    def teach(self,student, language):

        if language in self.languages:
            student.languages.append(language)
            return True
        else:
            return False
teacher = LanguageTeacher()
teacher.add_language('English')
student = LanguageStudent()
val=teacher.teach(student, 'English')
if val==True:
    print("Teacher can teach student")
else:
    print("Teacher can not teach student")

############################# Questin No 3 #################################

# Q3.
# A script you are writing uses logarithmic functions from the math module.
# Implement the add_patch function that should add a log100 function to the math module.
# The log100 function should wrap the existing math.log function so that it calculates a logarithm with a base of 100.
# For example, math.log100(10) is equivalent to math.log(10, 100) and should return 0.5.
import math
print(math.log(10,100))
#################### Patch Function #####################################
def log100(self,val):
    calculate=math.log(val,100)
    return calculate
math.log=log100
print(math.log100(10))

