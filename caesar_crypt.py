def caesar_crypt_word(string):
    crypted = ""
    for i in range(len(string)):
        crypted += str(chr(ord(string[i]) + 5))
    return crypted
word = input()
print(caesar_crypt_word(word))
