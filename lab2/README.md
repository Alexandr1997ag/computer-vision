1. Прямой поиск одного изображения на другом (template matching)
Представляет собой пошаговое сканирование шаблоном исходного изображения, причем на каждом шаге рассчитывается либо просто измеряется степень соответствия участка изображения существующему шаблону. Когда сканирование заканчивается, на изображении выделяется область, которая соответствует шаблону в большей степени.
скрипт template.py 
Результат работы алгоритма на примере:
![find_template_2](https://user-images.githubusercontent.com/87136289/198731603-fa25589a-d088-428e-ad06-cf38e4381668.png)
![find_template_3](https://user-images.githubusercontent.com/87136289/198731607-dba2a1c0-a1bb-4d73-8de6-77017e13d47a.png)
![find_template_4](https://user-images.githubusercontent.com/87136289/198731608-ac525ef6-4dd2-465b-a321-d1a229f583c7.png)
![find_template_5](https://user-images.githubusercontent.com/87136289/198731612-2a54431d-7784-4dd7-9c29-1119341c6324.png)
![find_template_6](https://user-images.githubusercontent.com/87136289/198731616-205639e0-ecac-4966-a686-a952b222c4ef.png)
![find_template_1](https://user-images.githubusercontent.com/87136289/198731600-1f584abd-2413-4181-90ca-ebd434f447d4.png)

2. Поиск ключевых точек эталона на входном изображении (например, с
помощью SIFT, ORB..)


ORB:
В отличие от SIFT - в открытом доступе. ORB представляет собой сочетание детектора ключевых точек FAST и дескриптора BRIEF с некоторыми дополнительными функциями для повышения производительности. FAST — это функция ускоренного сегментного теста , используемая для обнаружения функций на предоставленном изображении. Алгоритм FAST заключается в том, чтобы отсмотреть насколько светлее или темнее точки в окружности искомой. Для вычислительного ускорения сначала исследуются 4 точки вокруг искомой, если они одинаковы по яркости - берем следующую, если нет - берем и исследуем 16 точек вокруг искомой. После того, как особые точки найдены, вычисляют их дескрипторы, т.е. наборы признаков, характеризующие окрестность каждой особой точки. BRIEF – быстрый эвристический дескриптор, строится из 256 бинарных сравнений между яркостями пикселов на размытом изображении. 
![orb1](https://user-images.githubusercontent.com/87136289/198731873-bda3f4fb-c9ba-4a06-b883-6137639faecc.png)
![orb2](https://user-images.githubusercontent.com/87136289/198731892-347a33c2-4a56-4637-b8aa-7d7289692850.png)

SIFT:
Поиск кл точек заключается в прохождении алгоритма нескольких фаз - 1) потенциальные точки для исследования 2) Локализация с помощью Лапласиана и отсеяние лишних по пороговому значению 3) назначение ориентации ключевым точкам (через вычисление градиента окрестности) Дескриптор ключевого момента. Дескрипторы используются для сопоставления ключевых точек изображений. 

![sift1](https://user-images.githubusercontent.com/87136289/198731919-7b719570-4784-4fff-811a-cd4c642b7360.png)
![sift2](https://user-images.githubusercontent.com/87136289/198731941-537271e8-ca96-49c5-8708-860ae19d75c4.png)


Источники:
https://www.thepythoncode.com/article/sift-feature-extraction-using-opencv-in-python
https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html
https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
https://stackoverflow.com/questions/23180630/using-opencv-matchtemplate-for-blister-pack-inspection
https://vc.ru/dev/249864-poisk-izobrazheniy-po-fragmentu-s-pomoshchyu-orb
