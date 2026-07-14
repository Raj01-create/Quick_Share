import os
import uuid
from werkzeug.utils import secure_filename


def save_file(file, upload_folder):

    original_filename = secure_filename(file.filename)

    unique_filename = f"{uuid.uuid4().hex[:8]}_{original_filename}"

    filepath = os.path.join(upload_folder, unique_filename)

    file.save(filepath)

    return original_filename, unique_filename


def get_file_size(filepath):
    return os.path.getsize(filepath)