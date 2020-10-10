#Encrypts and decrypts using key
def encrypt(plain_text,key):
   ciphered_text = ""
   plain_text = plain_text.replace(" ", "").lower()
   for letter in plain_text:
      ciphered_text += chr((ord(letter) + key -97) % 26 + 97)
   return ciphered_text

def decrypt(ciphered_text,key):
   translated_text=""
   ciphered_text = ciphered_text.lower()
   for letter in ciphered_text:
      translated_text += chr((ord(letter) - key - 97) % 26 + 97)
   return translated_text

if __name__ == '__main__':

   print("\t\t\t==========Welcome to Caesar Cipher===========\t\t\t\n")
   plain_text = input("Please enter your text: ")
   key= int(input("\nPlease enter key: "))
   encrypted_text = encrypt(plain_text,key)
   print("Encrypted Text is: " + encrypted_text)
   print("Decrypted Text is: " + decrypt(encrypted_text, key))
   