import requests
import time
import json

TOKEN = "TOKEN"

url = f"https://botapi.rubika.ir/v3/{TOKEN}/getUpdates"

offset = None

print("Listening for updates...")
print("پیام‌های مختلف را در گروه بفرست.")
print()

while True:
    try:
        data = {}

        if offset:
            data["offset_id"] = offset

        response = requests.post(
            url,
            json=data,
            timeout=15
        )

        result = response.json()

        updates = result.get("data", {}).get("updates", [])

        for update in updates:
            print("=" * 60)
            print(json.dumps(update, ensure_ascii=False, indent=2))

        offset = result.get("data", {}).get("next_offset_id", offset)

        time.sleep(3)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(3)
