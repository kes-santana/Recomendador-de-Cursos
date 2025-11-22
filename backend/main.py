from create_curse_end_point import *
from recomend_curse_end_point import *

name = input("Por favor escriba su nombre:\n")
print()
while True:
    action: int = int(input("Escoja el numero de la accion que desea realizar: \n\t 1- Crear curso \n\t 2- Recomendar curso \n\t 3- Salir \n \n"))
    print()
    
    if action == 1:
        curse_name  = input("Introduzca el nombre del curso \n")
        print()
        curse_duration  = input("Introduzca la duracion del curso \n")
        print()
        tags = input("Introduzca los tags del curso \n")
        print()
        create_curse = CreateCurse(curse_name, curse_duration, tags)
        message = create_curse.create_curse()
        print(message)
        print()

    if action == 2:
        description = input("Por favor de una descripcion sobre el curso que desea \n")
        print()
        recommend_curse = RecommendCurse(name, description)
        match_curses = recommend_curse.recommend_curse()
        if len(match_curses)==0:
            print("No encontramos cursos que coincidan con su descripcion \n")
        message = "Dada su descripcion le ofrecemos los siguientes cursos: \n\t"
        print()

        for c in match_curses:
            message = f"{message} {c} \n\t"
        print(message)
        
    if action == 3:
        print("Vuelva pronto")
        break