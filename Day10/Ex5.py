text = "Hello World, this is an example string"

vowels_set = {char.upper() for char in text if char.lower() in "aeiou"}

print(vowels_set)
