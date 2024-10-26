import streamlit as st
import pickle
import requests

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Load movie data
movies = pickle.load(open(r"C:\Users\dell\OneDrive\clutterfolder\movie\movie_list.pkl", 'rb'))
similarity = pickle.load(open(r"C:\Users\dell\OneDrive\clutterfolder\movie\similar_score.pkl", 'rb'))
movies_list = movies['title'].values

# Streamlit Header
st.header("Movie Recommendation System")

# Custom component for image carousel
import streamlit.components.v1 as components
imageCarouselComponent = components.declare_component("image-carousel-component", path=r"C:\Users\dell\OneDrive\clutterfolder\movie\frontend\frontend\public")

# Image URLs for carousel
imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
]
imageCarouselComponent(imageUrls=imageUrls, height=200)

# State management for dropdown interaction
if "dropdown_clicked" not in st.session_state:
    st.session_state.dropdown_clicked = False

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommend_poster

# Dropdown text based on state
dropdown_text = "▼ Select movie from dropdown" if not st.session_state.dropdown_clicked else "▶ Select movie from dropdown"

# Dropdown for movie selection
selectvalue = st.selectbox(dropdown_text, movies_list, on_change=lambda: st.session_state.update(dropdown_clicked=True))

# Show recommended movies on button click
if st.button("Show Recommendation"):
    movie_name, movie_poster = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])






