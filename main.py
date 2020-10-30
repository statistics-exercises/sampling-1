# Uncomment these two lines if you get an error saying pandas is not available
#from os import system
#system('pip install pandas')
import numpy as np 
import pandas as pd

# This reads in the data from the movie_data.txt file
movies_df = pd.read_csv("movie_data.txt", index_col="Title")

# This command outputs the first five elements in the movie_data.txt file 
print( movies_df.head() )
