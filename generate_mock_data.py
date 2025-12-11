import json
import random
from datetime import date, timedelta

# 設定日期範圍
start_date = date(2025, 9, 1)
end_date = date(2025, 12, 10)

# 分類與對應的常見項目與金額範圍 (min, max)
categories = {
    "餐飲食品": [
        ("早餐蛋餅+紅茶", 35, 50), ("學餐便當", 60, 80), ("校外小吃", 80, 100),
        ("便利商店飯糰", 30, 45), ("手搖杯", 35, 60), ("宵夜鹹酥雞", 100, 150),
        ("小火鍋", 150, 250), ("零食", 15, 50), ("水果", 40, 100)
    ],
    "交通運輸": [
        ("公車", 15, 30), ("捷運", 20, 40), ("Uber", 120, 200),
        ("火車票", 80, 300), ("YouBike", 5, 15)
    ],
    "居家生活": [
        ("牙膏", 60, 100), ("衛生紙", 100, 150), ("洗衣精", 120, 200),
        ("手機費", 499, 499), ("房租", 5500, 5500) # 每月一次
    ],
    "服飾購物": [
        ("特價T恤", 290, 490), ("網拍衣服", 200, 500), ("新鞋子", 1000, 1800)
    ],
    "休閒娛樂": [
        ("電影票", 220, 300), ("KTV唱歌", 300, 600), ("Netflix訂閱", 270, 270),
        ("Spotify", 149, 149), ("Steam遊戲", 200, 800)
    ],
    "醫療保健": [
        ("診所掛號費", 150, 200), ("感冒藥", 150, 300), ("維他命", 200, 500)
    ],
    "投資儲蓄": [
        ("零股投資", 1000, 3000), ("定期存款", 1000, 1000)
    ],
    "其他": [
        ("影印費", 10, 30), ("系費", 100, 300)
    ]
}

data = []

current_date = start_date
while current_date <= end_date:
    
    # 每天隨機產生 1-4 筆消費
    num_records = random.randint(1, 4)
    
    # 周末可能花比較多
    if current_date.weekday() >= 5: 
        num_records += random.randint(0, 2)

    for _ in range(num_records):
        # 較高機率是吃的
        if random.random() < 0.6:
            cat = "餐飲食品"
        else:
            cat = random.choice(list(categories.keys()))
            
        item_choice = random.choice(categories[cat])
        item_name = item_choice[0]
        amount = random.randint(item_choice[1], item_choice[2])
        
        # 稍微調整項目名稱增添變化
        if cat == "餐飲食品" and amount > 150:
             note = "偶爾吃好點"
        else:
             note = ""

        record = {
            "品項": item_name,
            "分類": cat,
            "金額": amount,
            "日期": str(current_date),
            "備註": note
        }
        data.append(record)
    
    # 每月固定支出 (假設每月 5 號)
    if current_date.day == 5:
        # 房租
        data.append({
            "品項": "房租",
            "分類": "居家生活",
            "金額": 5500,
            "日期": str(current_date),
            "備註": "固定支出"
        })
        # 手機費
        data.append({
            "品項": "手機費",
            "分類": "居家生活",
            "金額": 499,
            "日期": str(current_date),
            "備註": "自動扣款"
        })

    current_date += timedelta(days=1)

# Sort by date
data.sort(key=lambda x: x["日期"])

file_path = "data/records.json"
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Generated {len(data)} records to {file_path}")
