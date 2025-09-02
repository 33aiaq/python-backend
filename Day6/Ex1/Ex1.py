def count_word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()

        import string
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator).lower()

        words = cleaned_text.split()
        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        return frequency

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = 'sample.txt'
freq = count_word_frequency(filename)

if freq:
    print("Word Frequencies:")
    for word, count in sorted(freq.items()):
        print(f"{word}: {count}")
