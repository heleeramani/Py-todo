# Py-todo
# Flask To-Do App

## 1. Clone the project

```bash
git clone <repository-url>
cd to-do-master
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

---

## 3. Activate Virtual Environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows (CMD)

```cmd
.venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Since this project uses Flask, if Flask is not included in `requirements.txt`, install it manually:

```bash
pip install flask
```

(Optional) Save the updated dependencies:

```bash
pip freeze > requirements.txt
```

---

## 5. Run the Application

```bash
python app.py
```

---

## 6. Open in Browser

```
http://127.0.0.1:5000
```

---

## 7. Test API

### Create Task

**POST**

```
http://127.0.0.1:5000/tasks
```

Body:

```json
{
    "title": "Learn Flask",
    "description": "Practice CRUD"
}
```

---

## If `python` command is not found

Run:

```bash
python3 app.py
```

or create an alias:

```bash
sudo apt install python-is-python3
```

---

## If Flask is not installed

```bash
pip install flask
```

---

## Deactivate Virtual Environment

```bash
deactivate
```

---

## Next Time You Open the Project

```bash
cd ~/Downloads/to-do-master
source .venv/bin/activate
python app.py
```