MORSE_CODE_DICT = {

    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',

    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',

    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',

    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',

    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',

    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'

}
string_to_decode1 = '..  .-.. .. -.- .  .--. -.-- - .... --- -.  ...-- .-.-.- .---- ----- '
string_to_decode2 = '..  -.- -. --- .-- --..--  -.-- --- ..-  -.-. .- -.  -.. ---  .. - '

print()
inverse_MORSE_CODE_DICT = {}
for key, val in MORSE_CODE_DICT.items():
    inverse_MORSE_CODE_DICT[val] = key
# print(inverse_MORSE_CODE_DICT)
result_str = ''
list_to_check = string_to_decode1.split('  ')
# print(list_to_check)
for word in list_to_check:
    for letter in word.split():
        result_str += inverse_MORSE_CODE_DICT[letter]
    result_str += ' '
print(result_str)
