import sqlite3

# Функция для создания таблиц
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Salespeople (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sname TEXT NOT NULL,
            city TEXT NOT NULL,
            comm REAL
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cname TEXT NOT NULL,
            city TEXT NOT NULL,
            rating INTEGER,
            id_sp INTEGER,
            FOREIGN KEY (id_sp) REFERENCES Salespeople(id)
        );
    ''')
    conn.commit()
    

# Функция для добавления записи о продавце
def add_salesperson(conn, sname, city, comm):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Salespeople (sname, city, comm) VALUES (?, ?, ?)
    ''', (sname, city, comm))
    conn.commit()
    print(f"Продавец {sname} добавлен!")
    

# Функция для добавления записи о заказчике
def add_customer(conn, cname, city, rating, id_sp):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Customers (cname, city, rating, id_sp) VALUES (?, ?, ?, ?)
    ''', (cname, city, rating, id_sp))
    conn.commit()
    print(f"Заказчик {cname} добавлен!")
    

# Функция для удаления всех записей
def delete_all(conn):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Salespeople;')
    cursor.execute('DELETE FROM Customers;')
    conn.commit()
    

# Основная функция
def main():
    conn = sqlite3.connect('Seller_and_buyer.db')
    create_tables(conn)

    while True:
        print("Меню:\n"
        "1 - Добавить продавца\n"
        "2 - Добавить заказчика\n"
        "3 - Удалить все записи\n"
        "4 - Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            sname = input("Введите имя продавца: ")
            city = input("Введите город: ")
            comm = float(input("Введите комиссионные: "))
            add_salesperson(conn, sname, city, comm)
        elif choice == '2':
            cname = input("Введите имя заказчика: ")
            city = input("Введите город: ")
            rating = int(input("Введите рейтинг: "))
            id_sp = int(input("Введите номер продавца: "))
            add_customer(conn, cname, city, rating, id_sp)
        elif choice == '3':
            delete_all(conn)
            print('Все записи удалены.')
            choice2 = input('Хотите заново заполнить данные? (да/нет): ').lower()
            if choice2 != 'да':
                break
        elif choice == '4':
            print('Выход из программы.')
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из меню.")

    conn.close()

if __name__ == "__main__":
    main()