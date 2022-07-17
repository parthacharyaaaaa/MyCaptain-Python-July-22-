filename = input("Please enter your complete file name: ")
f_extns = filename.split(".")
print("The extension of the given file is: "+repr(f_extns[-1]))