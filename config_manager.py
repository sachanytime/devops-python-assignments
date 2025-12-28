import configparser
import json
import sqlite3
from flask import Flask, jsonify

CONFIG_FILE = "config.ini"
DB_FILE = "config_data.db"

app = Flask(__name__)


# ---------------------------
# Read Configuration File
# ---------------------------
def read_config(file_path):
    config = configparser.ConfigParser()
    data = {}

    try:
        config.read(file_path)

        for section in config.sections():
            data[section] = {}
            for key, value in config.items(section):
                data[section][key] = value

        return data

    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return None


# ---------------------------
# Save JSON Data to Database
# ---------------------------
def save_to_database(json_data):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS config_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT
            )
        """)

        cursor.execute("DELETE FROM config_data")  # Keep latest config
        cursor.execute(
            "INSERT INTO config_data (data) VALUES (?)",
            (json.dumps(json_data),)
        )

        conn.commit()
        conn.close()

    except Exception as e:
        print(f"Database error: {e}")


# ---------------------------
# Fetch Data from Database
# ---------------------------
def fetch_from_database():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT data FROM config_data ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        conn.close()

        if row:
            return json.loads(row[0])
        return {}

    except Exception as e:
        print(f"Database fetch error: {e}")
        return {}


# ---------------------------
# API Endpoint (GET)
# ---------------------------
@app.route("/config", methods=["GET"])
def get_config():
    data = fetch_from_database()
    return jsonify(data)


# ---------------------------
# Main Execution
# ---------------------------
if __name__ == "__main__":
    config_data = read_config(CONFIG_FILE)

    if config_data:
        print("\nConfiguration File Parser Results:\n")

        for section, values in config_data.items():
            print(f"{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
            print()

        save_to_database(config_data)
        print("Configuration saved to database as JSON.\n")

    else:
        print("Failed to load configuration.")

    # Start API Server
    app.run(debug=True)
