import sqlite3

def create_table():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS loja(
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER   
            )
        '''
    )
    conn.commit()
    conn.close()

def adicionar_produto():
    name = input('write the product name: ').lower()
    price = input('product price: ')

    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
            INSERT INTO loja(name, price) \
            VALUES (?, ?)
        ''', (name, price)
    )
    conn.commit()

def listar_produtos():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
            SELECT * FROM loja
        '''
    )
    conn.commit()
    loja = cursor.fetchall()
    for produtos in loja:
        print(produtos)
    conn.close()

create_table()
adicionar_produto()
listar_produtos()
