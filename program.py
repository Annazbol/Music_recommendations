from owlready2 import *
from random import randint

onto = get_ontology("C:/Users/User/Documents/Колледж/МДК 06.04/Лаба1/lab1.owx").load()
genre_class = onto["Жанр"]
artist_class = onto["Исполнитель"]
year_class = onto["Год_выпуска"]
song_class = onto["Музыкальные_треки"]
genre_instances = genre_class.instances()
artist_instances = artist_class.instances()
year_instances = year_class.instances()
song_instances = song_class.instances()

genre_list = [str(i)[9:].replace("_", " ") for i in list(genre_instances)]
artist_list = [str(i)[9:].replace("_", " ") for i in list(artist_instances)]
year_list = [str(i)[9:].replace("_", " ") for i in list(year_instances)]

song_properties = []

for ind in song_instances:
    related = []
    for prop in ind.get_properties():
        related.extend([str(prop)[9:].replace("_", " ") for prop in prop[ind]])
    song_properties.append(related)

song_properties = dict(zip([str(i)[9:].replace("_", " ") for i in list(song_instances)], tuple(song_properties)))

print('Добро пожаловать в систему рекомендации музыкальных произведений! ')
print('Пожалуйста, ответьте на несколько вопросов.')
while True:
    genre = input(f'Какой музыкальный жанр предпочитаете? ({', '.join(genre_list)}): ').strip()
    if genre not in genre_list:
        print('Данного жанра либо нет в базе, либо название жанра написано некорректно')
    elif not genre:
        print('Необходимо ввести данные')
    else:
        break
available_artists = sorted(list(set(
    item for props in song_properties.values() for item in props
    if item in artist_list and genre in props
)))
if not available_artists:
    print(f"К сожалению, исполнителей в жанре '{genre}' не найдено.")
    exit()
else:
    while True:
        artist = input(f'Какого исполнитель Вы бы хотели послушать? ({", ".join(available_artists)}): ').strip()
        if genre not in genre_list:
            print('Данного исполнителя либо нет в базе, либо название исполнителя написано некорректно')
        elif not genre:
            print('Необходимо ввести данные')
        else:
            break
available_years = sorted(list(set(
    item for props in song_properties.values() for item in props
    if item in year_list and genre in props and artist in props
)))

if not available_years:
    print(f"Для {artist} в жанре {genre} года не найдены.")
    exit()
else:
    while True:
        year = input(f'Какой год? ({", ".join(available_years)}): ').strip()
        if genre not in genre_list:
            print('Данного года либо нет в базе, либо он написан некорректно')
        elif not genre:
            print('Необходимо ввести данные')
        else:
            break

found_songs = []

for song_name, properties in song_properties.items():
    if (genre in properties and
        artist in properties and
        year in properties):
        found_songs.append(song_name)

print(f'Рекомендованный трек: {found_songs[randint(0, len(found_songs)-1)]}')