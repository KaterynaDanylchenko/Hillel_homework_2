# Завдання 2
# макс 30 балів
# дано код Морзе, що зберігається в словнику
# є стрічка, в якій слова розділені 2 пробілами, а букви в слові - одним пробілом
# написати програму по декодуванню даної (чи подібної) стрічки
# ПІДКАЗКА - при потребі можна створити симетричний словник, де ключами буде код Морзе, а значеннями - символи латиниці


MORSE_CODE_DICT = {

'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',

'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',

'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',

'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',

'6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',

'?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'

}

string_to_decode1 = '.. .-.. .. -.- . .--. -.-- - .... --- -. ...-- .-.-.- .---- ----- '

string_to_decode2 = '.. -.- -. --- .-- --..-- -.-- --- ..- -.-. .- -. -.. --- .. - '

def encryption(message):
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += MORSE_CODE_DICT[myletter] + ' '
      else:
         my_cipher += ' '
      return my_cipher
# This function is used to decrypt
# Morse code to English
def decryption(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for myletter in message:
      # checks for space
      if (myletter != ' '):
         i = 0
         mycitext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
            .values()).index(mycitext)]
            mycitext = ''
   return decipher
def main():
   my_message = "PYTHON-PROGRAM"
   output = encryption(my_message.upper())
   print (output)
   my_message = ".. .-.. .. -.- . .--. -.-- - .... --- -. ...-- .-.-.- .---- -----"
   output = decryption(my_message)
   print (output)
# Executes the main function
if __name__ == '__main__':
   main()