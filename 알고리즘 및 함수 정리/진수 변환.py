#진수 변환

#n진수 -> 10진수 int()
print(int('1111',2))
print(int('1111',3))
print(int('1111',4))
print(int('1111',5))
print(int('1111',6))
print(int('1111',7))
print(int('1111',8))
print(int('1111',9))
print(int('1111',16))

#10진수 -> 2, 8, 16진수 bit(), oct(), hex() **string 결과값
print(bin(10))
print(oct(10))
print(hex(10))
#0b1010
#0o12
#0xa

#접두사 없애서 표현 slicing, format() 사용
print(bin(10)[2:])
print(oct(10)[2:])
print(hex(10)[2:])

print(format(10, 'b'))
print(format(10, 'o'))
print(format(10, 'x'))

#1010
#12
#a

#2진수 0으로 채우기 .zfill() 사용
print(format(10, 'b').zfill(10))
#0000001010

#10진수 -> n진수 2, 8, 16 이외 진수 변환
def solution(n, k):
    num_str = ''
    while n > 0:
        n, mod = divmod(n, k)
        num_str += str(mod)

    return num_str[::-1]

print(solution(354, 6))

#n진수 -> n진수    n진수 -> 10진수 -> n진수
print(solution(int('a', 16), 5)) #16진수 a를 5진수로 변경

