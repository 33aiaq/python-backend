text = """
Python is great and Python is easy to learn. Python is also powerful.
"""

words = text.lower().replace('.', '').replace('\n', '').split()

unique_words = set(words)
print("Unique words (using set):")
print(unique_words)

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord frequency (using dictionary):")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
