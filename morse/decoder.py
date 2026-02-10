from morse.mapping import MORSE


# ters sözlük: morse -> harf
REVERSE_MORSE = {v: k for k, v in MORSE.items()}

def decode_word(word):
    """
    Decodes a single Morse word (letters separated by space).
    """

    letters = []

    for symbol in word.split():
        if symbol in REVERSE_MORSE:
            letters.append(REVERSE_MORSE[symbol])

    return "".join(letters)


def decode(code):
    """
    Decodes the given Morse code into text.
    Words are separated by a pipe (|) and letters by a space.
    """

    words = code.split("|")
    decoded_words = []

    for w in words:
        letters = []

        for symbol in w.split():
            if symbol in REVERSE_MORSE:
                letters.append(REVERSE_MORSE[symbol])

        decoded_words.append("".join(letters))

    return " ".join(decoded_words)


if __name__ == "__main__":

    from morse.encoder import encode

    text = "abc ABC"
    encoded = encode(text)
    decoded = decode(encoded)

    print("Original:", text.upper())
    print("Encoded :", encoded)
    print("Decoded :", decoded)
