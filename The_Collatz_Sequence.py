import time
print('Please enter a natural number. It will be calculated to 1')
while True:
    try:
        num = int(input('>>'))
    except ValueError:
        print('Please enter a valid Number!')
    else:
        break
def collatz():
    global num
    if num % 2 == 0:
        num = num // 2
        print(num)
    elif num % 2 == 1:
        num = num * 3 + 1
        print(num)
    else:
        print("Please enter a valid number!")


while num != 1:
    collatz()
    time.sleep(0.5)
print("Tadaaaaaa")