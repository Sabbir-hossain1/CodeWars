import re

# Solution 1
# def capitalize_words(s):
#     return re.sub('[_-]([a-zA-Z])', lambda x: x.group(1).title(), s)

# Solution 2
# def to_camel_case(text):
#     removed = text.replace("-"," ").replace("_",' ').split()
#     if len(removed) == 0:
#         return ""
#     return removed[0] + ''.join(x.capitalize() for x in removed[1:])

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


my_string = "this_is-an_example" 
new_string = to_camel_case(my_string)
print(new_string.replace('_', '').replace('-', ''))
