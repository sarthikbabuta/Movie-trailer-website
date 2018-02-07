#media vali python file
import media
import fresh_tomatoes

tiger = media.Movie("Tiger Zinda hai","Salman Khan and katrina Kaif","http://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2017/10/25/Pictures/tiger-poster-salman-tiger-katrina-zinda-featuring_84cce058-b941-11e7-83cc-689513d74e1b.jpg","https://www.youtube.com/watch?v=ePO5M5DE01I")
#print (tiger.storyline)

fukrey = media.Movie("Fukrey Returns","Story of 4 Friends","https://pbs.twimg.com/media/DQgvrlyVAAAAKF_.jpg","https://www.youtube.com/watch?v=f-UzOpuKOVY")
#print(fukrey.storyline)
#fukrey.show_trailer()

raees = media.Movie("Raess","Shah Rukh Khan","http://images.mymovies.net/images/film/cin/350x522/fid17187.jpg","https://www.youtube.com/watch?v=J7_1MU3gDk0")

dangal = media.Movie("Dangal","Aamir Khan","https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg","https://www.youtube.com/watch?v=x_7YlGv9u1g")

movies = [tiger,fukrey,raees,dangal]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.valid_ratings)

print(media.Movie.__doc__)



