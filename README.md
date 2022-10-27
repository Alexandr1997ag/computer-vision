# computer-vision

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



