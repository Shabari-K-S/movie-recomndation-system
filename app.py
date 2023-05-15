import imdb 
import streamlit as st
# creating instance of IMDb

st.set_page_config(page_title='Movie Recommendation System', page_icon=':movie_camera:', layout='wide', initial_sidebar_state='auto')

ia = imdb.IMDb()

st.title('Movie Recommendation System')

# searching the movie

name_movie = st.text_input('Enter a movie title:',placeholder='The Matrix')

num = st.slider('Number of movies to recommend:', 1, 10, 5)

if st.button('Recommend'):
    st.write('---')
    st.header('Recommended movies:')
    search = ia.search_movie(name_movie)

    if len(search) <num:
        st.info(f"Sorry, we have less recommendations found for {name_movie}.")
        num = len(search)
    for i in range(num):
        id = search[i].getID()

        # getting information

        movie_i = ia.get_movie(id)

        title = movie_i['title']
        


        st.write("###")
        st.subheader(f"{i+1} - {title}")
        st.write("###")
        # getting movie poster
        c1, c2 = st.columns([1, 4])
        with c1:
            try:
                poster = movie_i['full-size cover url']
                st.image(poster)
            except KeyError:
                st.write('Poster not found')
        with c2:
            year = movie_i['year']
        
            st.write("###")
            st.write('Title:', title)
            
            try:
                st.write(f'Year: {year}')
            except KeyError:
                st.write('Year: not found')
            try:
                rating = movie_i['rating']
                st.write(f'Rating: {rating} :star:')
            except KeyError:
                st.write('Rating: not found')
            try:
                directors = movie_i['directors']
                director = ','.join(map(str, directors))
                st.write('Directors:', director)
            except KeyError:
                st.write('Directors: not found')
