# num_a = int(input('값을 입력하세요 :'))
# print()
# num_b = int(input('값을 입력하세요 :'))
# print()
# def abc(num_a,num_b):
#     if num_a < 0 and num_b < 0:
#         print("둘 다 음수")
#     if num_a > 0 and num_b < 0:
#         print("하나만 음수")
#     if num_a < 0 and num_b > 0:
#         print("하나만 음수")
#     if num_a > 0 and num_b > 0:
#         print("둘다 양수")

# abc(num_a,num_b)

# num_a = int(input('값을 입력하세요 :'))
# print()
# num_b = int(input('값을 입력하세요 :'))
# print()
# def abc(num_a,num_b):
#     if num_a == num_b:
#         print("두 수가 같습니다")
#     if num_a > num_b:
#         print("첫번째 수가 두번째 수 보다 큽니다")
#     if num_a < num_b:
#         print("첫번째 수가 두번째 수 보다 작습니다")

# abc(num_a,num_b)

# do = input("::")
# if do == "LOOK":
#     print("모래 독이 있는 도랑에 갇혔습니다.")
#     print("왼쪽(LEFT)나 오른쪽(RIGHT)으로 엉금엉금 기어갑니다.")

#     do = input("::")
#     if do == "LEFT":
#         print("도랑 밖으로 기어 나왔습니다. 배가 있네요!")
#         print("살아 나왔습니다!!")
#     elif do == "RIGHT":
#         print("아 ! 둑을 올라갈 수가 없습니다. 오른쪽 둑은 아주 미끄럽습니다.")
#         print("멀리 미끄러져 내려가 이상한 동굴로 떨어졌습니다.")
#         print("살아남지 못했습니다 :(")
# else:
#         print("대문자로 표시된 동작만 입력해주세요.")
#         print("다시 한번 도전해 보세요 !")     


# cnt = 0
# for a in range(1,100):
#     if a %2 == 0:
#         if a% 6 == 0:
#             cnt +=1
# print(cnt)

# a = int(input("읽을책을 입력하세요: "))
# for a in range(a,0,-1):
#     print(f'파이썬 책{a}권이 들어있는 책장에 파이썬 책이{a}권')
#     print(f'책을 한 권 꺼내 돌려 보고 나니 {a-1}권이 남았네')
#     print()

# a,b,c=int(input("이름을 입력하세요 : ")).split()
# print(f'안녕{a}')
# print(f'안녕{b}')
# print(f'안녕{c}')

# arr = [273,32,103,"문자열", True, False]
# print(arr)

# from csv import list_dialects


# list_a=[1,2,3]
# list_b=[4,5,6]

# print("#리스트")
# print("list_a=",list_a)
# print("list_b=",list_b)
# print()

# print("#리스트 기본 연산자")
# print('list_a + list_b =',list_a,list_b)
# print("list_a*3=",list_a*3)
# print()

# print("#길이 구하기")
# print("len(list_a)",len(list_a))


# n=[273,103,5,32,65,9,72,800,99]
# for i in range(0,9):
#     if n[i]%2==0:
#         print("짝수입니다",n[i])
#     if n[i]%2==1:
#         print("홀수입니다",n[i])


# n=["273","103","5","32","65","9","72","800","99"]
# for i in n:
#         print(i,"는",len(i),"자리입니다")


# l_o_l=[[1,2,3],[4,5,6,7],[8,9]]
# for l_o_l in range():
#     print(l_o_l)


# character = {
#     "name" : "기사",
#     "level" : 12,
#     "items" : {
#         "sword": "불꽃의 검",
#         "armor": "풀플레이트"
#     },
#     "skill" : ["베기","세게 베기", "아주 세게 베기"]
# }
# for key in character:
#     print(key, ":", character[key])
#     print()
    

# def p_time(value, n=2):
#     for i in range(n):
#         print(value)
# p_time("안녕하세요")   


# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3

# list_input_a=[1,2,3,4,5]

# output_a=map(power, list_input_a)
# print("# map() 함수의 실행결과")
# print("map(power, list_input_a):",output_a)
# print("map(power, list_input_a):", list(output_a))
# print()

# output_b=filter(under_3, list_input_a)
# print("# filter() 함수의 실행결과")

# file=open("basic.txt", "w")
# file.write("hello python programming")
# file.close()




# wpr = int(input('문자열을 입력하세요 :'))
# li = ("aeiou")
# ab = ("abcdefghigklmnopqrstuv")
# if pr in li.find('a','e','i','o','u') :
#     print("모든 모음이 들어있습니다")
# elif pr in ab:
#     print("알파벳순입니다 !")





def abc(a,b):
    print(f'{a}더하기{b} = {a+b}')
    print(f'{a}빼기{b} = {a-b}')
    print(f'{a}곱하기{b} = {a*b}')
    print(f'{a}나누기{b} = {a/b}')










