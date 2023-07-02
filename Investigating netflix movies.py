years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
movie = {'years':years, 'durations':durations}
print(movie)
import pandas as pd
df = pd.DataFrame(movie)
print(df)
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(df['years'], df['durations'])
plt.title("Netflix Movie Durations 2011-2020")
plt.show()
netflix = pd.read_csv("netflix_data.csv")
print(netflix.head())   
netflix_df = netflix[netflix['type'] == 'Movie']
netflix_movies_col = netflix_df[['title', 'country', 'genre', 'release_year', 'duration']]
print(netflix_movies_col[0:5])
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col["release_year"], netflix_movies_col["duration"])
plt.title("Movie Duration by Year of Release")
plt.show()
short_movies = netflix_movies_col[netflix_movies_col['duration'] < 60]
print(short_movies[0:20])
colors = []
for lab, row in netflix_movies_col.iterrows():
    if row['genre'] == "Children" :
        colors.append("red")
    elif row['genre'] == "Documentaries" :
        colors.append("blue")
    elif row['genre'] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")
print(colors[0:10])
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col["release_year"],netflix_movies_col["duration"], c = colors)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()
