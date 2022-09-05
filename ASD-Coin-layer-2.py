#!/usr/bin/env python3
"""
Script that decodes the inner ring of characters on side A of the coin.
"""

ciphertext = """
BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5
""".strip()

hint = 'FIND CLARITY IN 7 WIDTH X 5 DEPTH'


WIDTH = 7
DEPTH = 5
X = WIDTH * DEPTH

"""
Analyzing the ciphertext visually:

     B      E      L      O      N      E      L      L      E      N
      G      I      N      G      T      C      E      W      E      M
       O      A      G      R      E      A      K      E      A      D
        A      T      T      E      A      I      F      F      E      R
         M      S      T      R      I      E      N      C      E      X
          V      I      N      G      F      O      R      H      E      X
           O      R      E      X      C      A      5      D      7      5

       B      E      L      O      N         E      L      L      E      N
       G      I      N      G      T         C      E      W      E      M
       O      A      G      R      E         A      K      E      A      D
       A      T      T      E      A         I      F      F      E      R
       M      S      T      R      I         E      N      C      E      X
       V      I      N      G      F         O      R      H      E      X
       O      R      E      X      C         A      5      D      7      5

                   BELON                                 ELLEN
                   GING T                                CE WE M
                   O A GRE                               AKE A D
                   AT TEA                                IFFER
                   M STRI                                ENCE X
                   VING F                                OR HEX
                   OR EXC                                A5D75
"""

def decode(letters):
    result = []
    N = len(letters)
    for i in range(WIDTH):
        for n in range(0, N, WIDTH):
            result.append(letters[i + n])
    return result

plaintext = ''.join(decode(ciphertext[:X]) +
                    decode(ciphertext[X:]))


print('Ciphertext: {}'.format(ciphertext))
print('      Hint: {}'.format(hint))
print(' Plaintext: {}'.format(plaintext))

"""
Ciphertext: BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5
      Hint: FIND CLARITY IN 7 WIDTH X 5 DEPTH
 Plaintext: BELONGINGTOAGREATTEAMSTRIVINGFOREXCELLENCEWEMAKEADIFFERENCEXORHEXA5D75

BELONGING TO A GREAT TEAM STRIVING FOR EXCELLENCE WE MAKE A DIFFERENCE
XOR HEX A5D75
"""
