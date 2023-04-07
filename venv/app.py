from flask import Flask, request
from notion_manager import find_row_in_database, update_row
from notion_client import Client
from pprint import pprint

app = Flask(__name__)

NOTION_API_KEY = "secret_mqg8dyuo729AtFeHReI4U0sMfCNslzvJVrAiCysNsxL"
DB_ID = "9c0e71c0f9c645089fdbba0126762d80"

@app.route("/", methods=['GET', 'POST'])
def notion_api_test():
    rows = find_row_in_database("CodeWars")
    if rows:
        row = rows[0]
        commit_count = row['properties']['CommitCount']['number']
        update_row(row['id'], "CommitCount", commit_count + 1)
    else:
        pprint(f"No rows")

    return ""

if __name__ == '__main__':
    app.run()