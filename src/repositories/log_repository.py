from ..helpers.db_connection import connection
import sqlite3

def select_all_hosts():
    sql = f'''
        SELECT * From hosts;
    '''

    conn = connection()
    cursor = conn.cursor()

    cursor.row_factory = sqlite3.Row

    cursor.execute(sql)

    res = cursor.fetchall()
    
    if(res is not None): 
        return res
    
    return []

def select_host(host_name: str):
    sql = f'''
        SELECT * FROM hosts where host_name = ?;
    '''

    conn = connection()
    cursor = conn.cursor()

    cursor.execute(sql, (host_name,))

    res = cursor.fetchone()
    
    if(res is not None): 
        return res
    
    return None

def insert_log(data: dict):

    host = select_host(data['conf']['system_name'])

    conn = connection()
    cursor = conn.cursor()

    if not host:
        sql_new_host = f'''
            INSERT INTO hosts
            (host_name, system_name, system_description, system_arquitecture, total_of_cores, total_of_threads, total_of_memory)
            VALUES
            (?, ?, ?, ?, ?, ?, ?);
        '''

        cursor.execute(sql_new_host, (data['conf']['system_name'], data['system_infor']['system'], data['system_infor']['arquitecture'], data['system_infor']['total_of_cores'], data['system_infor']['total_of_threads'], data['system_infor']['total_of_threads'], data['system_infor']['total_of_memory']))

        conn.commit()

    sql = f'''
        INSERT INTO sistem_monitor
        (host_name, cpu_usage_porcentage, memory_usage_porcentage, total_of_memory_used, send_bytes, received_bytes, data_log)
        VALUES
        (?, ?, ?, ?, ?, ?, ?);
    '''

    cursor.execute(sql, (data['conf']['system_name'], data['log']['cpu_usage_porcentage'], data['log']['memory_usage_porcentage'], data['log']['total_of_memory_used'], data['log']['internet_bytes_enviados'], data['log']['internet_bytes_recebidos'], data['log']['date_time'],))

    conn.commit()
    cursor.close()
    conn.close()

# Metodo responsável por buscar todos os logs 
def select_logs(host_name: str):
    sql = '''
            SELECT * FROM system_monitor WHERE host_name = ?;
        '''
    
    conn = connection()
    cursor = conn.cursor()

    cursor.row_factory = sqlite3.Row

    cursor.execute(sql, (host_name,))

    res = cursor.fetchall()