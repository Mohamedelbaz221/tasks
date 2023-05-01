import pandas as pd
from  nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
ps = PorterStemmer()
sb = SnowballStemmer('English')
user_choice = int(input('Please Enter Your Choice :'))
if user_choice == 4:
    var = int(input('Choose Snowball or Porter?:'))
if var == 1:
    print(ps.stem('Programming'))
elif var == 2:
    print(sb.stem('Programming'))