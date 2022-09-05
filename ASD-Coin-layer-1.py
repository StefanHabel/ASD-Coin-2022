#!/usr/bin/env python3
"""
Script that decodes the outer ring of characters on side A of the coin.
"""

ciphertext = """
.DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS
""".strip()

hint = 'ATBASH -- https://en.wikipedia.org/wiki/Atbash'


"""
Atbash substitution cipher:
Plaintext   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext  Z Y X W V U T S R Q P O N M L K J I H G F E D C B A
"""

import string
ATBASH = {character: substitute
          for character, substitute in zip(string.ascii_uppercase,
                                           reversed(string.ascii_uppercase))}

plaintext = ''.join(ATBASH.get(character, character)
                    for character in ciphertext)


print('Ciphertext: {}'.format(ciphertext))
print('      Hint: {}'.format(hint))
print(' Plaintext: {}'.format(plaintext))

"""
Ciphertext: .DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS
      Hint: ATBASH -- https://en.wikipedia.org/wiki/Atbash
 Plaintext: .WEAREAUDACIOUSINCONCEPTANDMETICULOUSINEXECUTION.FINDCLARITYIN7WIDTHX5DEPTH

WE ARE AUDACIOUS IN CONCEPT AND METICULOUS IN EXECUTION
FIND CLARITY IN 7 WIDTH X 5 DEPTH
"""
