import string


def scramble_words(words):

    func_input = words.split()
    list_len = len(func_input)

    for idx in range(list_len):
        idx_count = 0  # This tracks the index of characters within words
        punc = {}

        # Check for punctuation and store location in the dictionary
        for char in func_input[idx]:
            if char in string.punctuation:
                punc[idx_count] = char
            idx_count += 1

        idx_count = 0  # Reset

        # Search again;  this time delete the punctuation
        for char in func_input[idx]:
            if char in string.punctuation:
                func_input[idx] = func_input[idx][:idx_count] + func_input[idx][idx_count + 1:]
            else:
                idx_count += 1

        # Sort the inside letters by alphabetical order;  ignore single characters
        if len(func_input[idx]) > 1:
            func_input[idx] = func_input[idx][0] + ''.join(sorted(func_input[idx][1:-1])) + func_input[idx][-1]

        # Add the punctuation back into its place
        for key in punc:
            func_input[idx] = func_input[idx][:key] + punc[key] + func_input[idx][key:]

    return ' '.join(func_input)


print(scramble_words(input("Enter text to scramble: ")))