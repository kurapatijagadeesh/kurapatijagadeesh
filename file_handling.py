"""
file handling
"""

"""
read
write
append
binary
"""

#read

"""
# r read
# r+  read&write
# rb  read binary
# rb+ read binary&write
"""

#write

"""
# w  write
# w+   write&read
# wb  write binary
# wb+ write binary&write
"""

#append

"""
a   append
a+  append&read
ab  append binary
ab+ append binary&write
"""should

"""
#read operation
  two methods
  1.open methods
  2.withopen
"""
#open methods
#should be close once work complete
#syntax:
"""
<variable>=open(<file name>,"mode")
<variable>.close()
""" 

file_obj=open("names.txt","r")
print(file_obj.read())
file_obj.close()
