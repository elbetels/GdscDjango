# question 1
for i in range(100):
    if i<10:
      print("{:02d}".format(i), end="")
    else:
        print(i, end="")
    if i != 99:
        print(", ", end="")
    else:
        print()

#question 2
char = input("Enter any character: ")
n = int(input("Length of the loop: ")) 

vowels = ['a', 'e', 'i', 'o', 'u']
if len(char)!=1 or char in vowels:
    print("Error: Please enter a consonant.")
else:
 for i in range(1, n*2): 
     if i <= n: 
        print(char*i) 

#question 3
word = input("Enter a word: ")
reverse_word = word[::-1]
if word == reverse_word:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")

#question4
total_sum = 0
count = 0
for num in range(1, 51):
    if num % 2 == 0:
        total_sum += num
        if num % 3 == 0:
            print("Three")
            count += 1
        elif num % 5 == 0:
            print("Five")
            count += 1
        else:
            print(num)

print("Total sum:", total_sum)
print("Count of replaced numbers:", count)