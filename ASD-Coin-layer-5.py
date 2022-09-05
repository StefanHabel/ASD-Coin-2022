#!/usr/bin/env python3
"""
Script that decodes the styling of characters on the inner ring on side A of
the coin.
"""

ciphertext = """
B<strong>GOAMV</strong>OE<strong>I</strong>A<strong>TS</strong>IRL
<strong>NGT</strong>T<strong>NE</strong>O<strong>GRER</strong>GXNT
<strong>EAI</strong>F<strong>C</strong>ECA<strong>IE</strong>O
<strong>AL</strong>EK<strong>FN</strong>R<strong>5L</strong>WE
<strong>FCHDE</strong>EA<strong>EE</strong>E<strong>7N</strong>MD
<strong>RX</strong>X<strong>5</strong>
""".replace('\n', '')

hint = 'Binary numbers -- https://en.wikipedia.org/wiki/Binary_number'


import html.parser

class StyleToBinaryCharactersHTMLParser(html.parser.HTMLParser):

    def __init__(self, *args, **kwargs):
        super(StyleToBinaryCharactersHTMLParser, self).__init__(*args, **kwargs)

        self.binary_characters = ''
        self.binary_character = '1'

        # The rest is for display/debug purposes
        self.styled_ciphertext = ''
        self.text_style_characters = ' '
        self.text_styles = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'u':
            self.binary_character = ' '

            self.text_style_characters = ' '
        elif tag == 'strong':
            self.binary_character = '0'

            self.styled_ciphertext += '\033[1m'
            self.text_style_characters = '\033[1mS\033[0m'

    def handle_endtag(self, tag):
        self.binary_character = '1'

        if self.binary_character == '0':
            self.styled_ciphertext += '\033[0m'
            self.text_style_characters = ' '

    def handle_data(self, data):
        self.binary_characters += self.binary_character * len(data)

        self.styled_ciphertext += data
        self.text_styles += self.text_style_characters * len(data)


parser = StyleToBinaryCharactersHTMLParser()
parser.feed(ciphertext)

# Split the overall 70-character binary code into 10 words of 7 characters each
N = len(parser.binary_characters)
NUM_WORDS = 10
STEP = N // NUM_WORDS
binary_texts = [parser.binary_characters[i:i + STEP]
                for i in range(0, N, STEP)]

# Convert the 10 binary codes into 10 integer numbers
import ast
BIN_PREFIX = '0b'
integers = [ast.literal_eval(BIN_PREFIX + binary_text)
            for binary_text in binary_texts]

# Convert the 10 integer numbers to Unicode strings of one character
characters = [chr(integer) for integer in integers]

# Build the resulting plaintext from the generated characters
plaintext = ''.join(characters)


print('Ciphertext: {}'.format(parser.styled_ciphertext))
print('    Styles: {}'.format(parser.text_styles))
print('      Hint: {}'.format(hint))
print('    Binary: {}'.format(parser.binary_characters))
print('            {}'.format('^      ' * NUM_WORDS))
print(' Plaintext: {}'.format(plaintext))

"""
Ciphertext: BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5
    Styles:  SSSSS  S SS   SSS SS SSSS    SSS S   SS SS  SS SS  SSSSS  SS SS  SS S
      Hint: Binary numbers -- https://en.wikipedia.org/wiki/Binary_number
    Binary: 1000001101001110001001000011110001011100100110010011000001100100110010
            ^      ^      ^      ^      ^      ^      ^      ^      ^      ^      
 Plaintext: ASDCbr2022
"""
