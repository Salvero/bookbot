def main():
    # Specify the relative path to the file
    path_to_file = 'books/frankenstein.txt'
    
    # Use a with block to open and read the file
    with open(path_to_file) as f:
        file_contents = f.read()

    # Split the file contents into words and count them
    words = file_contents.split()
    word_count = len(words)    
    
    # Print the contents of the file
    print(file_contents)

    # Print the number of words
    print(f"The book contains {word_count} words.")    

def count_characters(text):
    # Convert the entire string to lowercase
    text = text.lower()

    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate over each character in the string
    for char in text:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            char_count[char] = 1

    return char_count

def count_characters(text):
    # Convert the entire string to lowercase
    text = text.lower()

    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate over each character in the string
    for char in text:
        # Only count alphabetic characters
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def sort_on(dict_item):
    return dict_item["num"]

def sort_character_counts(char_count):
    # Convert the character count dictionary to a list of dictionaries
    char_list = [{"char": k, "num": v} for k, v in char_count.items()]

    # Sort the list by the "num" key in descending order
    char_list.sort(reverse=True, key=sort_on)

    return char_list

# Example usage
text = "FOR FRODO"
character_counts = count_characters(text)
sorted_character_counts = sort_character_counts(character_counts)

print(sorted_character_counts)

# Example usage
text = "FOR FRODO"
character_counts = count_characters(text)
print(character_counts)


# Call the main function to execute the program
if __name__ == "__main__":
    main()
