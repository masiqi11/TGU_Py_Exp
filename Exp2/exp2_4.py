smoke = input("请输入抽烟的人的姓名，多个人名用空格分割：").split()
drink = input("请输入喝酒的人的姓名，多个人名用空格分割：").split()
print("既抽烟又喝酒的人：" + str(list(set(smoke) & set(drink))))
