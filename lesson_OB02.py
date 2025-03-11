class User:
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут ID
        self._name = name  # Защищенный атрибут имени
        self._access_level = 'user'  # По умолчанию уровень доступа обычного сотрудника

    def get_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def __str__(self):
        return f"User[ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}]"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа администратора

    def add_user(self, user_list, user):
        """Добавляет нового пользователя в список"""
        user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user_list, user_id):
        """Удаляет пользователя по ID"""
        for user in user_list:
            if user.get_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь не найден.")

    def __str__(self):
        return f"Admin[ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}]"


# Создание списка пользователей
users = []

# Создание админа
admin = Admin(1, "Alice")

# Добавление пользователей
user1 = User(2, "Bob")
user2 = User(3, "Charlie")
admin.add_user(users, user1)
admin.add_user(users, user2)

# Вывод списка пользователей
print("\nСписок пользователей:")
for user in users:
    print(user)

# Удаление пользователя
admin.remove_user(users, 2)

# Вывод списка пользователей после удаления
print("\nОбновленный список пользователей:")
for user in users:
    print(user)
