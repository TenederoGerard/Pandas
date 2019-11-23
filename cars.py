import pandas as pd

#Corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv("cars.csv") 

#Display the first five and last five rows of the resulting cars.
A = cars.head(5).append(cars.tail(5))
