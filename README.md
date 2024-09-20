# <div align="center"></div>

## Description:

A Chrome extension for encrypting Gmail email that utilizes both asymmetric encryption (RSA) and symmetric encryption (AES).

## Purposes:

This project demonstrates an easy and practical approach to encrypting Gmail emails using RSA public/private keys and AES encryption methods.

1.  RSA is used to encrypt an AES key.
2.  The AES key is used to encrypt the email body text.
3.  The encrypted AES key is sent along with the encrypted email body.
4.  On the receiving end, the encrypted AES key is extracted, decrypted, and used to decrypt the encrypted email body.
5.  The decrypted email text is then displayed in a new window.

## Component Descriptions:

`keys` folder contains public keys for all recipient emails and the private key for current email user.  
`app.py`  is python code for a http server to provide public keys  
`content.js` is where all the action takes place.  
`keys_generator.py`  is a python code to generate RSA private/public key pairs.  

Note:  You need to update the list of recipients and their corresponding public key files in app.py.  
You can also relocate your private_key.pem to another location if desired.

## Procedure:

1.  Install the extension. 

Sending:

1.  Run app.py
2.  Compose Gmail email.
3.  Select 'Encrypt' from the extension button dropdown.

Receiving:

1.  Open the encrypted email.
2.  Select 'Descrypt' from the extension button dropdown.

## Contributors 

ChatGPT - Whatever free version is available at the time:  The coding machine!

## Disclaimer

This project is provided "as is" and without any warranty. Use it at your own risk. 

MIT License

Copyright (c) [2024] [github\babadue]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
   





