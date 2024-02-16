def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers and words
    words_dict = {}
    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            number, word = int(parts[0]), parts[1]
            words_dict[number] = word

    # Sort the numbers and construct the decoded message
    sorted_numbers = sorted(words_dict.keys())
    decoded_message = ' '.join(words_dict[number] for number in sorted_numbers)

    return decoded_message

# Example usage
message_file_path = 'your_file.txt'  # Replace with the actual file path
decoded_message = decode(message_file_path)
print(decoded_message)
