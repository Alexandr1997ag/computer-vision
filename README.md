# computer-vision
сделать картиночки, переделать время. сравнить результат работы нумпай и опенсв вычесть одну из другой. 
UPDATE: 
1. загрузил фото результатов работы каждого алгоритма. 
2. Провел сравнительный анализ работы алгоритмов на numpy и на opencv. Для работы использовался скрипт dif.py (загружен дополнительно).
Фотографии в самом конце отчета. 


Эквализация гистограммы. На вход поступает видео, программа на
выходе отрисовывает два окна: с рассчитанной гистограммой и
изображением. По нажатию определенной кнопки на клавиатуре
изображение должно переключаться между исходным и после
эквализации. Базовый алгоритм - эквализация гистограммы.


Мной было разработано 4 скрипта: 
1. screen.py - для работы по захвату видео и сохранению скриншота
2. все остальные - алгоритмы эквализации с помощью numpy, numba, opencv.

Эквализация, это просто процедура выравнивания гистограммы изображения, путем воздействия (т.е. коррекции) яркости отдельных пикселей.

Один из методов - найти самые яркие и самые темные значения пикселей в изображении и сопоставить их с чистым белым и чистым черным. Другой метод - найти среднее значение значений пикселей в изображении как промежуточное значение серого, а затем расширить диапазон для достижения максимально полного отображаемого значения.

Глобально - мы находим функцию отображения выходного от входного сигнала, затем эквализируем нашу гистограмму по функции отображения. 

время работы каждого алгоритма:
numba - 05.420805
numpy - 03.359753
opencv - 03.351171

результат работы numba
![numba_2](https://user-images.githubusercontent.com/87136289/198679262-c9f7f5f1-e0ea-4292-a341-8c8042f1342d.png)
![numba_1](https://user-images.githubusercontent.com/87136289/198679229-3a7e1f0a-1d55-485b-9caa-09ee4e2a1f05.png)

результат работы numpy

![numpy_1](https://user-images.githubusercontent.com/87136289/198679437-64f63833-2e5b-4327-b308-ed400bcb1396.png)
![numpy_2](https://user-images.githubusercontent.com/87136289/198679583-ae0472bd-38e3-4b21-a5fd-43735b508eb2.png)


результат работы opencv


![open_cv1](https://user-images.githubusercontent.com/87136289/198680061-0ecbce58-576b-4d28-af44-b43ec8106aea.png)
![open_cv2](https://user-images.githubusercontent.com/87136289/198680064-65591182-4676-4cb1-87d9-fd31d5ed9a3b.png)


Результат сравнения работы двух алгоритмов:
![dif](https://user-images.githubusercontent.com/87136289/198683354-eb9b17b5-522b-4074-92a5-2ad3bc38cb58.png)


Источники - https://russianblogs.com/article/17011016846/
https://numba.pydata.org/numba-examples/examples/density_estimation/histogram/results.html
https://numba.pydata.org/numba-doc/latest/index.html  
https://docs.opencv.org/4.x/


