#for loop
# for keyword, loop variable, in, sequence

names = {"Alice", "Bob", "Charlie", "David"}
for name in names:
    print(name)

sentence = "Hello World"
for character in sentence:
    if character.isalpha():
        print(character)

for number in range(1, 6):
    print(number)

#challenge
numbers = [12, 45, 6, 72, 21, 8, 94, 57]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("The maximum value in the list is: ", maximum)