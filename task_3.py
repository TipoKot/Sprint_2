# Напиши класс PointsForPlace. Он получает количество очков в зависимости от места, которое занял спортсмен.
class PointsForPlace:
# В этом классе напиши метод get_points_for_place(), который принимает аргумент place — целое число. Причём: 
#   Если место строго больше 100, должно выводиться сообщение 'Баллы начисляются только первым 100 участникам'.
#   Если как аргумент передали значение меньше 1, должно печататься сообщение 'Спортсмен не может занять нулевое или отрицательное место'.
#   В остальных случаях начисляются очки по формуле: 101 - place.
# Изначально количество очков равно нулю: подумай, как это отобразить в коде.
# Метод get_points_for_place() должен возвращать points.
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
            return
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
            return
        else:
            points = 101 - place
            return points
        
# Напиши класс PointsForMeters. Он рассчитывает очки в зависимости от количества метров, 
# на которое спортсмен толкнул ядро или метнул диск: расстояние*0,5.
# Например, если расстояние 10 метров, спортсмен получит 5 очков.
class PointsForMeters:
    # Напиши метод get_points_for_meters(), который принимает аргумент meters — целое число. Причём:
    #   Если количество метров меньше нуля, должно выводиться сообщение Количество метров не может быть отрицательным'.
    #   В остальных случаях начисляются очки по формуле: «количество метров умножить на 0.5».
    # Метод должен возвращать points. Изначально количество очков — 0.
    @staticmethod
    def get_points_for_meters(meters):
        points = 0
        if meters < 0:
            print("оличество метров не может быть отрицательным")
            return
        else:
            points = meters * 0.5
            return points

# Напиши класс TotalPoints для многоборцев. Он наследуется сразу от двух классов — PointsForPlace и PointsForMeters и реализует все их методы.
class TotalPoints(PointsForPlace, PointsForMeters):
    #Также он должен содержать:
    #   метод get_total_points(), который принимает как аргументы meters и place;
    #   переменную total, которая суммирует значения методов get_points_for_place() и get_points_for_meters().
    # Метод возвращает переменную total.
    @staticmethod
    def get_total_points(meters, place):
        total = PointsForPlace.get_points_for_place(place) + PointsForMeters.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))