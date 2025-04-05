class Movies:
    def __init__(self):
        self.moviespass = []

    def add_movie(self, movie):
        self.moviespass.append(movie)

#Создай два дочерних класса — Comedy и Drama. 
# Они наследуют метод add_movie(). Метод этих классов должен принимать параметр movie и добавлять его в конец списка self.movies. 
# Затем возвращать записи вида Комедии: '[]' и Драмы: '[]' соответственно.
class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.moviespass}"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.moviespass}"

comedy = Comedy()
print(comedy.add_movie('Большой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))