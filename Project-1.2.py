filename = input("Input the Filename: ")
f_extns = filename.split(".")
a= str(f_extns[-1])
b= None
if a=='py':
    b= "python"
elif a=='java':
    b= 'Java'
elif a=='txt':
    b= 'text'
elif a=='docx':
    b='document'
else:
    b='Unknown Extension'            
print ("The extension of the file is : "+"'"+b+"'")
