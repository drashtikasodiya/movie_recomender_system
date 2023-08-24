import streamlit as st
import pickle
import pandas as pd
import requests

# getting requirement for system
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=47032f9b6c1e2da17a8c4972176ccc2f&language=en-US')
    data = response.json()
    return  'https://image.tmdb.org/t/p/original' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    recom_list_index = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recom_list = []
    recom_poster = []
    for i, j in recom_list_index:
        movie_id=movies.iloc[i]['movie_id']
        recom_list.append(movies.iloc[i]['title'])
        recom_poster.append(fetch_poster(movie_id))
    return recom_list,recom_poster

st.title('Movie Recommendation System')
st.title(" ")

selected_movie_name = st.selectbox(
    'Enter Movie for Recommendation',
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


