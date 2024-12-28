# ReadMyCert (Medium)

## Problem
```
How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file here.
```

* [readmycert.csr](./readmycert.csr)


## Hint

1. Download the certificate signing request and try to read it.

## Solution

1. If you see "=" or "==" at the end of a mysterious text, usually the text is in Base64. Using the Base64 decoder online, we'll got the flag.

### Flag

`picoCTF{read_mycert_41d1c74c}`