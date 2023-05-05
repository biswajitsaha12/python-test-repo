import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# Extract the relevant data from the dataset
movies = []
for item in data:
  year = item['year']
  genre = item['genres']
  movies.append({'year': year, 'genre': genre})

# Filter the data to include only movies released between 2010 and 2018
movies_2010_2018 = [movie for movie in movies if 2010 <= movie['year'] <= 2018]

# Count the number of movies released per genre per year
genre_counts = {}
for movie in movies_2010_2018:
  year = movie['year']
  if year not in genre_counts:
    genre_counts[year] = {}
  for genre in movie['genre']:
    if genre not in genre_counts[year]:
      genre_counts[year][genre] = 0
    genre_counts[year][genre] += 1

print("\n1.Most films per year per genre b/w 2010 - 2018: ")
max_genre_counts = {}
for year in genre_counts:
  max_count = max(genre_counts[year].values())
  max_genres = [
    genre for genre, count in genre_counts[year].items() if count == max_count
  ]
  max_genre_counts[year] = {'genres': max_genres, 'count': max_count}
print(json.dumps(max_genre_counts, indent=2))

# List down the number of movies released in each genre in the year 2018 in descending order
movies_2018 = [movie for movie in movies_2010_2018 if movie['year'] == 2018]
genre_counts_2018 = {}
for movie in movies_2018:
  genre = "|".join(movie['genre'])
  if genre not in genre_counts_2018:
    genre_counts_2018[genre] = 0
  genre_counts_2018[genre] += 1
sorted_genre_counts_2018 = sorted(genre_counts_2018.items(),key=lambda x: x[1],reverse=True)

print("\n2.Count of Movies released in each Genre in 2018: (Genre, Count) ")
for genre, count in sorted_genre_counts_2018:
  print(genre, count)
