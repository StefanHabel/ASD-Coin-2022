#!/usr/bin/env python3
"""
Script that decodes the hexadecimal characters on side A of the coin.
"""

ciphertext = """
E3B
8287D4
290F723381
4D7A47A291DC
0F71B2806D1A53B
311CC4B97A0E1CC2B9
3B31068593332F10C6A335
2F14D1B27A3514D6F7382F1A
D0B0322955D1B83D3801CDB2
287D05C0B82A311085A03329
1D85A3323855D6BC333119D
6FB7A3C11C4A72E3C17CCB
B33290C85B6343955CCBA3
B3A1CCBB62E341ACBF72
E3255CAA73F2F14D1B27A
341B85A3323855D6BB33
3055C4A53F3C55C7B22
E2A10C0B97A291DC0F
73E3413C3BE392819
D1F73B331185A33
23855CCBA2A3
206D6BE383
1108B
""".replace('\n', '')

hint = 'XOR HEX A5D75'


KEY = 'A5D75'


# Build a key text that matches the length of the ciphertext by repeating the
# characters of the given key
import itertools
key_cycle = itertools.cycle(KEY)
key_text = ''.join(next(key_cycle)
                   for _ in ciphertext)

# Convert the hexademical ciphertext and key text to numeric values
import ast
HEX_PREFIX = '0x'
cipher_number = ast.literal_eval(HEX_PREFIX + ciphertext)
key_number = ast.literal_eval(HEX_PREFIX + key_text)

# XOR the cipher number with the key number
plaintext_number = cipher_number ^ key_number

# Convert the plaintext number to hexademical text, removing the '0x' prefix
plaintext_hex = hex(plaintext_number)[len(HEX_PREFIX):]

# Build a list of pairs of hexademical characters
hex_codes = [plaintext_hex[i:i + 2]
             for i in range(0, len(plaintext_hex), 2)]

# Convert the pairs of hexademical characters to integer numbers
integers = [int(hex_code, 16) for hex_code in hex_codes]

# Convert the integer numbers to Unicode strings of one character
characters = [chr(integer) for integer in integers]

# Build the resulting plaintext from the generated characters
plaintext = ''.join(characters)


print('Ciphertext: {}'.format(ciphertext))
print('      Hint: {}'.format(hint))
print('       Key: {}'.format(KEY))
print(' Plaintext: {}'.format(plaintext))

"""
Ciphertext: E3B8287D4290F7233814D7A47A291DC0F71B2806D1A53B311CC4B97A0E1CC2B93B31068593332F10C6A3352F14D1B27A3514D6F7382F1AD0B0322955D1B83D3801CDB2287D05C0B82A311085A033291D85A3323855D6BC333119D6FB7A3C11C4A72E3C17CCBB33290C85B6343955CCBA3B3A1CCBB62E341ACBF72E3255CAA73F2F14D1B27A341B85A3323855D6BB333055C4A53F3C55C7B22E2A10C0B97A291DC0F73E3413C3BE392819D1F73B331185A3323855CCBA2A3206D6BE3831108B
      Hint: XOR HEX A5D75
       Key: A5D75
 Plaintext: For 75 years the Australian Signals Directorate has brought together people with the skills, adaptability and imagination to operate in the slim area between the difficult and the impossible.
"""
