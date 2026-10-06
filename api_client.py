import requests
from models import User, Post

class APIClient:
  BASE_URL = "https://jsonplaceholder.typicode.com"

  def get_users(self, limit=5):
    try:
      reponse = requests.get(f"{self.BASE_URL}/users", timeout=10)      
      
      if reponse.status_code != 200:
        print(f"Loi HTTP khi lay users: {reponse.status_code}")
        return []
      
      data = reponse.json()
      users = []
      
      for u in data[:limit]:
        users.append(User(u["id"], u["name"], u ["email"]))
      return users
    except requests.RequestException as e:
      print(f"Loi khi lay users {e}")
      return []

  def get_posts(self, limit=5):
    try:
      reponse = requests.get(f"{self.BASE_URL}/posts", timeout=10)

      if reponse.status_code != 200:
        print(f"Loi HTTP khi lay posts: {reponse.status_code}")
        return []

      data = reponse.json()
      posts = []

      for p in data[:limit]:
        posts.append(Post(p["id"], p["title"], p["body"]))
      return posts
    except requests.RequestException as e:
      print(f"Loi khi lay posts {e}")
      return []