from nltk.tokenize import sent_tokenize, word_tokenize
text = "NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.."
number = int(input('Choice number '))
if number == 1 :
    #     y = text.split()
    #     print(y)
    print(word_tokenize(text))
elif number == 2 :
    #     y = text.split('.')
    #     print(y)
    print(sent_tokenize(text))
elif number == 3:
    print(text)
# Importing pandas package
import pandas as pd

