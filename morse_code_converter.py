MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    }


ENGLISH_DICT = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '--..--': ', ',
    '.-.-.-': '.',
    '..--..': '?',
    '-..-.': '/',
    '-....-': '-',
    '-.--.': '(',
    '-.--.-': ')',
    }




def encrypt(text):
    cipher_text =''
    for letter in text:
        if letter in MORSE_CODE_DICT:
            cipher_text += MORSE_CODE_DICT[letter] + ' '
    print(f'The encoded text is: {cipher_text}')


def decrypt(text):
    morse_code_words = text.split(' / ')
    plain_text = ''

    for morse_word in morse_code_words:
        morse_characters = morse_word.split(' ')
        for char in morse_characters:
            if char in ENGLISH_DICT:
                plain_text += ENGLISH_DICT[char]
            else:
                plain_text += ' '  
        plain_text += ' '
    print(f'The decoded text is: {plain_text}')


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

if direction == 'decode':
    print('Remember to insert space after each morse character')

text = input("Type your message:\n").upper()


if direction == 'encode':
    encrypt(text)
elif direction == 'decode':
    decrypt(text)
else:
    print("Try again")
