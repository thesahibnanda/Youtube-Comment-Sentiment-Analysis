#Data Preprocessing

#First We Have To Download NLTK Packages, They Should Be Downloaded Only Once
#Run The Below Commented Script Only Once
"""
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')
nltk.download('wordnet')
"""
#Importing Libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
from string import punctuation
import re
import enchant



#Below Code Is For PreProcessing Data

#Dictionary
english_dict = enchant.Dict("en_US")

#Removal Of Non Dictionary Words
def Remove_Non_Dict_Words(text):
    words_only = ''.join([c if c.isalpha() else ' ' for c in text]) 
    dict_words_only = [word for word in words_only.lower().split() if english_dict.check(word)]  
    return ' '.join(dict_words_only)


#Preprocessing Using NLTK
def Preprocess_Text_NLTK(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens]
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

#Lemmatization Of Text (Part 1: Defining Lemmatized Words)
def lemmatize_word(word):
    inflections = {
        'nouns': {'s': '', 'es': '', 'ies': 'y'},
        'verbs': {'s': '', 'es': '', 'ies': 'y', 'ed': 'e', 'ing': 'e'}
    }
    stem, suffix = '', ''
    for i in range(len(word)):
        if i == len(word) - 1 or word[i+1:].isalpha():
            suffix = word[i:]
            break
        stem += word[i]
    if suffix.startswith('N'):
        inflection = inflections['nouns']
    elif suffix.startswith('V'):
        inflection = inflections['verbs']
    else:
        return word
    for suffix in inflection:
        if stem.endswith(suffix):
            base_word = stem[:-len(suffix)] + inflection[suffix]
            return base_word + suffix
    return word

#Lemmatization Of Text (Part 2: Lemmatization)
def Lemmatize_Text(text):
    words = re.findall(r'\b\w+\b', text)
    lemmatized_words = [lemmatize_word(word) for word in words]
    lemmatized_text = ' '.join(lemmatized_words)
    return lemmatized_text

#Cleaning Text
def Clean_Text_WO_L(text):
    text = re.sub(r"http\S+", "", text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r"#[\w\d]+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = ''.join([c for c in text if c not in punctuation and not c.isdigit()])
    text = text.lower()
    text = re.sub('\s+', ' ', text).strip()
    words = text.split()
    stop_words = set(['a', 'an', 'the', 'and', 'or', 'but', 'not', 'in', 'on', 'at', 'to', 'of', 'for', 'with', 'by', 'from'])
    words = [word for word in words if word not in stop_words]
    cleaned_text = ' '.join(words)
    return cleaned_text

#Correcting Misspelled Words
def Correction(text):
    words = text.split()
    for i, word in enumerate(words):
        if not english_dict.check(word):
            suggestions = english_dict.suggest(word)
            if suggestions:
                words[i] = suggestions[0]
    corrected_text = " ".join(words)
    return corrected_text

#Cleaning Text Using Above Functions
def Clean_Text_WO_NLTK(text):
    a = Clean_Text_WO_L(text)
    b = Lemmatize_Text(a)
    return b

#Finally This Preprocesses Data
def Clean_Text(text):
    a = Preprocess_Text_NLTK(text) #NLTK Preprocessing
    b = Clean_Text_WO_NLTK(a)#Without NLTK (Lemmatize And Other Things) Preprocessing
    c = Correction(b)#Correcting Misspelled Words
    d = Remove_Non_Dict_Words(c)#Removing Words Not In Dictionary
    return d
