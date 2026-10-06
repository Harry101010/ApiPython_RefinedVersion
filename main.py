import json
from api_client import APIClient
from storage import DataStorage

file_name = "system_data.json"

if __name__ == "__main__":
  client = APIClient()

  users = client.get_users(10)
  posts = client.get_posts(10)

  all_data = users + posts

  storage = DataStorage()
  storage.save_to_json(file_name, all_data)

  data = storage.load_from_json(file_name)
  print(json.dumps(data, indent=2, ensure_ascii=False))