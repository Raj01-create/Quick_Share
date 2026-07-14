import uuid


def generate_unique_code():
    return uuid.uuid4().hex[:8]


def format_file_size(size):
    if size < 1024:
        return f"{size} Bytes"

    elif size < 1024 * 1024:
        return f"{round(size / 1024, 2)} KB"

    elif size < 1024 * 1024 * 1024:
        return f"{round(size / (1024 * 1024), 2)} MB"

    else:
        return f"{round(size / (1024 * 1024 * 1024), 2)} GB"
    
def allowed_file(filename, allowed_extensions):
    """
    Check whether the uploaded file extension is allowed.
    """

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )