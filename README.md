# ASD-Coin-2022
Solutions decoding cryptographic code of the Australian Signals Directorate's 75th anniversary coin.

| :grey_exclamation: This repository contains SPOILERS |
|------------------------------------------------------|

Background
---
> On 1 September 2022, the Royal Australian Mint released a limited edition 50 cent commemorative coin to celebrate the Australian Signals Directorate's (ASD) 75th anniversary. [...]
>
> In tribute to the importance of code breaking and evolution of signals intelligence, mulitple [sic] layers of cryptographic code have been included in the design of the coin. ASD cryptographic experts collaborated with the Royal Australian Mint to design the coins unique and enigmatic code. A hidden message will be revealed once each layer of code has been cracked. All that is needed is a pen, paper, Wikipedia and brainpower. [...]

Source: https://www.asd.gov.au/75th-anniversary/events/2022-09-01-75th-anniversary-commemorative-coin

Acknowledgements
---
The approaches of decoding the coin's cryptographic codes in Python scripts
in this repository are based on findings<br>
**James Newburrie** (@DifficultNerd)
shared in a Twitter thread the same day the coin was released:
> Solved the ASD coin. 
>
> Do you want spoilers?

Source: https://twitter.com/DifficultNerd/status/1565587468703137792

The HTML text used as ciphertext in this repository was copied from
the **Accessible text version** section of the webpage describing
the coin on the ASD website, which looked similar to the following:
> Side A outer ring<br>
> ~.~**D**VZIV~Z~FWZX**R**~L~**FHRM**X~L~MX**VKG**~ZM~W**NV**~G~**RXF**~O~L**FHR**~M~**V**C~V~**X**F**GR**~L~M.**UR**~M~**W**~X~**O**Z**I**~R~G~B~**R**M7**D**~R~**W**G~S~**C**5**W**~V~K**G**S
>
> Side A inner ring<br>
> B**GOAMV**OE**I**A**TS**IRL**NGT**T**NE**O**GRER**GXNT**EAI**F**C**ECA**IE**O**AL**EK**FN**R**5L**WE**FCHDE**EA**EE**E**7N**MD**RX**X**5**

Source: https://www.asd.gov.au/75th-anniversary/events/2022-09-01-75th-anniversary-commemorative-coin
