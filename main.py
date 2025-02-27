from fastapi import FastAPI
import json
import os
import datetime

app = FastAPI()

# 📌 Verzeichnis für JSON-Dateien
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 🔹 JSON-Datei laden
def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# 🔹 JSON-Datei speichern
def save_json(filename, data):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# ✅ 📌 CHARAKTER ABRUFEN & SPEICHERN
@app.get("/get_character")
def get_character():
    return load_json("charakter.json")

@app.post("/update_character")
def update_character(new_data: dict):
    data = load_json("charakter.json")
    data.update(new_data)
    save_json("charakter.json", data)
    return {"status": "updated", "data": new_data}

# ✅ 📌 DENKMUSTER ABRUFEN & SPEICHERN
@app.get("/get_thinking_patterns")
def get_thinking_patterns():
    return load_json("denkmuster.json")

@app.post("/update_thinking_patterns")
def update_thinking_patterns(new_data: dict):
    data = load_json("denkmuster.json")
    today = datetime.date.today().isoformat()

    if today in data:
        data[today].append(new_data)
    else:
        data[today] = [new_data]

    save_json("denkmuster.json", data)
    return {"status": "updated", "data": new_data}

# ✅ 📌 REFLEXION ABRUFEN & SPEICHERN
@app.get("/get_reflection")
def get_reflection():
    return load_json("reflexion.json")

@app.post("/update_reflection")
def update_reflection(new_data: dict):
    data = load_json("reflexion.json")
    today = datetime.date.today().isoformat()

    if today in data:
        data[today].append(new_data)
    else:
        data[today] = [new_data]

    save_json("reflexion.json", data)
    return {"status": "updated", "data": new_data}

# ✅ 📌 SELBSTBEOBACHTUNG ABRUFEN & SPEICHERN
@app.get("/get_self_observation")
def get_self_observation():
    return load_json("selbstbeobachtung.json")

@app.post("/update_self_observation")
def update_self_observation(new_data: dict):
    data = load_json("selbstbeobachtung.json")
    today = datetime.date.today().isoformat()

    if today in data:
        data[today].append(new_data)
    else:
        data[today] = [new_data]

    save_json("selbstbeobachtung.json", data)
    return {"status": "updated", "data": new_data}
