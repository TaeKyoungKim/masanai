age = int(input("나이를 입력하세요"))
print(type(age))

# if age<14:
#     print("어린이 ~")
# else:
#     if age >=14 and age<20:
#         print("청소년~!")
#     else:
#         print("어른~!")

# elif를 사용

if age<14:
    print("어린이")
elif age >=14 and age<20:
    print("청소년")
elif age >=20 and age <50:
    print("청년")

else:
    print("노땅!!")
