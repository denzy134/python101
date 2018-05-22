pyg = ('ay')

name = input('what is your name: ')
original = input('Enter a word: ')
print (name + ' your original word is ' + original)

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print ('Your pig latin word is ' + new_word)
else:
    print ('try_again')