secret_word = input('Type something:')
shift = 3 

# implement cipher encrypt algo
def caesar_cipher_encrypt(secret_word,shift):
 # first i`m put all of it in cycle 
    encrypted_text = ''.join(
        chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else # here im checking if char is lower. then i'm shifting it begining with position 97
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else char # if position start with upper cases, then i'm shifting with 65 position in ASCI
        for char in secret_word
    )
    return encrypted_text # return result 

# implement decrypt algo 
def caesar_cipher_decrypt(encrypted_word,shift):
    decrypted_text = ''.join(
        chr((ord(char) - 97 - shift) % 26 + 97) if char.islower() else  # the principle is the same with encryption. the difference, that i'm shift back at the amout position
        chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else char 
        for char in encrypted_word
    )
    return decrypted_text # return result 

# store result of encrypt and decrypt method 
test_word_encrypt = caesar_cipher_encrypt(secret_word,shift)
test_word_decrypt = caesar_cipher_decrypt(test_word_encrypt,shift)

# print results 
print(f'The encrypted word is:{test_word_encrypt}\nThe decrypted code is:{test_word_decrypt}')




