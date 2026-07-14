import sqlite3
from config import Config


def get_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def insert_file(filename, stored_filename, unique_code, file_size):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO files(filename, stored_filename, unique_code, file_size)
        VALUES(?,?,?,?)
    """, (filename, stored_filename, unique_code, file_size))

    conn.commit()
    conn.close()


def get_file(unique_code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM files WHERE unique_code=?", (unique_code,))
    data = cursor.fetchone()

    conn.close()
    return data


def increase_download(unique_code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE files
        SET download_count = download_count + 1
        WHERE unique_code=?
    """, (unique_code,))

    conn.commit()
    conn.close()


def get_all_files():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM files
        ORDER BY upload_time DESC
    """)

    data = cursor.fetchall()

    conn.close()
    return data

def get_dashboard_stats():
    conn = get_connection()
    cursor = conn.cursor()

    # Total Files
    cursor.execute("SELECT COUNT(*) FROM files")
    total_files = cursor.fetchone()[0]

    # Total Downloads
    cursor.execute("SELECT SUM(download_count) FROM files")
    result = cursor.fetchone()[0]
    total_downloads = result if result else 0

    # Total Storage
    cursor.execute("SELECT file_size FROM files")
    rows = cursor.fetchall()

    total_storage_kb = 0

    for row in rows:
        size = row["file_size"]

        if not size:
            continue

        if size.endswith("KB"):
            total_storage_kb += float(size.replace(" KB", ""))

        elif size.endswith("MB"):
            total_storage_kb += float(size.replace(" MB", "")) * 1024

        elif size.endswith("GB"):
            total_storage_kb += float(size.replace(" GB", "")) * 1024 * 1024

    if total_storage_kb >= 1024:
        storage = f"{total_storage_kb / 1024:.2f} MB"
    else:
        storage = f"{total_storage_kb:.2f} KB"

    # Latest Upload
    cursor.execute("""
        SELECT filename
        FROM files
        ORDER BY upload_time DESC
        LIMIT 1
    """)

    latest = cursor.fetchone()
    latest_upload = latest["filename"] if latest else "No uploads"

    conn.close()

    return {
        "total_files": total_files,
        "downloads": total_downloads,
        "storage": storage,
        "latest_upload": latest_upload,
    }

def delete_file(unique_code):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM files WHERE unique_code=?",
        (unique_code,)
    )

    conn.commit()
    conn.close()

def search_files(query):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM files
        WHERE filename LIKE ?
        ORDER BY upload_time DESC
    """, (f"%{query}%",))

    files = cursor.fetchall()

    conn.close()

    return files

def sort_files(sort_by):

    conn = get_connection()
    cursor = conn.cursor()

    if sort_by == "oldest":

        cursor.execute("""
            SELECT * FROM files
            ORDER BY upload_time ASC
        """)

    elif sort_by == "downloads":

        cursor.execute("""
            SELECT * FROM files
            ORDER BY download_count DESC
        """)

    else:

        cursor.execute("""
            SELECT * FROM files
            ORDER BY upload_time DESC
        """)


    files = cursor.fetchall()

    conn.close()

    return files