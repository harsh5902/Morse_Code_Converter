# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...',
                   'T': '-', 'U': '..-', 'V': '...-',
                   'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                   '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
                   ' ': ' / '
}


def morse_code_converter(text):
    text_list = list(text)
    morse_code = ''
    morse_code_list = []
    for letter in text_list:
        morse_code_list.append(MORSE_CODE_DICT[letter])
    morse_code = morse_code.join(morse_code_list)
    return morse_code


input_text = input('\nEnter the input test here:\n').upper()

print('\nMorse Code:\n', morse_code_converter(input_text))


