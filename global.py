total=0;
#global variabble
#function definition
def sum(arg1,arg2):
    total=arg1 + arg2
#local variable
    print('inside a function locaal to this', total)
    return total
#call function
sum(20,20)
print('outside a function global is' , total)