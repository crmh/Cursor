from string import ascii_lowercase, ascii_uppercase


def _shift_table(alphabet: str, offset: int) -> str:
    n = len(alphabet)
    return alphabet[offset % n :] + alphabet[: offset % n]


_LOWER = ascii_lowercase
_UPPER = ascii_uppercase
_TRANSLATE = str.maketrans(
    _LOWER + _UPPER,
    _shift_table(_LOWER, 1) + _shift_table(_UPPER, 1),
)


def caesar_cipher(text: str) -> str:
    """Return *text* encrypted with a Caesar cipher (shift of 1).

    Letters are shifted within their alphabet; case and non-letters are preserved.
    """
    return text.translate(_TRANSLATE)
