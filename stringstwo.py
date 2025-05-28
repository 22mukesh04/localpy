print("This is from lecture 2\n")
str1="this is a string\n"
str2='string with single quote\n'
str3="""string with triple quote
        is used for more 
lines\n"""
print(str1,str2,str3)
print(str1+str3)

# Concatenation
# " hello"+"world" = "hello world"
# basic operations concatenation and len(str)
string1="hello\t"
string2="world"
print(string1,string2)
print(string1+string2)
print(string2,string2)
print(string2+string2)
concatenated_string=string1+string2
print(concatenated_string)

### Length function len(str)
print(len(str1),len(string1))
len1=len(str1)
len2=len(string2)
print(len1,len2)

# Indexing
str = "hello world"
ch = str[0]
print(ch)

# Slicing
# accessing parts of a string
print(str[2:5]) # ending number index not print or included
print(str[3:]) # from index 3 to len(str)
print(str[:5])
# Negative Index is not a part of other languages . it is a special feature of python language 
strf="APPLE"
print(strf[-5:])
print(strf[-3:-1])

# string ends with function
strb="hello this is a big string"
print(strb.endswith("ing"))
print(strb.endswith("in"))
print(strb.capitalize())
