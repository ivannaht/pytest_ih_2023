def integer_boolean(binary_number):
    list_in = [int(d) for d in str(binary_number)]
    new_list = []
    for num in list_in:
        if num == 1:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list


if __name__ == "__main__":
    print(integer_boolean(11001))


def count_vowels(word):
    vowels = ['a', "e", "i", "o", "u"]
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1

    return count


if __name__ == "__main__":
    print(count_vowels("word wide web"))


def binary(decimal):
    digits = "0123456789"
    rem_list = []
    new_string = ""
    if decimal == 0:

        return '0'
    else:
        while decimal > 0:
            rem = decimal % 2
            rem_list.append(rem)
            decimal = decimal // 2
        while not len(rem_list) == 0:
            new_string = new_string + digits[rem_list.pop()]

        return new_string


if __name__ == "__main__":
    print(binary(5))


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = []
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.append(rem)
        dec_number = dec_number // base
    new_string = ""
    while not len(rem_stack) == 0:
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


if __name__ == "__main__":
    print(base_converter(25,2))


def mean(number):
    total = 0
    list_in = [int(d) for d in str(number)]
    for num in list_in:
        total = total + num
    return round(total/len(list_in))


if __name__ == "__main__":
    print(mean(512))


def is_isogram(word):
    lowercase_word = word.lower()
    letters_list = []
    for letter in lowercase_word:
        if letter.isalpha():
            if letter in letters_list:
                return False
            letters_list.append(letter)

    return True


if __name__ == '__main__':
    print(is_isogram("Man"))
    print(is_isogram("Maya"))
