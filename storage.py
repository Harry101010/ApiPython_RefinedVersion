import json

class DataStorage:
  def save_to_json(self, file_path: str, entities):
    try:
      data = [e.to_dict() for e in entities]
      
      with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
      print(f"Da luu {len(data)} ban ghi vao {file_path}")
    except (OSError, TypeError) as e:
      print(f"Loi khi luu file: {e}")

  def load_from_json(self, file_path: str):
    try:
      with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    except FileNotFoundError:
      print(f"khong tim thay file: {file_path}")
      return []
    except json.JSONDecodeError as e:
      print(f"File JSON khong hop le: {e}")
      return []