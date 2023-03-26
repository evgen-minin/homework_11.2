def changes_letter_case(text):
    """
    comment
    :param text:
    :return:
    """
    return text.upper()

print(changes_letter_case("hello skypro"))


def changes_letter_case_2(text):
    """
    comment
    :param text:
    :return:
    """
    return ' '.join(map(lambda x: x.capitalize(), text.split(' ')))

print(changes_letter_case_2("hello skypro"))
