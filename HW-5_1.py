class HashTable:
    def __init__(self, size):
        """
        Ініціалізація хеш-таблиці.
        :param size: Розмір таблиці (кількість бакетів).
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Створюємо список бакетів

    def hash_function(self, key):
        """
        Хеш-функція для визначення індексу бакета.
        :param key: Ключ, який потрібно хешувати.
        :return: Індекс бакета.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Додавання пари ключ-значення в хеш-таблицю.
        :param key: Ключ.
        :param value: Значення.
        """
        key_hash = self.hash_function(key)
        key_value = [key, value]

        for pair in self.table[key_hash]:
            if pair[0] == key:  # Оновлення значення, якщо ключ вже існує
                pair[1] = value
                return True

        # Якщо ключа немає, додаємо нову пару
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        """
        Пошук значення за ключем у хеш-таблиці.
        :param key: Ключ.
        :return: Значення або None, якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]  # Повертаємо знайдене значення
        return None  # Якщо ключ не знайдено

    def delete(self, key):
        """
        Видалення пари ключ-значення з хеш-таблиці.
        :param key: Ключ, який потрібно видалити.
        :return: True, якщо видалення успішне, або False, якщо ключ не знайдено.
        """
        key_hash = self.hash_function(key)
        for index, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:  # Знаходимо ключ і видаляємо пару
                del self.table[key_hash][index]
                return True  # Видалення успішне
        return False  # Ключ не знайдено

# Тестування хеш-таблиці
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("Значення за ключем 'apple':", H.get("apple"))   # Виведе: 10
print("Значення за ключем 'orange':", H.get("orange"))  # Виведе: 20
print("Значення за ключем 'banana':", H.get("banana"))  # Виведе: 30

# Видалення ключа
print("Видалення ключа 'orange':", H.delete("orange"))  # Виведе: True
print("Значення за ключем 'orange' після видалення:", H.get("orange"))  # Виведе: None

# Спроба видалити неіснуючий ключ
print("Видалення ключа 'grape':", H.delete("grape"))  # Виведе: False
