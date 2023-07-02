import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        muscle_group TEXT,
        video_link TEXT
    )
''')

muscle_group = "Chest.m, Chest.w, Back.m, Back.w, Arms.m, Arms.w, Legs.m, Legs.w, Shoulders.m, Shoulders.w"
video_link = ""

cursor.execute("INSERT INTO exercises (muscle_group, video_link) VALUES ('Chest.m', 'https://www.youtube.com/watch?v=Vf2evnGKTfo')")
cursor.execute("INSERT INTO exercises (muscle_group, video_link) VALUES ('Back.m', 'https://www.youtube.com/watch?v=ni4qZejmb3I')")
cursor.execute("INSERT INTO exercises (muscle_group, video_link) VALUES ('Arms.m', 'https://www.youtube.com/watch?v=NsHsuqd-B2Y')")
cursor.execute("INSERT INTO exercises (muscle_group, video_link) VALUES ('Legs.m', 'https://www.youtube.com/watch?v=KF6_2hRFtq4')")
cursor.execute("INSERT INTO exercises (muscle_group, video_link) VALUES ('Shoulders.m', 'https://www.youtube.com/watch?v=0N_SmoM3UQc')")


cursor.execute("SELECT * FROM exercises")
rows = cursor.fetchall()

for row in rows:
    print(row)
# Сохраняем изменения и закрываем подключение
conn.commit()
conn.close()