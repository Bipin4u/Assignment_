'''Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
(You may assume that the input to add_dots does not itself contain any dots.)'''

import re
def add_dot(word):
    return word[0]+((word.join(re.findall("\w(\w*)\w$",word))).replace("","."))+word[-1]

def remove_dot(word):
    return word.replace(".","")

print(add_dot("hello"))
print(remove_dot("h.e.l.l.o"))
