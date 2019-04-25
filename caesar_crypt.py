def caesar_crypt_word(string):
    
    string = string.lower() #приводим нашу строку к нижнему регистру
    crypted = "" #создаем строку crypted 
    
    for i in range(len(string)):
        
        crypted += str(chr(ord(string[i]) + 5)) #к пустой строке crypted добовляем символы из string следующие за ними через 5
        
    return crypted #возвращаем строку crypted

word = input()
print(caesar_crypt_word(word))
