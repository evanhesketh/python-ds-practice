def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    no_spaces = []
    split_phrase = [*phrase]
    for char in split_phrase:
        if char != ' ':
            no_spaces.append(char.lower())


    replica = no_spaces.copy()

    replica.reverse()
    return replica == no_spaces


