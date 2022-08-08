'''
lamda is a small anonymous function
we can right in single line operation
'''
# lambda function
'''
map
filter
reduce
'''
data= lambda a,b:a+b
print(data(7,8))

#map
'''
my_list=[1,2,3,4,5,6,7,8,9]
new_list=list(map(lambda x:x*2,my_list))
print(new_list)
'''

#filter

'''
my_list=[1,2,3,4,5,6,7,8,9,14,26,27]
print(list(filter(lambda x:x%2==1,my_list)))
'''

#reduce
import functools
list=[1,2,3,4,5]
print(functools.reduce(lambda a,b:a+b,list))


















