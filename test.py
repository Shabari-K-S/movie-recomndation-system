import imdb 
import streamlit as st
# creating instance of IMDb

ia = imdb.IMDb()

st.title('Movie Recommendation System')

# searching the movie

name_movie = st.text_input('Enter a movie title:',placeholder='The Matrix')

num = st.slider('Number of movies to recommend:', 1, 10, 5)

if st.button('Recommend'):
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

        poster = movie_i['full-size cover url']
        
        c1, c2 = st.columns([1, 4])
        with c1:
            st.image(poster)

        with c2:
            year = movie_i['year']
        
            st.write("###")
            st.write('Title:', title)
            rating = movie_i['rating']
        
            st.write(f'Year: {year}')
            st.write(f'Rating: {rating} :star:')

            try:
                directors = movie_i['directors']
                director = ','.join(map(str, directors))
                st.write('Directors:', director)
            except KeyError:
                st.write('Directors: not found')