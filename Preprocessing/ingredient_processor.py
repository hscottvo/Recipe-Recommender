import nltk
import string

def ingredient_process(ingredient):
    ingredient = ingredient.lower()

    # Remove punctuation
    ingredient_p = "".join([char for char in ingredient if char not in string.punctuation])

    # Tokenize words
    ingredient_p = nltk.word_tokenize(ingredient_p)

    # Remove stemming words
    filter_words = []
    snowball_st = nltk.stem.snowball.SnowballStemmer("english")
    for i in ingredient_p:
        filter_words.append(snowball_st.stem(i))

    # Select Nouns Only
    root_ingredient = []
    pos = nltk.pos_tag(filter_words)
    for i in pos:
        if i[1] == "NN":
            root_ingredient.append(i[0])
    
    return root_ingredient


ingredients = ["Frozen Carrots."]
for i in ingredients:
    print(ingredient_process(i))