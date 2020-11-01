
import pandas as pd
import os
import numpy as np
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

#now some text processing
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


df1=pd.read_csv('C:/Users/ann/Documents/MSDS434/FinalProject/True.csv')
df2=pd.read_csv('C:/Users/ann/Documents/MSDS434/FinalProject/Fake.csv')


df1['Target']=1
df2['Target']=0
df=pd.concat([df1,df2],axis=0)
df=df.drop(['text','subject','date'],axis=1)
def custom_preprocessor(text):
    '''
    Make text lowercase, remove text in square brackets,remove links,remove special characters
    and remove words containing numbers.
    '''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) # remove special chars
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    
    return text

df['title']=df['title'].apply(custom_preprocessor)

y=df['Target']
x=df['title']


x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.2)


vectorizer = TfidfVectorizer()
x_trn_vec = vectorizer.fit_transform(x_train)
model_1=LogisticRegression()
model_1.fit(x_trn_vec,y_train)
pred_1=model_1.predict(vectorizer.transform(x_test))
score_1=accuracy_score(y_test,pred_1)
#print(score_1)
