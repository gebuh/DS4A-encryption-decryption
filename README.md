# DS4A Mini project Encryption-Decryption Machine

## Description
From a user input txt file E-D will encrypt (public key) or decrypt (private key) text using configurable keys

## File Structure
```
DS4A-encryption-decryption
├── rsa
    ├── arguments.py
    ├── decryption.py
    ├── encryption.py
    ├── rsa_calc.py
```



## Usage

assumes you're running from the rsa directory

```
$ python encryption.py 

Optionally you can set your own co primes
$ python encryption.py 53 59

at the prompt enter your string to encrypt and press enter
$ give me some text: 
a cipher will be generated

python decryption.py is similar, you will have to use the same primes used to create your cipher
and the cipher exactly as printed
```



## Limitations
Following characters are allowed (values from string.printable)
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

decryption with some co primes do not work - need more investigation why, but the default p=13 and q=17 and p=53 and q=50  work

## TODO
create a test harness to automate testing
create standard test data
- import the decimal module to reduce floating-point errors: [floating point errors](https://medium.com/code-85/how-to-stop-floating-point-arithmetic-errors-in-python-a98d3a63ccc8)

### More info:
[link to project requirements](https://s3.us-east-2.amazonaws.com/ds4a-empowerment-2.0/cases/training/Encryption-Decryption+Mini-Project.pdf?latest=true)

This project was created with Python 3.8



