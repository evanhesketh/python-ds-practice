def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_list = [*phrase]
    phrase_list.reverse()
    rev_phrase = ''.join(phrase_list)
    return rev_phrase
