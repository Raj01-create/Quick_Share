# Quick_Share
A QR-based file sharing platform built with **Python Flask** that allows users to upload files, generate unique sharing links, and share files instantly using QR codes.
QuickShare provides a simple and fast way to transfer files without requiring user accounts. Users can upload a file, get a unique download link, and share it through a QR code.


## 📸 Screenshots
<img width="830" height="457" alt="Screenshot 2026-07-15 041754" src="https://github.com/user-attachments/assets/92f3e6e0-9a30-4c72-9582-4a419a3fcfc0" />
<img width="749" height="359" alt="Screenshot 2026-07-15 041916" src="https://github.com/user-attachments/assets/ac6ddfec-bb82-42b5-9d79-7cd87ea27f1e" />
<img width="769" height="435" alt="Screenshot 2026-07-15 041814" src="https://github.com/user-attachments/assets/c430db13-eb8e-4aad-b5fd-17328b27c260" />


## ✨ Features

* 📁 Easy file upload system
* 🔗 Unique file-sharing links
* 📱 QR code generation for quick sharing
* 📥 Direct file download
* 📊 Download tracking
* 🗂️ File history management
* 🔍 Search and sorting functionality
* 🛡️ Secure file handling
* ⚡ Simple and user-friendly interface


## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

### Database

* SQLite

### Python Libraries

* Flask
* qrcode
* Pillow
* Werkzeug

---

## 🏗️ Project Structure
```
QuickShare/
│
├── app.py                 # Main Flask application
├── config.py              # Application configuration
├── requirements.txt       # Project dependencies
├── README.md
├── LICENSE
│
├── database/
│   └── quickshare.db      # SQLite database
│
├── utils/
│   ├── database.py        # Database operations
│   ├── file_manager.py    # File handling logic
│   ├── helper.py          # Helper functions
│   └── qr_generator.py    # QR code generation
│
├── templates/             # HTML templates
│
└── static/
    ├── css/               # Stylesheets
    └── js/                # JavaScript files

```
## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
https://github.com/Raj01-create/Quick_Share.git
```

### 2. Navigate to project directory

```bash
cd quickshare
```

### 3. Create virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```


## 🔄 How It Works

1. User uploads a file.
2. QuickShare stores the file securely.
3. A unique sharing link is generated.
4. A QR code is created for that link.
5. Anyone with the link or QR code can download the file.

---

## 🚀 Future Improvements

* User authentication system
* Cloud storage integration
* File expiration feature
* Password-protected sharing
* File encryption
* Mobile application support

---

## 🌐 Live Demo

Coming soon:


## 👨‍💻 Author

Rajendra pal

## 📄 License

This project is licensed under the MIT License.
