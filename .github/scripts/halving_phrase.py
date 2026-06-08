from datetime import date
import os

today = date.today()
last_halving = date(2024, 4, 20)
next_halving = date(2028, 4, 18)

days_passed = (today - last_halving).days
total_days = (next_halving - last_halving).days
progress = (days_passed / total_days) * 100
days_remaining = (next_halving - today).days

segments = 14
filled = int(progress / 100 * segments)
bar = "🟧" * filled + "⬜" * (segments - filled)

content = f"""GM, Bitcoin halving:

Progress: {progress:.2f}%

{bar}

Estimated days remaining: {days_remaining}

One day closer to the halving! ☀️"""

# Siempre publica (porque es manual)
with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"content<<EOF\n{content}\nEOF\n")
