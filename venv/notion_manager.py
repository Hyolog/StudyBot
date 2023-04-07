from notion_client import Client

NOTION_API_KEY = "secret_mqg8dyuo729AtFeHReI4U0sMfCNslzvJVrAiCysNsxL"
DB_ID = "9c0e71c0f9c645089fdbba0126762d80"


def find_row_in_database(repo_name):
    notion = Client(auth=NOTION_API_KEY)
    return notion.databases.query(DB_ID, filter={"property": "RepoName", "title": {"equals": f"{repo_name}"}}).get("results")

def update_row(page_id, property_name, new_property_value):
    notion = Client(auth=NOTION_API_KEY)
    page = notion.pages.retrieve(page_id=page_id)

    properties = page['properties']
    properties[property_name] = {"number": new_property_value}

    notion.pages.update(
        page_id=page_id,
        properties=properties
    )