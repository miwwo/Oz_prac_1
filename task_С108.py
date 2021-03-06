"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Person с полями имя, фамилия, возраст. Добавить конструктор класса.
Создать производный от Person класс Student. Новые поля: класс, дневник
    (словарь словарей вида предмет: {дата : отметка}). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления отметки в дневник, получения всех отметок по предмету,
    форматированной печати всего дневника. Переопределить метод преобразования в строку для печати
    основной информации (ФИ, возраст, класс).
Создать производный от Person класс Teacher. Новые поля: номер кабинета, преподаваемые
    предметы (словарь вида класс: список предметов). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения кабинета, добавления и удаления предмета. Переопределить метод преобразования
    в строку для печати основной информации (ФИ, возраст, номер кабинета, предметы).
Создать класс Class. Поля: номер rкласса, список класса (список экземпляров класса Student), классный руководитель
    (экземпляр класса Teacher). Определить конструктор. Переопределить метод преобразования в строку для печати
    всей информации о классе (с использованием переопределения в классах Teacher и Student). Переопределить
    методы получения количества учеников функцией len, получения ученика/учителя по индексу, изменения
    по индексу, удаления по индексу (0 индекс - учитель, начиная с 1 - ученики). Переопределить
    операции + и - для добавления или удаления ученика из группы. Добавить функцию создания txt-файла и записи
    всей информации в него (в том числе дневников учеников).
Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""