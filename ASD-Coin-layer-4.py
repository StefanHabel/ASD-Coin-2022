#!/usr/bin/env python3
"""
Script that decodes the styling of characters on the outer ring on side A of
the coin.
"""

ciphertext = """
<u>.</u><strong>D</strong>VZIV<u>Z</u>FWZX<strong>R</strong><u>L</u>
<strong>FHRM</strong>X<u>L</u>MX<strong>VKG</strong><u>ZM</u>W
<strong>NV</strong><u>G</u><strong>RXF</strong><u>O</u>L<strong>FHR</strong>
<u>M</u><strong>V</strong>C<u>V</u><strong>X</strong>F<strong>GR</strong>
<u>L</u>M<strong>.UR</strong><u>M</u><strong>W</strong><u>X</u>
<strong>O</strong>Z<strong>I</strong><u>R</u>G<u>B</u><strong>R</strong>M7
<strong>D</strong><u>R</u><strong>W</strong>G<u>S</u><strong>C</strong>5
<strong>W</strong><u>V</u>K<strong>G</strong>S
""".replace('\n', '')

hint = 'Morse code -- https://en.wikipedia.org/wiki/Morse_code'


DIT = '·'
DAH = '−'
PAUSE = ' '

MORSE_CODE = {
    # Letters
    'A': '·−',    'B': '−···',  'C': '−·−·',  'D': '−··',   'E': '·',
    'F': '··−·',  'G': '−−·',   'H': '····',  'I': '··',    'J': '·−−−',
    'K': '−·−',   'L': '·−··',  'M': '−−',    'N': '−·',    'O': '−−−',
    'P': '·−−·',  'Q': '−−·−',  'R': '·−·',   'S': '···',   'T': '−',
    'U': '··−',   'V': '···−',  'W': '·−−',   'X': '−··−',  'Y': '−·−−',
    'Z': '−−··',

    # Numbers
    '1': '·−−−−', '2': '··−−−', '3': '···−−', '4': '····−', '5': '·····',
    '6': '−····', '7': '−−···', '8': '−−−··', '9': '−−−−·', '0': '−−−−−',
}

REVERSE_MORSE_CODE = {morse_code: character
                      for character, morse_code in MORSE_CODE.items()}

import html.parser

class StyleToMorseCodeHTMLParser(html.parser.HTMLParser):

    def __init__(self, *args, **kwargs):
        super(StyleToMorseCodeHTMLParser, self).__init__(*args, **kwargs)

        self.morse_code = ''
        self.current_morse_code_characters = DAH

        # The rest is for display/debug purposes
        self.current_text_style_characters = ' '
        self.text_styles = ''
        self.styled_ciphertext = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'strong':
            self.current_morse_code_characters = DIT

            self.current_text_style_characters = '\033[1mS\033[0m'
            self.styled_ciphertext += '\033[1m'
        elif tag == 'u':
            self.current_morse_code_characters = PAUSE

            self.current_text_style_characters = '\033[4m_\033[0m'
            self.styled_ciphertext += '\033[4m'

    def handle_endtag(self, tag):
        self.current_morse_code_characters = DAH

        self.current_text_style_characters = ' '
        self.styled_ciphertext += '\033[0m'

    def handle_data(self, data):
        self.morse_code += self.current_morse_code_characters * len(data)

        self.text_styles += self.current_text_style_characters * len(data)
        self.styled_ciphertext += data


parser = StyleToMorseCodeHTMLParser()
parser.feed(ciphertext)

# Generate the plain text by replacing sequences of characters that represent
# morse code with their equivalent characters
morse_codes = parser.morse_code.replace(' ', '|').split('|')
plaintext = ''.join(REVERSE_MORSE_CODE.get(morse_code, ' ')
                    for morse_code in morse_codes)


print('Ciphertext: {}'.format(parser.styled_ciphertext))
print('    Styles: {}'.format(parser.text_styles))
print('      Hint: {}'.format(hint))
print('     Morse: {}'.format(parser.morse_code))
print(' Plaintext: {}'.format(plaintext))

"""
Ciphertext: .DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS
    Styles: _S    _    S_SSSS _  SSS__ SS_SSS_ SSS_S _S SS_ SSS_S_S S_ _S  S_S _S S_ S 
      Hint: Morse code -- https://en.wikipedia.org/wiki/Morse_code
     Morse:  ·−−−− −−−−· ····− −−···  −·· ··· −··· ·− ·−·· −··· · ·−· − ·−−· ·− ·−· −·−
 Plaintext:  1947 DSBALBERTPARK
"""
