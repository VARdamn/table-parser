'''
CREATE TABLE specializations (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    code TEXT UNIQUE,
);'''

'''CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    group_name TEXT NOT NULL,
    group_code TEXT NOT NULL UNIQUE,
    specialization_id INTEGER REFERENCES specializations(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);'''

'''CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    code TEXT UNIQUE,
);'''

'''CREATE TABLE group_subjects (
    group_id INTEGER NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
    subject_id INTEGER NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    PRIMARY KEY (group_id, subject_id)
);'''

'''CREATE TABLE reports (
    id SERIAL PRIMARY KEY AUTOINCREMENT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100),
    filename TEXT,
    file_hash VARCHAR(64) UNIQUE
);'''

'''CREATE TABLE report_entries (
    id SERIAL PRIMARY KEY,
    report_id INTEGER NOT NULL REFERENCES reports(id) ON DELETE CASCADE,
    row_number INTEGER NOT NULL,
    group_id INTEGER REFERENCES groups(id),
    specialization_id INTEGER REFERENCES specializations(id),
    subject_id INTEGER REFERENCES subjects(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(report_id, row_number)
);'''

'''
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    short_name TEXT,
    employee_number TEXT UNIQUE
);
'''

'''
CREATE TABLE teacher_assigned (
    id SERIAL PRIMARY KEY,
    type TEXT,
    teacher_id INTEGER NOT NULL REFERENCES teachers(id) ON DELETE CASCADE,
    group_id INTEGER NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
    subject_id INTEGER NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    UNIQUE (type, teacher_id, group_id, subject_id)
);
'''

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "excel_reports_db"
DB_USER = "postgres"
DB_PASSWORD = "rootroot"
DB_HOST = "localhost"
DB_PORT = "5432"

def create_database():
    try:
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(DB_NAME))
            )

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error initializing db: {e}")

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS reports (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_by VARCHAR(100),
            original_filename TEXT,
            file_hash VARCHAR(64) UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS specializations (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            code TEXT UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            group_name TEXT NOT NULL,
            group_code TEXT NOT NULL UNIQUE,
            specialization_id INTEGER REFERENCES specializations(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT TRUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS subjects (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            code TEXT UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS group_subjects (
            group_id INTEGER NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
            subject_id INTEGER NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
            PRIMARY KEY (group_id, subject_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS report_entries (
            id SERIAL PRIMARY KEY,
            report_id INTEGER NOT NULL REFERENCES reports(id) ON DELETE CASCADE,
            row_number INTEGER NOT NULL,
            group_id INTEGER REFERENCES groups(id),
            specialization_id INTEGER REFERENCES specializations(id),
            subject_id INTEGER REFERENCES subjects(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(report_id, row_number)
        )
        """
    )
    
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        
        for command in commands:
            cursor.execute(command)
        
        conn.commit()
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    create_database()
    create_tables()