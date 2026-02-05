import doctest
from abc import ABC, abstractmethod


class Book(ABC):
    """
    Абстрактный класс, описывающий книгу.
    """

    def __init__(self, title: str, page_count: int, publication_year: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param page_count: Количество страниц
        :param publication_year: Год публикации

        Примеры:
        >>> book = Book("Война и мир", 1225, 1869)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.page_count = page_count

        if not isinstance(publication_year, int):
            raise TypeError("Год публикации должен быть целым числом")
        if publication_year < 0 or publication_year > 2100:
            raise ValueError("Год публикации должен быть в разумных пределах")
        self.publication_year = publication_year

    @abstractmethod
    def get_reading_time(self, reading_speed: int) -> float:
        """
        Расчет времени прочтения книги

        :param reading_speed: Скорость чтения (страниц в час)
        :return: Время прочтения в часах

        Примеры:
        >>> book = Book("Война и мир", 1225, 1869)
        >>> book.get_reading_time(50)
        """
        ...

    @abstractmethod
    def get_age(self, current_year: int) -> int:
        """
        Расчет возраста книги

        :param current_year: Текущий год
        :return: Возраст книги в годах

        Примеры:
        >>> book = Book("Война и мир", 1225, 1869)
        >>> book.get_age(2024)
        """
        ...

    @abstractmethod
    def is_classic(self) -> bool:
        """
        Проверка, является ли книга классикой
        (возраст более 100 лет)

        :return: Является ли книга классикой

        Примеры:
        >>> book = Book("Война и мир", 1225, 1869)
        >>> book.is_classic()
        """
        ...


class Smartphone(ABC):
    """
    Абстрактный класс, описывающий смартфон.
    """

    def __init__(self, brand: str, battery_capacity_mah: int, storage_gb: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param battery_capacity_mah: Емкость аккумулятора в mAh
        :param storage_gb: Объем памяти в гигабайтах

        Примеры:
        >>> phone = Smartphone("Samsung", 5000, 256)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not brand.strip():
            raise ValueError("Бренд не может быть пустым")
        self.brand = brand

        if not isinstance(battery_capacity_mah, int):
            raise TypeError("Емкость аккумулятора должна быть целым числом")
        if battery_capacity_mah <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительной")
        self.battery_capacity_mah = battery_capacity_mah

        if not isinstance(storage_gb, int):
            raise TypeError("Объем памяти должен быть целым числом")
        if storage_gb <= 0:
            raise ValueError("Объем памяти должен быть положительным")
        self.storage_gb = storage_gb

    @abstractmethod
    def estimate_battery_life(self, screen_on_hours: float) -> float:
        """
        Оценка времени работы от аккумулятора

        :param screen_on_hours: Время работы экрана в часах
        :return: Общее время работы в часах

        Примеры:
        >>> phone = Smartphone("Samsung", 5000, 256)
        >>> phone.estimate_battery_life(5.0)
        """
        ...

    @abstractmethod
    def has_enough_storage(self, required_gb: int) -> bool:
        """
        Проверка, достаточно ли памяти для указанного объема

        :param required_gb: Требуемый объем памяти в гигабайтах
        :return: Достаточно ли памяти

        Примеры:
        >>> phone = Smartphone("Samsung", 5000, 256)
        >>> phone.has_enough_storage(128)
        """
        ...

    @abstractmethod
    def is_premium_brand(self) -> bool:
        """
        Проверка, является ли бренд премиальным

        :return: Является ли бренд премиальным

        Примеры:
        >>> phone = Smartphone("Samsung", 5000, 256)
        >>> phone.is_premium_brand()
        """
        ...


class SocialNetworkAccount(ABC):
    """
    Абстрактный класс, описывающий аккаунт в социальной сети.
    """

    def __init__(self, username: str, registration_year: int, friends_count: int):
        """
        Создание и подготовка к работе объекта "Аккаунт в социальной сети"

        :param username: Имя пользователя
        :param registration_year: Год регистрации
        :param friends_count: Количество друзей

        Примеры:
        >>> account = SocialNetworkAccount("john_doe", 2018, 350)
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой")
        if len(username) < 3:
            raise ValueError("Имя пользователя должно содержать минимум 3 символа")
        self.username = username

        if not isinstance(registration_year, int):
            raise TypeError("Год регистрации должен быть целым числом")
        if registration_year < 2000 or registration_year > 2100:
            raise ValueError("Год регистрации должен быть в разумных пределах")
        self.registration_year = registration_year

        if not isinstance(friends_count, int):
            raise TypeError("Количество друзей должно быть целым числом")
        if friends_count < 0:
            raise ValueError("Количество друзей не может быть отрицательным")
        self.friends_count = friends_count

    @abstractmethod
    def calculate_account_age(self, current_year: int) -> int:
        """
        Расчет возраста аккаунта

        :param current_year: Текущий год
        :return: Возраст аккаунта в годах

        Примеры:
        >>> account = SocialNetworkAccount("john_doe", 2018, 350)
        >>> account.calculate_account_age(2024)
        """
        ...

    @abstractmethod
    def is_popular(self, threshold: int = 500) -> bool:
        """
        Проверка, является ли аккаунт популярным

        :param threshold: Пороговое значение друзей для популярности
        :return: Является ли аккаунт популярным

        Примеры:
        >>> account = SocialNetworkAccount("john_doe", 2018, 350)
        >>> account.is_popular(500)
        """
        ...

    @abstractmethod
    def can_send_message(self, recipient_online: bool, mutual_friends: int) -> bool:
        """
        Проверка, можно ли отправить сообщение пользователю

        :param recipient_online: Онлайн ли получатель
        :param mutual_friends: Количество общих друзей
        :return: Можно ли отправить сообщение

        Примеры:
        >>> account = SocialNetworkAccount("john_doe", 2018, 350)
        >>> account.can_send_message(True, 15)
        """
        ...


if __name__ == "__main__":
    # Тестирование с помощью doctest
    doctest.testmod(verbose=True)

    # Проверка создания объектов (вызовет ошибки, так как классы абстрактные)
    try:
        book = Book("Война и мир", 1225, 1869)
    except TypeError as e:
        print(f"Невозможно создать экземпляр абстрактного класса Book: {e}")

    try:
        phone = Smartphone("Samsung", 5000, 256)
    except TypeError as e:
        print(f"Невозможно создать экземпляр абстрактного класса Smartphone: {e}")

    try:
        account = SocialNetworkAccount("john_doe", 2018, 350)
    except TypeError as e:
        print(f"Невозможно создать экземпляр абстрактного класса SocialNetworkAccount: {e}")
