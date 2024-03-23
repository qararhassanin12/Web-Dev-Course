def spell_check(input_text, wordlist):
    words = input_text.split()
    misspelled_words = []

    for word in words:
        # Remove punctuation from the word
        word = word.strip('.,?!()[]{}:;"\'')
        
        # Check if the lowercase version of the word is in the wordlist
        if word.lower() not in wordlist:
            misspelled_words.append(word)

    return misspelled_words

def main():
    # Example wordlist
    example_wordlist = set(['example', 'word', 'list', 'for', 'spell', 'checking'])

    # Get user input
    user_input = input("Enter a string: ")

    # Perform spell check
    misspelled_words = spell_check(user_input, example_wordlist)

    # Print results
    if misspelled_words:
        print("Misspelled words:")
        for word in misspelled_words:
            print("- " + word)
    else:
        print("No misspelled words found.")

if __name__ == "__main__":
    main()
