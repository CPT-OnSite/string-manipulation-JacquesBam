"""Write a function concatenate_strings that takes two strings as input and 
returns their concatenation."""
def concatenate_strings(str1, str2):
    concatenated = str1 + str2
    return concatenated


""" Write a function string_length that takes a string as input and returns its length."""
def string_length(string):
    length = len(string)
    return length


"""Write a function string_slice that takes a string and two integers, start and end, 
and returns the slice of the string from start to end."""
def string_slice(string, start, end):
    sliced = string[start:end]
    return sliced


"""Write a function find_substring that takes two strings, main_string and substring, 
and returns the starting index of the first occurrence of substring in main_string.
If substring is not found, return -1."""
def find_substring(main_string, substring):
    position = main_string.find(substring)
    return position


"""Write a function replace_substring that takes three strings, 
main_string, old_substring, and new_substring, and returns a new string
where all occurrences of old_substring in main_string are replaced with new_substring."""
def replace_substring(main_string, old_substring, new_substring):
    main_string = main_string.replace(old_substring, new_substring)
    return main_string


"""Write a function remove_whitespace that takes a string and returns the string
 with all leading and trailing whitespaces removed."""
def remove_whitespace(string):
    string = string.strip(" ")
    return string


"""Write a function string_to_list that takes a string and a delimiter,
and returns a list of substrings split by the delimiter."""
def string_to_list(string, delimiter):
    split_list = string.split(delimiter)
    return split_list


"""Write a function list_to_string that takes a list of strings and a delimiter, 
and returns a single string with the list elements joined by the delimiter."""
def list_to_string(string_list, delimiter):
    string = string_list.join(delimiter)
    return string

"""Write a function is_palindrome that takes a string and returns True if the string
 is a palindrome (reads the same forward and backward) and False otherwise."""
def is_palindrome(string):
    string_backwards = string[::-1].lower()
    if string_backwards == string.lower():
        return True
    else:
        return False
