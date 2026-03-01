import os

NOTE_TOKEN = os.getenv("NOTE_ACCESS_TOKEN")
MANUS_KEY = os.getenv("MANUS_API_KEY")

print("本番コード起動")
print("NOTE_TOKEN exists:", NOTE_TOKEN is not None)
print("MANUS_KEY exists:", MANUS_KEY is not None)
