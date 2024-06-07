# morse.py

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', ':': '---...', ';': '-.-.-.', '?': '..--..', '!': '-.-.--', '-': '-....-',
    ' ': '\t'
}

def encode(text):
    encoded_text = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            encoded_text += MORSE_CODE_DICT[char] + ' '
        else:
            encoded_text += char
    return encoded_text.strip()

def decode(encoded_text):
    decoded_text = ''
    encoded_chars = encoded_text.split()
    for char in encoded_chars:
        for key, value in MORSE_CODE_DICT.items():
            if char == value:
                decoded_text += key
    return decoded_text