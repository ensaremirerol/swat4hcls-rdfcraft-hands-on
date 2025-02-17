from datetime import datetime

return datetime.strptime(
    value, "%Y-%m-%d %H:%M:%S"
).isoformat()
