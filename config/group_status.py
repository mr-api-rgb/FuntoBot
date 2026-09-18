import json
import os


FILE_NAME = "config/active_groups.json"


def load_groups():
    if not os.path.exists(FILE_NAME):
        return set()

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        data = json.load(file)

    return set(data)


def save_groups(groups):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(list(groups), file, ensure_ascii=False, indent=4)


def is_group_active(chat_id):
    groups = load_groups()
    return str(chat_id) in groups


def activate_group(chat_id):
    groups = load_groups()
    groups.add(str(chat_id))
    save_groups(groups)


def deactivate_group(chat_id):
    groups = load_groups()
    groups.discard(str(chat_id))
    save_groups(groups)
