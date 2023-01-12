# a = 8
# for i in range(a):
#     print(" " * (a-i+1), end="")
#     print('*' * (i+1))


# a = 8
# for i in range(a):
#     print(" " * (a), end="")
#     print('*' * (a))


# a = 8
# for i in range(a):
#     print('*' * (i))
#     print(" " * (a+1), end="")


# a=11

# for i in range(a//2):	
    # print(' ' * (a//2-i), end='')
    # print('*' * (2*i+1))
    
# for i in range(a//2-1):
#     print(' ' * (i+2), end='')
#     print('*' * ((a//2*2)-3-2*i))


# for i in range(a-1):
#     print(' ' * (a-i+2), end='')
#     print('*' * ((a)-i))


# a = [[10,20],[30,40],[50,60]]
# for i in a:
#     for j in i:
#         print(j, end='')
#         print()

#int(input('입력하세요'))
# for sum in range(1,10):
#     for k in range(2,10):
#         print(f'{k} * {sum} = {k * sum : 2d} ')
#     print()

# num = int(input('입력하세요: '))
# for sum in range(1,10):
#     print(f'{num} * {sum} = {num*sum:2d}')



# a = int(input('분을 입력하세요. :'))
# b = a//60
# c = a%60
# print(f'{b}시간{c}분')


# f = 75
# c = (f-32)/1.8
# print(f'{c}')

# a = 5
# b = (5/0.62137)
# c = (b * 1000)
# print(f'{a}')
# print('마일')
# print(f'{b}')
# print('킬로미터')
# print(f'{c}')
# print('미터')

a = "Eat Work Play Sleep repeat"
b=a.find("Work")
c=a.find("Play")
q=b.replace('Work')
w=c.replace('Play')

print(f'{q}ing')
print(f'{w}ing')
