from datetime import datetime

t = datetime.now().astimezone()
print(t)
print(t.tzinfo)