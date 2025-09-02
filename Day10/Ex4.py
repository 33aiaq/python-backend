words = ["apple", "banana", "cherry"]

ascii_dict = {word: {char: ord(char) for char in word} for word in words}

print(ascii_dict)
