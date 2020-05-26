# English Word Frequencies

Each `txt` file contains lines in the format `word,freqency`. All words are in lowercase. The frequency is an integer that represents how common the word is. For more details, look at the script `process.py` to see exactly how the original data was converted to this format. The `uncompressed` directory contains the raw text files for each letter and for all of the letters combined. The `compressed` directory contains the same files compressed using `gzip`.

This dataset was created using [information from the Google Ngram viewer](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html). Each of the `txt` files was created by running `process.py` on the 1-gram file for each letter. All of the 1-grams with non-alphabetic characters have been removed, so words listed here only include the letters a-z.

## License

The [source data](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html) for this dataset is licensed under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/). Apart from that I really don't care what you use this for.
