
field_size = int(input())
apple_num = int(input())
apple_location1,apple_location2 = map(int, input().split())

for i in range(len(apple_num)):
    li = [map(int, input().split()) for i in range(2)]
array=[[0 for col in range(field_size)]for row in range(field_size)]
print(li)
class bamm:
    def __init__(self, start):
        self.start = start
    

print(apple_location1, apple_location2)
bam=bamm("*")
array[0][0]=bam.start
#for i in 
print(array)


