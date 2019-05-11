def change_case(list, upper):
    """
    Change strings in list into upper or lower case.

    Args:
        list: List of strings.
        upper: Boolean indicating whether case should be upper or lower.

    Returns:
        List with changed case.
    """
    return [item.upper() if upper else item.lower() for item in list]


def word_count(sentence):
    """
    Create dictionary of words as keys and number of their occurrences as values.

    Args:
        sentence: String.

    Returns:
        Dictionary with occurrences of words.
    """
    num_of_words = {}
    sanitized_sentence = sentence.replace(",", " ").replace(".", " ")
    for word in sanitized_sentence.split():
        if word not in num_of_words:
            num_of_words[word] = 1
        else:
            num_of_words[word] += 1
    return num_of_words


def no_special_chars(text):
    """
    Remove special characters from text.
    """
    for character in ['@', '#', '$', '%', '^', '&', '*', '+', '<', '>', '~']:
        if character in text:
            text = text.replace(character, '')
    return text


def word_to_num(text):
    """
    Assign unique number to every unique word in text.

    Args:
        text: String.

    Returns:
        Dictionary with unique words as keys and unique numbers as values.
    """
    words_as_nums = {}
    sanitized_text = text.replace(",", "").replace(".", "")
    number = 0
    for word in sanitized_text.split():
        if word not in words_as_nums:
            words_as_nums[word] = number
            number += 1
        else:
            continue
    return words_as_nums


def no_polish_chars(text):
    """
    Replaces polish characters in text with english alphabet letters.
    """
    polish_chars = ['Ą', 'ą', 'Ć', 'ć', 'Ę', 'ę', 'Ó', 'ó', 'Ł', 'ł', 'Ń', 'ń', 'Ś', 'ś', 'Ź', 'ź', 'Ż', 'ż']
    non_polish_chars = ['A', 'a', 'C', 'c', 'E', 'e', 'O', 'o', 'L', 'l', 'N', 'n', 'S', 's', 'Z', 'z', 'Z', 'z']
    chars_tuples = list(zip(polish_chars, non_polish_chars))
    chars_dict = dict(chars_tuples)

    for key, value in chars_dict.items():
        if key in text:
            text = text.replace(key, value)
        else:
            continue
    return text
