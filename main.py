letters = 0    
digits = 0     
spaces = 0     
others = 0     

# 获取用户输入
user_input = input("请输入一行字符：")

# 遍历每个字符并统计
for char in user_input:
    if char.isalpha(): 
        letters += 1
    elif char.isdigit():  
        digits += 1
    elif char.isspace(): 
        spaces += 1
    else:  # 其他字符
        others += 1

print(f"英文字符：{letters}个")
print(f"数字：{digits}个")
print(f"空格：{spaces}个")
print(f"其他字符：{others}个")
