import re
sen="hi hi hello hello hi hide 13 inhidden 13,14 15:16 "
ct=re.findall("[0-5][0-9]",sen)
print(ct)