str1 = "12345"
str2 = "PythonAi"
str3 = "Python Ai"
str4 = "김민아"
str5 = "1234abce"

#숫자만으로 구성되어 있는지 검사
print(f"숫자로만 구성되어 있나요? : {str1.isdigit()}")
print(f"숫자로만 구성되어 있나요? : {str2.isdigit()}")
print(f"숫자로만 구성되어 있나요? : {str5.isdigit()}")

print("-"*30)

#문자로만 구성되어 있는지 검사
print(f"문자로만 구성되어 있나요? : {str1.isalpha()}")
print(f"문자로만 구성되어 있나요? : {str2.isalpha()}")
print(f"문자로만 구성되어 있나요? : {str3.isalpha()}") #공백은 문자로 취급하지 않음 False
print(f"문자로만 구성되어 있나요? : {str4.isalpha()}")
print(f"문자로만 구성되어 있나요? : {str5.isalpha()}")

print("-"*30)

#문자나 숫자로 구성되어 있는지 검사
print(f"숫자나 문자로 구성되어 있나요? : {str1.isalnum()}")
print(f"숫자나 문자로 구성되어 있나요? : {str2.isalnum()}")
print(f"숫자나 문자로 구성되어 있나요? : {str3.isalnum()}")
print(f"숫자나 문자로 구성되어 있나요? : {str4.isalnum()}")
print(f"숫자나 문자로 구성되어 있나요? : {str5.isalnum()}")

print("-"*30)

#문자열이 소문자인지 검사(숫자나 공백이 섞인 것 상관 없이 소문자 알파벳만 확인)
str6 = str2.lower()
str7 = str3.lower()
print(f"소문자로 구성되어 있나요? : {str1.islower()}")
print(f"소문자로 구성되어 있나요? : {str6.islower()}")
print(f"소문자로 구성되어 있나요? : {str7.islower()}")
print(f"소문자로 구성되어 있나요? : {str4.islower()}")
print(f"소문자로 구성되어 있나요? : {str5.islower()}")

print("-"*30)

#문자열이 공백 문자인지
str8 = " "
print(f"문자열이 공백문자인가? : {str8.isspace()}")

print("-"*30)

#단어의 첫 글자가 대문자인지 검사
print(f"단어의 첫 글자가 대문자인가? : {str1.istitle()}")
print(f"단어의 첫 글자가 대문자인가? : {str2.istitle()}") # 첫 단어가 아닌 것이 대문자일 경우 Fals로 나옴
print(f"단어의 첫 글자가 대문자인가? : {str3.istitle()}")
print(f"단어의 첫 글자가 대문자인가? : {str4.istitle()}")
print(f"단어의 첫 글자가 대문자인가? : {str5.istitle()}")

print("-"*30)

#빈자리를 0으로 채우기
str9 = "Hello Python!!!"
str10 = str9.zfill(20)#뒤에 들어가는 숫자는 자리수
print(str9)
print(str10)

