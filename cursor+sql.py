import sqlite3

# 1. Подключение к базе данных (или создание, если её нет)
conn = sqlite3.connect('mydatabase.db')

# 2. Создание курсора
cursor = conn.cursor()

# 3. Создание таблицы (если её нет)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# 4. Вставка данных
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 40))
conn.commit()  # Сохраняем изменения в базе данных

# 5. Выборка данных с использованием курсора
cursor.execute("SELECT id, name, age FROM users WHERE age > ?", (27,))  # Выбираем пользователей старше 27 лет

# 6. Перебор результатов с использованием курсора
print("Users older than 27:")
for row in cursor:  # Cursor ведет себя как итератор
    user_id, name, age = row
    print(f"ID: {user_id}, Name: {name}, Age: {age}")

# 7. Пример обновления данных с использованием курсора (менее распространен, но возможен)
# cursor.execute("UPDATE users SET age = ? WHERE id = ?", (31, 1)) #Обновляем Alice
# conn.commit()

# 8. Закрытие курсора и соединения
cursor.close()
conn.close()