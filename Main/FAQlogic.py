import pandas as pd;

#Load dataset and examine dataset, rename columns to questions and answers

df=pd.read_csv("C:/Users/verma/Documents/GitHub/Sem4PLPPrj/Main_code/TelegramBot-PizzaOrderBot-master/Counsel.csv")
df.columns=["questions","answers"]

import re
import gensim 
from gensim.parsing.preprocessing import remove_stopwords

def clean_sentence(sentence, stopwords=False):
    
    sentence = sentence.lower().strip()
    sentence = re.sub(r'[^a-z0-9\s]', '', sentence)
    #sentence = re.sub(r'\s{2,}', ' ', sentence)
    
    if stopwords:
         sentence = remove_stopwords(sentence)
    
    return sentence
                    
def get_cleaned_sentences(df,stopwords=False):    
    sents=df[["questions"]]
    cleaned_sentences=[]

    for index,row in df.iterrows():
        #print(index,row)
        cleaned=clean_sentence(row["questions"],stopwords)
        cleaned_sentences.append(cleaned)
    return cleaned_sentences

cleaned_sentences=get_cleaned_sentences(df,stopwords=True)
print(cleaned_sentences)

print("\n")

cleaned_sentences_with_stopwords=get_cleaned_sentences(df,stopwords=False)
print(cleaned_sentences_with_stopwords)

import numpy

sentences=cleaned_sentences_with_stopwords

# Split it by white space 
sentence_words = [[word for word in document.split() ]
         for document in sentences]

from gensim import corpora

dictionary = corpora.Dictionary(sentence_words)
for key, value in dictionary.items():
    print(key, ' : ', value)

import pprint
bow_corpus = [dictionary.doc2bow(text) for text in sentence_words]
for sent,embedding in zip(sentences,bow_corpus):
    print(sent)
    print(embedding)

import sklearn
from sklearn.metrics.pairwise import cosine_similarity;

def retrieveAndPrintFAQAnswer(question_embedding,sentence_embeddings,FAQdf,sentences):
    max_sim=-1
    index_sim=-1
    for index,faq_embedding in enumerate(sentence_embeddings):
        #sim=cosine_similarity(embedding.reshape(1, -1),question_embedding.reshape(1, -1))[0][0];
        sim=cosine_similarity(faq_embedding,question_embedding)[0][0]

        print(index, sim, sentences[index])
        if sim>max_sim:
            max_sim=sim
            index_sim=index
    
    answer = FAQdf.iloc[index_sim,1]
    return answer

def getAns(que):
    que=clean_sentence(que,stopwords=False)
    que_emb = dictionary.doc2bow(que.split())
    return retrieveAndPrintFAQAnswer(que_emb,bow_corpus,df,sentences)
