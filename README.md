This code uses python's english_words module.

The required module can be installed using the following command :

  pip install english-words
  
The module contains sets of English words. 

We use english_words_set set of the module which contains both upper- and lower-case letters; with punctuation.

The program can be run using the following command :

  python3 jumble.py
  
Upon the running the program, the user is prompted for a input which can be scrambled.

The program outputs the best possible word that can formed using the scrambled words by searching all possible words in the english_words_set.

For example, 

  if the input is : teg
  the program returns : get
