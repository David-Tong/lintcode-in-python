import string


class Solution:
    """
    @param c: A character.
    @return: The character is alphanumeric or not.
    """
    def is_alphanumeric(self, c):
        # write your code here
        import string
        if c in string.ascii_lowercase or c in string.ascii_uppercase:
            return True
        elif c in string.digits:
            return True
        else:
            return False