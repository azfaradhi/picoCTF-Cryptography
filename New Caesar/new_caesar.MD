# ReadMyCert (Medium)

## Problem
```
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm
```

* [new_caesar.py](./new_caesar.py)


## Hint

1. How does the cipher work if the alphabet isn't 26 letters?
2. Even though the letters are split up, the same paradigms still apply

## Solution

1. We need to make python file that reverse all things new_caesar.py do.
    ```
    import string

    LOWERCASE_OFFSET = ord("a")
    ALPHABET = string.ascii_lowercase[:16]

    def eightbit_into_int(eightbit):
        value = 0
        for i in range(8):
            value += int(eightbit[i]) * (2 ** (7-i))
        return value

    def dec_b16_encode(enc):
        plain = ""
        for i in range(0,len(enc),2):
            firstfourbit = "{0:04b}".format(ord(enc[i])-LOWERCASE_OFFSET)
            lastfourbit = "{0:04b}".format(ord(enc[i+1])-LOWERCASE_OFFSET)
            bit = firstfourbit + lastfourbit
            value = eightbit_into_int(bit)
            plain += chr(value)
        return plain



    def unshift(cc,key):
        for c in range (97,123):
            if (ord(cc) - 97) == (c + key - 2) % 16:
                return chr(c)
        return (97 - key + ord(cc)) % 16


    string = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

    for k in range(97,123):
        b16 = ""
        for cc in string:
            b16 += unshift(cc,k)
        a = dec_b16_encode(b16)
        print(a)
    ```
2. That code will give us the output:
    ```
    ©¸¸¹su¥§yªw¨{}vt¥|yzut¥ª©¦vy{v|wu¨¥¥|
    §§¨bdhfjleckhidcehjekfdk
    qQqSWUY[TRZWXSRTWYTZUSZ
    v`@`BrtFwDuHJCArIFGBArwvsCFHCIDBurrI
    et_tu?_1ac5f3d7920a85610afeb2572831daa8
    TcNcd.N PR$U"S&(!/P'$% /PUTQ!$&!'" SPP'
    CR=RS=OADBOODC@BOO
    2A,AB
    >32?1>>
    !01û-/ñ"ÿ óõþü-ôñòýü-"!.þñóþôÿý --ô
    /
    / ê
    ìàîâäíëãàáìëíàâíãîìã
    ùÙùÛ
    ßÝÑÓÜÚ
        ÒßÐÛÚ

            ÜßÑÜÒÝÛ

                    Ò
    ÈèÊúüÎÿÌýÀÂËÉúÁÎÏÊÉúÿþûËÎÀËÁÌÊýúúÁ
    íü×üý·×¹éë½î»ì¿±º¸é°½¾¹¸éîíêº½¿º°»¹ìéé°
    ÜëÆëì¦Æ¨ØÚ¬ÝªÛ® ©§Ø¯¬­¨§ØÝÜÙ©¬®©¯ª¨ÛØØ¯
    ËÚµÚÛµÇÉÌÊÇÇÌËÈÊÇÇ
    ºÉ¤ÉÊ¤¶¸»¹¶¶»º·¹¶¶
    ©¸¸¹su¥§yªw¨{}vt¥|yzut¥ª©¦vy{v|wu¨¥¥|
    §§¨bdhfjleckhidcehjekfdk
    qQqSWUY[TRZWXSRTWYTZUSZ
    v`@`BrtFwDuHJCArIFGBArwvsCFHCIDBurrI
    et_tu?_1ac5f3d7920a85610afeb2572831daa8
    TcNcd.N PR$U"S&(!/P'$% /PUTQ!$&!'" SPP'
    CR=RS=OADBOODC@BOO
    2A,AB
    >32?1>>
    !01û-/ñ"ÿ óõþü-ôñòýü-"!.þñóþôÿý --ô
    /
    / ê
    ìàîâäíëãàáìëíàâíãîìã
    ```
3. Pick the one where all of the characters is in ascii printable characters.

### Flag

`picoCTF{et_tu?_1ac5f3d7920a85610afeb2572831daa8}`