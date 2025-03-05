# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


### Класс 1: `Table`
    """ 
    Класс `Table` описывает стол как физическую сущность с такими характеристиками, как длина, ширина и материал изготовления.
    """

class Table:
    """
    Класс, представляющий стол.

    Атрибуты:
    ---------
    length : float
        Длина стола в метрах.
    width : float
        Ширина стола в метрах.
    material : str
        Материал, из которого изготовлен стол.

    Методы:
    -------
    set_size(length: float, width: float) -> None
        Устанавливает новые размеры стола.
    get_area() -> float
        Вычисляет площадь поверхности стола.
    change_material(new_material: str) -> None
        Изменяет материал стола.
    """

    def __init__(self, length: float, width: float, material: str) -> None:
        """
        Конструктор класса Table.
        Параметры:
        ----------
        length : float
            Длина стола в метрах.
        width : float
            Ширина стола в метрах.
        material : str
            Материал, из которого изготовлен стол.

        Ограничения:
        ------------
        Длина и ширина должны быть положительными числами.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина стола должны быть больше нуля.")
        self.length = length
        self.width = width
        self.material = material

    def set_size(self, length: float, width: float) -> None:
        """
        Устанавливает новые размеры стола.
        Параметры:
        ----------
        length : float
            Новая длина стола в метрах.
        width : float
            Новая ширина стола в метрах.
        Ограничения:
        ------------
        Длина и ширина должны быть положительными числами.
        Возвращаемое значение:
        -----------------------
        Нет.
        Примеры:
        --------
        >>> table = Table(1.5, 0.8, "Дерево")
        >>> table.set_size(2.0, 1.0)
        >>> table.length, table.width
        (2.0, 1.0)
        """
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина стола должны быть больше нуля.")
        self.length = length
        self.width = width

    def get_area(self) -> float:
        """
        Вычисляет площадь поверхности стола.

        Параметры:
        ----------
        Нет.

        Возвращаемое значение:
        -----------------------
        area : float
            Площадь стола в квадратных метрах.

        Примеры:
        --------
        >>> table = Table(1.5, 0.8, "Дерево")
        >>> table.get_area()
        1.2
        """
        return self.length * self.width

    def change_material(self, new_material: str) -> None:
        """
        Изменяет материал стола.

        Параметры:
        ----------
        new_material : str
            Новый материал для стола.

        Возвращаемое значение:
        -----------------------
        Нет.

        Примеры:
        --------
        >>> table = Table(1.5, 0.8, "Дерево")
        >>> table.change_material("Металл")
        >>> table.material
        'Металл'
        """
        self.material = new_material

    ### Класс 4: `Facebook`
    """  
    Класс `Facebook` описывает
    социальную сеть с акцентом на подписчиков, публикации и взаимодействие
    пользователей.
    """

    class Facebook:
        """
        Класс, представляющий социальную сеть Facebook.

        Атрибуты:
        ---------
        username : str
            Имя пользователя.
        followers_count : int
            Количество подписчиков.
        posts_count : int
            Количество публикаций.

        Методы:
        -------
        follow(user: str) -> None
            Подписывается на другого пользователя.
        unfollow(user: str) -> None
            Отписывается от другого пользователя.
        post(content: str) -> None
            Делает публикацию.
        like(post_id: int) -> None
            Ставит лайк на публикацию.
        comment(post_id: int, content: str) -> None
            Оставляет комментарий к публикации.
        """

        def __init__(self, username: str, followers_count: int = 0, posts_count: int = 0) -> None:
            """
            Конструктор класса Facebook.

            Параметры:
            ----------
            username : str
                Имя пользователя.
            followers_count : int
                Начальное количество подписчиков (по умолчанию 0).
            posts_count : int
                Начальное количество публикаций (по умолчанию 0).

            Ограничения:
            ------------
            Количество подписчиков и публикаций должно быть неотрицательными.
            """
            if followers_count < 0 or posts_count < 0:
                raise ValueError("Количество подписчиков и публикаций не может быть отрицательным.")
            self.username = username
            self.followers_count = followers_count
            self.posts_count = posts_count

        def follow(self, user: str) -> None:
            """
            Подписывается на другого пользователя.

            Параметры:
            ----------
            user : str
                Имя пользователя, на которого подписываются.

            Возвращаемое значение:
            -----------------------
            Нет.

            Примеры:
            --------
            >>> facebook = Facebook("john_doe")
            >>> facebook.follow("jane_smith")
            John Doe followed Jane Smith.
            """
            print(f"{self.username} followed {user}.")

        def unfollow(self, user: str) -> None:
            """
            Отписывается от другого пользователя.

            Параметры:
            ----------
            user : str
                Имя пользователя, от которого отписываются.

            Возвращаемое значение:
            -----------------------
            Нет.

            Примеры:
            --------
            >>> facebook = Facebook("john_doe")
            >>> facebook.unfollow("jane_smith")
            John Doe unfollowed Jane Smith.
            """
            print(f"{self.username} unfollowed {user}.")

        def post(self, content: str) -> None:
            """
            Делает публикацию.

            Параметры:
            ----------
            content : str
                Содержимое публикации.

            Возвращаемое значение:
            -----------------------
            Нет.

            Примеры:
            --------
            >>> facebook = Facebook("john_doe")
            >>> facebook.post("Hello, world!")
            John Doe posted: Hello, world!
            """
            self.posts_count += 1
            print(f"{self.username} posted: {content}")

        def like(self, post_id: int) -> None:
            """
            Ставит лайк на публикацию.

            Параметры:
            ----------
            post_id : int
                Идентификатор публикации, на которую ставится лайк.

            Возвращаемое значение:
            -----------------------
            Нет.

            Примеры:
            --------
            >>> facebook = Facebook("john_doe")
            >>> facebook.like(12345)
            John Doe liked post with ID 12345.
            """
            print(f"{self.username} liked post with ID {post_id}.")

class Stack:
    """
    Класс, представляющий стек.

    Атрибуты:
    ---------
    items : list
        Список элементов стека.

    Методы:
    -------
    push(item: Any) -> None
        Добавляет элемент в вершину стека.
    pop() -> Any
        Удаляет и возвращает последний добавленный элемент.
    peek() -> Any
        Возвращает верхний элемент стека без удаления.
    """

    def __init__(self) -> None:
        """
        Конструктор класса Stack.

        Параметры:
        ----------
        Нет.

        Ограничения:
        ------------
        Нет.
        """
        self.items = []

    def push(self, item: Any) -> None:
        """
        Добавляет элемент в вершину стека.

        Параметры:
        ----------
        item : Any
            Элемент, который добавляется в стек.

        Возвращаемое значение:
        -----------------------
        Нет.

        Примеры:
        --------
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.items
        [1, 2]
        """
        self.items.append(item)

    def pop(self) -> Any:
        """
        Удаляет и возвращает последний добавленный элемент.

        Параметры:
        ----------
        Нет.

        Возвращаемое значение:
        -----------------------
        item : Any
            Последний добавленный элемент.

        Примеры:
        --------
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.pop()
        2
        >>> stack.items
        [1]
        """
        if not self.items:
            raise IndexError("Стек пуст.")
        return self.items.pop()

    def peek(self) -> Any:
        """
        Возвращает верхний элемент стека без удаления.

        Параметры:
        ----------
        Нет.

        Возвращаемое значение:
        -----------------------
        item : Any
            Верхний элемент стека.

        Примеры:
        --------
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.peek()
        2
        >>> stack.items
        [1, 2]
        """
        if not self.items:
            raise IndexError("Стек пуст.")
        return self.items[-1]



pass
