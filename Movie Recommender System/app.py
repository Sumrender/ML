import streamlit as st
import pickle
import requests

new_df = pickle.load(open('movies.pkl', 'rb'))
movies_name = new_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))
# print(movies_name)


# def fetch_poster(movie_id):
#     response = requests.get(
#         f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=62a8fa0074bf8e06e8ef823109f0e252')
#     data = response.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path


def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    recommend = []
    for i in movies_list:
        recommend.append(new_df.iloc[i[0]].title)

    return recommend


st.title('Movies Recommender System')

selected_movie_name = st.selectbox(
    'Enter movie to find similar movies', movies_name
)

if st.button('Recommend'):
    reco_movies = recommend(selected_movie_name)
    for movie in reco_movies:
        st.write(movie)
