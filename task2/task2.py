import sys
PATH_QP = sys.argv[1]
PATH_P = sys.argv[2]


class Point :
    def __init__(self, start, end):
        self.start = start
        self.end = end

quadrangle_points =[] #массив с координатами точек четырехугольника
points =[] #массив с координатами проверяемых точек

#Функция проверяющая совпадение точки и вершин четырехугольника
def equal(point):
    for q_point in quadrangle_points:
        if q_point.x == point.x and q_point.y == point.y:
            return 1


with open(PATH_QP) as file: #Открываю файл с координатами вершин четырехугольника
    for line in file:
        quadrangle_points.append(Point(float(line.split()[0]), float(line.split()[1])))#добавляю координаты в массив

with open(PATH_P) as file:#Открываю файл с координатами проверяемых точек
    for line in file:
        points.append(Point(float(line.split()[0]), float(line.split()[1])))#добавляю координаты в массив


for point in points:
    #Проверяю совпадает ли точка с одной из вершин четырехугольника
    if  equal(point):
        #Точка на одной из вершин
        print('0')
    else:
        """
        Алгоритм проверки следующий:
        
        Будем использовать уравнение прямой проходящей через 2 точки
        (x-x1)*(y2-y1) - (y-y1)(x2-x1) = 0; x1,y1; x2,y2 - координаты точек ребра
        Подставляя в это уравнение исследуемые точки значение 0 получим для точек лежащих на этой прямой.
        Для того чтобы проверить находится ли точка на стороне принадлежащей четырехугольнику относительно данной прямой
        нужно проверить соврадает ли знак у результата для исследуемой точки и для точки находящейся в плоскости 
        четырехугольника но не лежащей на этой прямой (наример вершину находящуюся на противоположной стороне).
        Проверяем это для всех сторон обходя их последовательно. Если для всех сторон условие выполняется то точка 
        находится внутри четырехугольника
        
        """
        # для первой стороны
        res1 = ((point.x - quadrangle_points[0].x )*(quadrangle_points[1].y-quadrangle_points[0].y) - \
               (point.y - quadrangle_points[0].y )*(quadrangle_points[1].x-quadrangle_points[0].x)) * \
               ((quadrangle_points[2].x - quadrangle_points[0].x)*(quadrangle_points[1].y-quadrangle_points[0].y) - \
               (quadrangle_points[2].y - quadrangle_points[0].y)*(quadrangle_points[1].x-quadrangle_points[0].x))
        # для второй стороны
        res2 = ((point.x - quadrangle_points[1].x )*(quadrangle_points[2].y-quadrangle_points[1].y) - \
               (point.y - quadrangle_points[1].y )*(quadrangle_points[2].x-quadrangle_points[1].x)) * \
               ((quadrangle_points[3].x - quadrangle_points[1].x)*(quadrangle_points[2].y-quadrangle_points[1].y) - \
               (quadrangle_points[3].y - quadrangle_points[1].y)*(quadrangle_points[2].x-quadrangle_points[1].x))
        # для третьей стороны
        res3 = ((point.x - quadrangle_points[2].x) * (quadrangle_points[3].y - quadrangle_points[2].y) - \
                (point.y - quadrangle_points[2].y) * (quadrangle_points[3].x - quadrangle_points[2].x)) * \
               ((quadrangle_points[0].x - quadrangle_points[2].x) * (quadrangle_points[3].y - quadrangle_points[2].y) - \
                (quadrangle_points[0].y - quadrangle_points[2].y) * (quadrangle_points[3].x - quadrangle_points[2].x))
        # для четвертой стороны
        res4 = ((point.x - quadrangle_points[3].x) * (quadrangle_points[0].y - quadrangle_points[3].y) - \
                (point.y - quadrangle_points[3].y) * (quadrangle_points[0].x - quadrangle_points[3].x)) * \
               ((quadrangle_points[1].x - quadrangle_points[3].x) * (quadrangle_points[0].y - quadrangle_points[3].y) - \
                (quadrangle_points[1].y - quadrangle_points[3].y) * (quadrangle_points[0].x - quadrangle_points[3].x))

        #Если выполняется условие то точка внутри прямоугольника иначе нет
        if res1 >= 0 and res2 >= 0 and res3 >= 0 and res4 >= 0:
            if res1 == 0 or res2 == 0 or res3 == 0 or res4 == 0:
                #1 - точка на одной из сторон
                print("1")
            else:
                #2 - точка внутри
                print("2")
        else:
            # 3 - точка снаружи
            print("3")



