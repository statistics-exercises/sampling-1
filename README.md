# Introduction to pandas

We are going to consider some real data in this series of exercises and learn about a new data type that we can use to handle real data in Python: a panda data frame.

If you look at the file called movie_data.txt by clicking on this file you will see the data that we are manipulating in this series of exercises.  This data set is taken from IMDB database and it contains various pieces of information about 1000 films.  In the file the data on each film is contained in a comma separated list on each row.  The 11 columns in this file then provide information on:
 
1. the titles of the films
2. a numerical index for the film
3. the genre of the film
4. the film's direction 
5. the actors who were in the film
6. the year the film was released
7. the films runtime in minutes
8. the films rating on IMDB
9. the number of votes that were cast to determine the rating
10. the amount of money the film made 
11. the metascore for the film.

It is difficult to read the movie_data.txt file.  If you thus go back to the code I have thus loaded the data into a panda data frame to make it easier to look through this information.  To see how loading the data this way makes it easier to see the data execute the code in the panel on the left now.  It will output information on the first five films that are listed in the file called `movie_data.txt`.

A panda data frame is somewhat like the 2D NumPy arrays that we have seen in previous weeks.  There are two important differences:

1. The elements in a 2D NumPy array can only be numbers.  The elements in a panda data frame by contrast can be numbers of strings of characters such as the titles of the movies in the data frame that we are using here.
2. We can pull data out of a data frame by referring using strings instead of indexes.  To see how this works in practise consider the command below:

````
print( movies.loc["Prometheus"] )
````

If you copy and paste this into the code cell on the left in place of the print command that is currently there the reworked code will output the information from `movie_data.txt` about the film Prometheus.

To complete this exercise I would like you to use commands such as the one above to extract and print information about the films:

Moonlight
La La Land
The Magnificent Seven

The information should be printed out in that order.  You should only print out information on these three films.
