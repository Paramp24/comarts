import sqlite3

class UserAuthentication:
    # this function will take in a database name and define it as a class characteristic
    def __init__(self):
        self.userDataBase = 'user_info.db'
    
    # adds user to data base if not part of the data base
    def user_loader(self, loginInfo):

        data = []
        phone_number = loginInfo[0]
        
        if len(loginInfo) == 2:   # signing up
            username = loginInfo[1]
            data = [phone_number, username]
            
            phone_number_result = self.searchUserDatabase(data[0])
            username_result = self.searchUserDatabase(data[1])

            if phone_number_result or username_result:
                return False
            else:
                self.addToUserDataBase(data[0], data[1])
                return True

        else:   # signing in

            data = [phone_number]
            user_name_result = self.searchUserDatabase(phone_number)

            if user_name_result:
                return True
            else:
                return False

    #accctually adds user to data base after signing up     
    def addToUserDataBase(self, phone_number, username):
        
        userDB = sqlite3.connect('user_info.db')
        cursor = userDB.cursor()

        data = [(phone_number, username)]

        cursor.executemany("INSERT INTO users VALUES(?, ?)", data)
        userDB.commit()  # Remember to commit the transaction after executing INSERT.
        userDB.close()

    # checks for query in database with the intention of logging in
    def searchUserDatabase(self, loginInfo):
        
        userDB = sqlite3.connect(self.userDataBase)
        cursor = userDB.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (phone_number STRING UNIQUE, username STRING UNIQUE)''')

        try:
            phone_number = int(loginInfo)
            cursor.execute('SELECT * FROM users WHERE phone_number=:c', {'c': phone_number})
        except ValueError:
            cursor.execute('SELECT * FROM users WHERE username=:c', {'c': loginInfo})

        user_search = cursor.fetchone()
        userDB.close()
        return user_search
