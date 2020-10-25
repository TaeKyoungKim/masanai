# number = [1,2,3,4,5,6,7]

# for a in number:
#     b = a *10
#     print(b)

number = [1, 2, 3, 4]
dan = [2,3,4,5,6,7,8,9]


# for i in dan:
#     if i ==3:
#         continue
#     for j in number:
#         print(i,'*', j ,' = ', i*j)
#         # print('{} * {} = {}'.format(i , j ,i*j))
#         # print('%d' %(i*j))

def hello(name , location):
    print("{}에 계신 {}님 안녕하세요 ".format(location , name))
    return 1 , 2

data = hello("김태경","마산")
# hello("창원")
print(data)
    