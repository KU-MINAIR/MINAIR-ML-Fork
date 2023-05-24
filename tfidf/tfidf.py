from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import os

path = '../extraction/extraction_keyword/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('extraction.txt')]

corpus = []
name = [] 

for i in file_list_py :
    file = open(path + i, encoding='UTF8')
    lines = ""
    while True:
        line = file.readline()
        if not line:
            break
        lines = lines + " " + line
    file.close()
    corpus.append(lines)
    name.append("_" + i.replace("_extraction.txt", ""))


vect = CountVectorizer()
document_term_matrix = vect.fit_transform(corpus)       # 문서-단어 행렬 

tf = pd.DataFrame(document_term_matrix.toarray(), columns=vect.get_feature_names())  
                                             # TF (Term Frequency)
D = len(tf)
df = tf.astype(bool).sum(axis=0)
idf = np.log((D+1) / (df+1)) + 1             # IDF (Inverse Document Frequency)

# TF-IDF (Term Frequency-Inverse Document Frequency)
tfidf = tf * idf                      
tfidf = tfidf / np.linalg.norm(tfidf, axis=1, keepdims=True)
tfidf.index = name

tfidf.to_csv("tfidf_table.csv", index='True', encoding='utf-8-sig')