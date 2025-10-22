import sqlite3

def connection():
    try:
        db = sqlite3.connect("database.db")

        db.execute('''
            CREATE TABLE IF NOT EXISTS hosts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   host_name VARCHAR(30) UNIQUE NOT NULL,
                   system_name VARCHAR(30),
                   system_description VARCHAR(30),
                   system_arquitecture VARCHAR(20),
                   total_of_cores INT,
                   total_of_threads INT,
                   total_of_memory VARCHAR(30),
                   discs VARCHAR(300),
                   data_log DATETIME
                   );
        ''')

        db.execute('''
                   CREATE TABLE IF NOT EXISTS sistem_monitor(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cpu_usage_porcentage VARCHAR(10), 
                        memory_usage_porcentage VARCHAR(10), 
                        total_of_memory_used VARCHAR(10), 
                        send_bytes INT, 
                        received_bytes INT,
                        host_name NOT NULL,
                        data_log DATETIME,
                        CONSTRAINT fk_host FOREIGN KEY(host_name) REFERENCES hosts(host_name)
                   
                   );
                   ''')


        db.commit()
        return db
    except(sqlite3.Error) as err:
        print(err)