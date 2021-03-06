"""
Необходимо реализовать классы Color и RGB
для работы с данными о цвете в разных форматах

Классы должны содержать информацию:
- название цвета (строка)
- обозначение в виде RGB и RGBA (дополнительные классы, как типы данных)
- представление в виде HEX (можно сделать динамическое property через геттер и сеттер)

Классы должны поддерживать операции:
- сложение Color с RGB, пример: Color('red') + RGB(0, 20, 0)
- сложение RGB с другим объектом RGB, пример: Color('red') + Color('blue')
- вычитание (аналогично сложению), пример: Color('green') - RGB(0, 255, 0)

Классы должны иметь конструкторы:
- создание цвета по названию, пример: my_color = Color('red')
- создание цвета по HEX, пример: my_color = Color('#ec20ce')
- создание цвета по RGB, пример: my_color = Color(RGB(56, 134, 255))

* При работе с RGB и RGBA необходимо учесть, что значения могут быть от 0 до 255 для RGB и от 0 до 1 для Alpha
"""
