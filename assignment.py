# This is the end of my beginning
while True:
    print("Choose an operation: \n1. Reverse the sentence\n2. Count vowels"
          "\n3. Check if palindrome\n4. Find and replace a word"
          "\n5. Format (title case)\n6. Split into words"
          "\n7. Word frequency counter\n8. Swap case\n9. Exit")

    choosen = input("Enter your choice: ")


    if choosen == "1":
        sentence = input("Enter sentence: ")
        reverseSentence = sentence[::-1]
        print("Reversed sentence:", reverseSentence)


    elif choosen == "2":
        sentence = input("Enter sentence: ")
        vowels = "aeiouAEIOU"
        count = 0
        for char in sentence:
            if char in vowels:
                count += 1
        print("Counted vowels:", count)


    elif choosen == "3":
        sentence = input("Enter sentence: ")
        clean = sentence.replace(" ", "").lower()
        if clean == clean[::-1]:
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")


    elif choosen == "4":
        sentence = input("Enter sentence: ")
        old = input("Enter the word to find: ")
        new = input("Enter the word to replace: ")
        updated_sentence = sentence.replace(old, new)
        print("Updated sentence:", updated_sentence)


    elif choosen == "5":
        sentence = input("Enter sentence: ")
        print("Title case:", sentence.title())

    elif choosen == "6":
        sentence = input("Enter sentence: ")
        words = sentence.split()
        print("Words:", words)

    elif choosen == "7":
        sentence = input("Enter sentence: ")
        words = sentence.lower () .split()
        freq = {}
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
        print("Words frequency:", freq)

    elif choosen == "8":
        sentence = input("Enter sentence: ")
        print("Swap case:", sentence.swapcase())


    elif choosen == "9":
        print("Daghang Salamat Babay :)!")
        break


    else:
        print("Mali Boss 1 to 8 lng pilia")



