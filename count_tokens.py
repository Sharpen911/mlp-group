import nltk
import re
def preprocessing(content):


    pattern = '[^a-zA-Z0-9\\ ]'

    content_str = re.sub(pattern, ' ', content).lower()
    tokens_list = nltk.word_tokenize(content_str)

    return tokens_list
#for clickbait
# with open("originaldata/clickbait.txt") as f1:
#     clickbait = f1.read()
# with open("originaldata/clickbait.txt") as f2:
#     non_clickbait = f2.read()

with open("originaldata/Biomedical.txt",encoding='utf-8') as f:
    text = f.read()
tokens = preprocessing(text)
print(len(set(tokens)))