from notion_manager import increment_count_by_repository_name

def handle_github_webhook(data):
    repository_name = data['repository']['name']
    increment_count_by_repository_name(repository_name)