from datetime import date
import requests
import os

# Obtener bloque actual en tiempo real
response = requests.get("https://mempool.space/api/v1/blocks/tip/height")
current_block = int(response.text.strip())

last_halving_block = 840000
next_halving_block = 1050000

blocks_mined = current_block - last_halving_block
blocks_total = next_halving_block - last_halving_block
progress = (blocks_mined / blocks_total) * 100
days_remaining = (next_halving_block - current_block) // 144

segments = 14
filled = int(progress / 100 * segments)
bar = "🟧" * filled + "⬜" * (segments - filled)

content = f"""GM, Bitcoin halving countdown:

Progress: {progress:.2f}%

{bar}

Days remaining: {days_remaining}

One day closer! ☀️ The most secure network completed another flawless day, zero downtime, zero hacks. Study, buy, self custody and talk about #Bitcoin"""

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"content<<EOF\n{content}\nEOF\n")
