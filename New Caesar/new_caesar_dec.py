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

