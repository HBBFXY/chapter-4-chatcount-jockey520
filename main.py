letters = 0    
digits = 0     
spaces = 0     
others = 0     


user_input = input()


for char in user_input:
    if char.isalpha(): 
        letters += 1
    elif char.isdigit():  
        digits += 1
    elif char.isspace(): 
        spaces += 1
    else:  # 其他字符
        others += 1

print(f"英文字符：{letters}")
print(f"数字：{digits}")
print(f"空格：{spaces}")
print(f"其他字符：{others}")
