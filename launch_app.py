
from video_summarizer import collect_transcript

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()



def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)









tfidf=pickle.load( open( 'tfidf_vectorizer.pkl','rb' ) )
model=pickle.load( open( 'bnb_model.pkl', 'rb' ) )

st.title('Video  Metadata  Generation & Classification')

input_video=st.text_area('Enter the Youtube Video URL')


if st.button('Classify'):
    st.video(input_video)
    #st.header(input_video)
    text=collect_transcript(input_video)

    # 1. preprocess
    video_text = transform_text(text)
    
    # 2. vectorize
    vector_input = tfidf.transform([video_text])
    
    # 3. predict
    result = model.predict(vector_input)[0]
    
    # 4. Display
    if  result==0:
     #st.header("Art & Music")
     st.success("Art & Music")
    elif result==1:
     st.success("Food")
    elif result==2:
        st.success("Sports")
    elif  result==3:
        st.success("Technology")
    elif result==4:
     st.success("Travel")
    else:
      print("OTHER Category")



        
