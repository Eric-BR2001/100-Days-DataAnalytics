# TMDb Movie Analysis - Todas as Perguntas

import tmdbsimple as tmdb
import requests
import pandas as pd
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import time

# Configuração da API
API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Substitua pelo seu API Key
tmdb.API_KEY = API_KEY

base_url = "https://api.themoviedb.org/3"
headers = {"Authorization": f"Bearer {API_KEY}"}
params_base = {"api_key": API_KEY, "language": "en-US"}

def get_paginated_results(endpoint, total_pages=5, **kwargs):
    results = []
    for page in range(1, total_pages + 1):
        time.sleep(0.2)  # Limitar taxa de requisição
        response = requests.get(f"{base_url}{endpoint}", params={**params_base, **kwargs, "page": page})
        data = response.json()
        results.extend(data.get("results", []))
    return results

# 1. Quantos filmes estão cadastrados na base de dados?
response = requests.get(f"{base_url}/movie/latest", params=params_base).json()
print("1. Total de filmes cadastrados (ID do último):", response['id'])

# 2. Quais são os 10 filmes mais antigos da base?
oldest = get_paginated_results("/discover/movie", sort_by="release_date.asc", total_pages=2)
oldest_sorted = sorted([m for m in oldest if m.get("release_date")], key=lambda x: x['release_date'])[:10]
print("\n2. 10 filmes mais antigos:")
for m in oldest_sorted:
    print(f"{m['title']} ({m['release_date']})")

# 3. Quantos filmes foram lançados por década?
decade_counter = Counter()
all_movies = get_paginated_results("/discover/movie", sort_by="release_date.asc", total_pages=10)
for movie in all_movies:
    date = movie.get("release_date")
    if date:
        year = int(date[:4])
        decade = (year // 10) * 10
        decade_counter[decade] += 1
print("\n3. Filmes por década:")
for dec, count in sorted(decade_counter.items()):
    print(f"{dec}s: {count}")

# 4. Qual é o gênero de filme mais comum na base?
genres = requests.get(f"{base_url}/genre/movie/list", params=params_base).json()['genres']
genre_map = {g['id']: g['name'] for g in genres}
genre_counter = Counter()
for movie in all_movies:
    for gid in movie.get('genre_ids', []):
        genre_counter[genre_map.get(gid, 'Unknown')] += 1
print("\n4. Gênero mais comum:", genre_counter.most_common(1))

# 5. Quantos filmes de ficção científica têm avaliação acima de 8.0?
scifi_id = next(g['id'] for g in genres if g['name'].lower() == 'science fiction')
scifi_movies = get_paginated_results("/discover/movie", with_genres=scifi_id, sort_by="vote_average.desc", vote_count_gte=50)
scifi_high = [m for m in scifi_movies if m['vote_average'] > 8.0]
print("\n5. Filmes de ficção científica com nota > 8.0:", len(scifi_high))

# 6. Top 5 filmes de terror com maior bilheteria
horror_id = next(g['id'] for g in genres if g['name'].lower() == 'horror')
horror_movies = get_paginated_results("/discover/movie", with_genres=horror_id, sort_by="revenue.desc")
print("\n6. Top 5 filmes de terror com maior bilheteria:")
for movie in horror_movies[:5]:
    print(f"{movie['title']} - Receita: {movie.get('revenue', 0)}")

# 7. Qual diretor tem mais filmes na base? (Aproximação)
director_counter = Counter()
movies_sample = get_paginated_results("/discover/movie", sort_by="popularity.desc", total_pages=5)
for movie in movies_sample:
    details = requests.get(f"{base_url}/movie/{movie['id']}/credits", params=params_base).json()
    crew = details.get("crew", [])
    for person in crew:
        if person['job'] == 'Director':
            director_counter[person['name']] += 1
print("\n7. Diretor com mais filmes:", director_counter.most_common(1))

# 8. Atores/atrizes em mais de 10 filmes
actor_counts = {}
people = get_paginated_results("/person/popular", total_pages=5)
for person in people:
    pid = person['id']
    credits = requests.get(f"{base_url}/person/{pid}/movie_credits", params=params_base).json()
    cast = credits.get('cast', [])
    if len(cast) > 10:
        actor_counts[person['name']] = len(cast)
print("\n8. Atores/atrizes com +10 filmes:")
for actor, count in actor_counts.items():
    print(f"{actor}: {count} filmes")

# 9. Filme com maior elenco
biggest_cast = ("", 0)
for movie in movies_sample:
    credits = requests.get(f"{base_url}/movie/{movie['id']}/credits", params=params_base).json()
    cast_count = len(credits.get("cast", []))
    if cast_count > biggest_cast[1]:
        biggest_cast = (movie['title'], cast_count)
print("\n9. Filme com maior elenco:", biggest_cast)

# 10. 3 filmes com maior nota média
top_rated = get_paginated_results("/discover/movie", sort_by="vote_average.desc", vote_count_gte=1000)
print("\n10. Top 3 filmes com maior nota média:")
for m in top_rated[:3]:
    print(f"{m['title']} - Nota: {m['vote_average']}")

# 11. Diferença crítica x público (não disponível na API)
print("\n11. Nota de crítica não disponível via API pública da TMDb. Pulado.")

# 12. Correlação orçamento x avaliação
budgets, ratings = [], []
for movie in movies_sample:
    details = requests.get(f"{base_url}/movie/{movie['id']}", params=params_base).json()
    budget = details.get('budget', 0)
    vote = details.get('vote_average', 0)
    if budget > 0 and vote:
        budgets.append(budget)
        ratings.append(vote)
if budgets and ratings:
    corr = np.corrcoef(budgets, ratings)[0, 1]
    print("\n12. Correlação orçamento x nota:", round(corr, 2))

# 13. Ano com mais lançamentos
year_counter = Counter()
for movie in all_movies:
    date = movie.get('release_date')
    if date:
        year = int(date[:4])
        year_counter[year] += 1
most_common_year = year_counter.most_common(1)[0]
print("\n13. Ano com mais lançamentos:", most_common_year)

# 14. Maior retorno financeiro (receita - orçamento)
best_profit = ("", -float('inf'))
for movie in movies_sample:
    details = requests.get(f"{base_url}/movie/{movie['id']}", params=params_base).json()
    revenue, budget = details.get('revenue', 0), details.get('budget', 0)
    if revenue and budget:
        profit = revenue - budget
        if profit > best_profit[1]:
            best_profit = (movie['title'], profit)
print("\n14. Filme com maior retorno:", best_profit)

# 15. Evolução média de notas por ano
votes_by_year = defaultdict(list)
for movie in all_movies:
    date = movie.get("release_date")
    if date and movie.get("vote_average"):
        year = int(date[:4])
        votes_by_year[year].append(movie["vote_average"])
years = sorted(votes_by_year.keys())
averages = [np.mean(votes_by_year[y]) for y in years]
plt.figure(figsize=(10, 5))
plt.plot(years, averages, marker='o')
plt.title("Evolução da nota média por ano")
plt.xlabel("Ano")
plt.ylabel("Nota Média")
plt.grid(True)
plt.tight_layout()
plt.show()
