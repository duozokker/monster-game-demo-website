import sqlite3
from argon2 import PasswordHasher

#conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

def create_user(name, email, password, level= 0, role = "user", money = 0):
    #argon2 hash creation
    ph = PasswordHasher()
    new_password = ph.hash(name+password)


    #Database stuff
    conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

    c = conn.cursor()
    c.execute(f"INSERT INTO users VALUES ('{name}','{email}','{new_password}', {level}, '{role}', {money})")
    conn.commit()
    conn.close()

def create_monster(name, atk, defense, lp):
    conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

    c = conn.cursor()
    c.execute(f"INSERT INTO monsters (name, atk, def, lp)VALUES ('{name}', {atk} , {defense} , {lp} )")
    conn.commit()
    conn.close()

def add_monster(user_name, monster_id):
    conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

    c = conn.cursor()
    c.execute(f"INSERT INTO user_monsters VALUES ('{user_name}', {monster_id} )")
    conn.commit()
    conn.close()

def create_warp(name, price):
    conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

    c = conn.cursor()
    c.execute(f"INSERT INTO warp (name, price) VALUES ('{name}', {price} )")
    conn.commit()
    conn.close()

def add_monster_warp(warp_id, monsters_id):
    conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

    c = conn.cursor()
    c.execute(f"INSERT INTO warp_monsters VALUES ({warp_id}, {monsters_id} )")
    conn.commit()
    conn.close()

def users_data(username): #game
    conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

    c = conn.cursor()
    c.execute(f"SELECT name, level, money, role FROM users WHERE name = '{username}'")

    rows = c.fetchall()

    conn.close()

    return rows[0]

def login_user_db(username, password):    
    #db call
    conn = sqlite3.connect('/Users/leo/Desktop/monster game/database.db')

    c = conn.cursor()
    c.execute(f"SELECT password FROM users WHERE name = '{username}'")

    rows = c.fetchall()

    conn.close()

    try:
        returned_data = rows[0][0]
        try:
            ph = PasswordHasher()
            password_check = ph.verify(returned_data, username+password)
            if password_check == True:
                return "Successfully signed in :)"
            else:
                return "Something went wrong"
        except:
            return "Wrong password"
    except:
        return "This Username does not exist"


#create_user("leo2", "email2@email.com", "123")
#create_monster("demo", 100, 100, 100)
#print(users_data("leo"))

#print(login_user("duozokker", "1234567890"))