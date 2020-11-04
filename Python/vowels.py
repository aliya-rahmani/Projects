def is_vowel(letter):
    if letter in "aeiouAEIOU":
      return True
    else: 
      return False

def vowelcount(word):
  
  num_vowels = 0
  for letter in word:
      if is_vowel(letter):
          num_vowels += 1
      else:
          pass
  return num_vowels


word = input("Enter a word: ")
length = len(word)
vowels = vowelcount(word)
consonants = length - vowels
print("There are {} vowels and {} consonants in {}".format(vowels, consonants, word))
