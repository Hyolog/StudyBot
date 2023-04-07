from flask import Flask, request
from notion_manager import find_row_in_database, increase_and_update_row
from notion_client import Client
from pprint import pprint

app = Flask(__name__)

NOTION_API_KEY = "secret_mqg8dyuo729AtFeHReI4U0sMfCNslzvJVrAiCysNsxL"
DB_ID = "9c0e71c0f9c645089fdbba0126762d80"
ROW_NAME = "CodeWars"

@app.route("/commit-count/", methods=['GET', 'POST'])
def notion_api_test():
    rows = find_row_in_database(ROW_NAME)
    increase_and_update_row(rows)
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0')