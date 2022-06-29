import csv
from datetime import datetime

candles = list()
with open("../resource/BTC-USDT-SWAP-week.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        ts = int(line[0])
        dt = datetime.fromtimestamp(ts / 1000)
        dts = datetime.strftime(dt, "%Y-%m-%d %H:%M:%S")
        candle = [dts] + line[1:6] + [0.0]
        candles.append(candle)

with open("../resource/feed/BTC-USDT-SWAP-week.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(candles)
