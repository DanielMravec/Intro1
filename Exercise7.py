list = [1, 2, 3, 4, 5]

num = int(input("Give me a number : "))

output = 0

for i in list:
  if num > i:
    output += 1


print(output)