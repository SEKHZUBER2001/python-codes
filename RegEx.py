import re 
#Regular Expression(RegEx)
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

pattern_1 = r"\W"  # Matches any non-word character
text_01 = "Hello,world!"
matches = re.findall(pattern_1, text_01)
if match:
    print("Charecter Found:",matches)
else:
    print("Charecter not found!")
search=text_01.find('ld')
result  = re.findall("ld",text_01)
print(result,search)