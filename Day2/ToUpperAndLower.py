given_str="Thankyousomuch"

count=1
converted_string = ''
for char in given_str:
    if((count%2) ==1):
       x=char.upper()
    else:
        x=char.lower()
    count=count+1
    converted_string=converted_string+x

print("Original String: {}".format(given_str))
print("converted_string: {}".format(converted_string))