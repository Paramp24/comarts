import sqlite3

class postAds():
    def __init__(self):
        pass

'''
    CREATE TABLE IF NOT EXISTS postingData (
            posting_user_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
            file_data_1 BLOB,
            file_data_2 BLOB,
            file_data_3 BLOB,
            file_data_4 BLOB,
            file_data_5 BLOB,
            text_input1 TEXT,
            text_input2 TEXT,
            text_input3 TEXT,
            text_input4 TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
'''