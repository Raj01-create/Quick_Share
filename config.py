import os

# Base Project Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "quickshare-secret-key"

    # Upload Folder
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

    # QR Code Folder
    QR_FOLDER = os.path.join(BASE_DIR, "qrcodes")

    # SQLite Database
    DATABASE = os.path.join(BASE_DIR, "database", "quickshare.db")

    # Maximum Upload Size (100 MB)
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024

    # Allowed File Types
    
    ALLOWED_EXTENSIONS = {
        "pdf", "png", "jpg", "jpeg",
        "doc", "docx",
        "ppt", "pptx",
        "xls", "xlsx",
        "zip", "rar",
        "txt", "mp4", "mp3"
    }