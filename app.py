import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from config import Config

from flask import flash
from database.init_db import create_database

from utils.database import (
    insert_file,
    get_file,
    increase_download,
    get_all_files,
    get_dashboard_stats,
    delete_file,
    search_files,
    sort_files
)

from utils.helper import (
    generate_unique_code,
    format_file_size,allowed_file
)

from utils.file_manager import (
    save_file,
    get_file_size
)

from utils.qr_generator import generate_qr


app = Flask(__name__)
app.config.from_object(Config)

# Create folders if not exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["QR_FOLDER"], exist_ok=True)
os.makedirs(os.path.join(os.path.dirname(__file__), "database"), exist_ok=True)

# Create Database
create_database()


@app.route("/")
def home():
    stats = get_dashboard_stats()

    return render_template(
        "index.html",
        stats=stats
    )

@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return redirect(url_for("home"))

    file = request.files["file"]

    if file.filename == "":
        return redirect(url_for("home"))

    # -------- Allowed File Validation --------
    if not allowed_file(file.filename, Config.ALLOWED_EXTENSIONS):
        flash(
            "Unsupported file type. Please upload a supported file.",
            "danger"
        )
        return redirect(url_for("home"))
    # ----------------------------------------

    original_filename, stored_filename = save_file(
        file,
        app.config["UPLOAD_FOLDER"]
    )

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        stored_filename
    )

    filesize = format_file_size(get_file_size(filepath))

    unique_code = generate_unique_code()

    insert_file(
        original_filename,
        stored_filename,
        unique_code,
        filesize
    )

    download_link = request.host_url + "download/" + unique_code

    generate_qr(
        download_link,
        unique_code,
        app.config["QR_FOLDER"]
    )

    return render_template(
        "upload_success.html",
        filename=original_filename,
        code=unique_code,
        link=download_link
    )

@app.route("/download/<code>")
def download(code):

    file = get_file(code)

    if not file:
        return render_template("404.html")

    increase_download(code)

    return render_template(
        "download.html",
        file=file
    )

@app.route("/qr/<filename>")
def qr_image(filename):
    return send_from_directory(
        app.config["QR_FOLDER"],
        filename
    )

@app.route("/file/<filename>")
def file_download(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename,
        as_attachment=True
    )


@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/delete/<code>")
def delete(code):

    file = get_file(code)

    if not file:
        return render_template("404.html")


    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file["stored_filename"]
    )


    qr_path = os.path.join(
        app.config["QR_FOLDER"],
        code + ".png"
    )


    if os.path.exists(file_path):
        os.remove(file_path)


    if os.path.exists(qr_path):
        os.remove(qr_path)


    delete_file(code)


    flash(
        "File deleted successfully!",
        "success"
    )


    return redirect(url_for("history"))


@app.route("/history")
def history():

    query = request.args.get("search")
    sort = request.args.get("sort")


    if query:
        files = search_files(query)

    elif sort:
        files = sort_files(sort)

    else:
        files = get_all_files()


    return render_template(
        "history.html",
        files=files
    )

if __name__ == "__main__":
    app.run(debug=True)