import re

example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'
print(re.findall(r'\d.+년', example1))
# 숫자(\d)로 시작하고 어떤 문자든(.) 반복(+)되며 '년'으로 끝나는 문자열을 반환
print(re.findall(r'\d.+?년', example1))
# '년'이라는 글자를 찾으면 패턴 찾기를 멈춤
print(re.findall(r'\d+.년', example1))
# 숫자를 반복시킨 후 '년'으로 끝나는 문자를 찾아도 됨

print('--------------------')
data = '010-1234-1234 011-1234-1234 010-123-1234 012-1234-1234 014-adf-1234 110-123-1234 011-12d-2193 010 222 5555 01033336666'
print(re.findall(r'\d{3}-\w{3,4}-\d{4}', data))
print(re.findall(r'\d{3} \d{3} \d{4}', data))
print(re.findall(r'\d{11}', data))

print('--------------------')
data = '010QEFX 011EFds 012$DF@ 014d123 010DA1234 012AEFD'
print(re.findall(r'01[012][A-Z]{2,4}', data))

print('--------------------')
data = '010-1234-1234 010 222 5555 01033336666 010AS 011GDWE 012QWEX a2F1b A3A0'
print(re.findall(r'[aA]\w{3}[bB]?', data))