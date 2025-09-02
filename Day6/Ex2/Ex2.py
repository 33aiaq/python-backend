def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def palindrome_checker(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            words = infile.readlines()

        palindromes = []

        for word in words:
            clean_word = word.strip()
            if clean_word and is_palindrome(clean_word):
                palindromes.append(clean_word.upper())

        with open(output_file, 'w') as outfile:
            for palindrome in palindromes:
                outfile.write(palindrome + '\n')

        print(f"Palindromes written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

palindrome_checker("input_words.txt", "palindromes.txt")
