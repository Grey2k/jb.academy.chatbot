# put your python code here
group_1 = int(input())
group_2 = int(input())
group_3 = int(input())

group_1 = group_1 if group_1 % 2 == 0 else group_1 + 1
group_2 = group_2 if group_2 % 2 == 0 else group_2 + 1
group_3 = group_3 if group_3 % 2 == 0 else group_3 + 1

print((group_1 + group_2 + group_3) // 2)
