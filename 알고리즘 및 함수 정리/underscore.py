class ManglingTest():
    def __init__(self):
        self.first = 1
        self.__second = 2

number = ManglingTest()

print(number.first)
#print(number.second)

print(dir(ManglingTest()))


class ManglingTest():

		def __init__(self):
				self.first = 1
				self.second = 2
				self.__third = 3


class Test(ManglingTest):

		def __init__(self):
				self.first = '1'
				self.second = '2'
				self.__third = '3'

number = Test()
print(number.first, number.second,number.__third)