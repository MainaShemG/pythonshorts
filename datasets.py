'''list= ['abcd ,1234 ,name:Joe']
tinylist =[1234, 'Joe']
print (list)
print (list[0])
print (list[2:6])
print (list+ tinylist)

name = input("Enter your name please: ")
age = input("enter you age:")
print(f'you are {name} and {int(age)} years old')

myset={3,3,3,4,4,5,5,5,23,34,23,65,56,77}
print(myset)'''


#adding elements to list
my_list=[1,2,3]
print(my_list)#outputs
my_list.append([66, 67, 'another example'])
print(my_list)#outputs [1,2,3 [66,67, 'another example']]
my_list.insert(2, 'insert example')
print(my_list)#outputs [1,2, 'insert example',3 [66,67, 'another example']]

#deleting elements
my_list=[1,2,3, 'example',69,'example2', 3.142]
print(my_list)
del my_list[5]#removes element index 5 from list
print(my_list)#outputs[1,2,3, 'example',69, 3.142]
my_list.remove('example')
print(my_list)#outputs [1,2,3,69, 3.142]
my_list.pop(3)
print(my_list)#output  [1,2,3, 3.142]
my_list.clear()
print(my_list)#outputs an empty list

#accessing elements
my_list=[1,2,3, 'example',69,'example2', 3.142, 678, 'last element']
for element in my_list: #access elements one by one
    print(element)
print(my_list)#access the whole list
print(my_list[2:5])#access element from index 2 to 5
print(my_list[-1])#access list in reverse


#TUPLES
my_tuple=(1,44,3.142, 'tuple example')
print(my_tuple)
my_tuple=my_tuple+(4,4,6,'another tuple')#append a tuple
print(my_tuple)#output (1, 44, 3.142, 'tuple example', 4, 4, 6, 'another tuple')


#DICTIONARIES
dict={}
dict['one']='This is one'
dict[2]='This is two'
tinydict={'name':'John','code':'6000', 3:'zendaya'}
print (dict['one'])
print (dict[2])
print (tinydict)#outputs {'name': 'John', 'code': '6000', 3: 'zendaya'}

tinydict
print(tinydict.keys())# outputs dict_keys(['name', 'code', 3])
print(tinydict.values())#outputs dict_values(['John', '6000', 'zendaya'])
#adding and changing values
tinydict['code']=  7000#changes the element to 7000
print(tinydict)
tinydict[4]='casie'# adds a new pair entry
print(tinydict)
#deleting elements
del tinydict['name']#deletes the element with that value
print(tinydict) #outputs {'code': 7000, 3: 'zendaya', 4: 'casie'
tinydict.pop(4)  #removes element with that value
print(tinydict)#outputs{'code': 7000, 3: 'zendaya'}
#accessing
print(tinydict['code']) #outputs element with key code

#SETS
my_set={3,3,3,4,4,5,5,5,23,34,23,65,56,77}
print(my_set)#outputs{65, 34, 3, 4, 5, 77, 23, 56}
my_set.add('zendaya')
print(my_set)#outputs {65, 34, 3, 4, 5, 77, 'zendaya', 23, 56}
my_set2={3.142,33,44, 3,3,5,5, 4,56, 'new zendaya', 'zendaya'}
print(my_set2)
#manipulating sets
print(my_set.union(my_set2))#outputs {'zendaya', 65, 34, 3, 4, 5, 33, 3.142, 44, 77, 'new zendaya', 23, 56}
print(my_set.intersection(my_set2)) #outputs {'zendaya', 3, 4, 5, 56}
print(my_set.difference(my_set2))#outputs {65, 34, 77, 23}
print(my_set.symmetric_difference(my_set2))#outputs {33, 65, 3.142, 'new zendaya', 34, 44, 77, 23}
