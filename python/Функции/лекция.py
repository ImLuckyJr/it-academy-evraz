# def helloWorld():
#     for i in range(6):
#         print('Hello world')
#
# # helloWorld()
#
# print(helloWorld())

a = 10
b = 20

def multipleDigits(d1 = 50, d2 = 100):
    a = d1 * d2
    return d1 * d2

c = multipleDigits(d2 = 8) + a + b
print(c)
