# English Word Frequencies

Each `txt` file contains lines in the format `word,freqency`. All words are in lowercase. The frequency is an integer that represents how common the word is. For more details, look at the script `process.py` to see exactly how the original data was converted to this format.

This dataset was created using [information from the Google Ngram viewer](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html). Each of the `txt` files was created by running `process.py` on the 1-gram file for each number. All of the 1-grams with non-alphabetic characters have been removed, so words listed here only include the letters a-z.
