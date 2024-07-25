import re

test = "hello [2023/04] welcome"

#괄호 내부 내용만 추출
p = re.compile('\[([^]]+)\]')
m = p.findall(test)
print(m)