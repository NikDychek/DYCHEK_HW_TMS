import requests

response = requests.get("https://www.nbrb.by/api/exrates/rates/431?periodicity=0")
data = response.json()
price_dollar = data["Cur_OfficialRate"]
count_dollar = int(
    input(
        "введи количество долларов, которые хочешь конвертировать в белорусский рубль "
    )
)
print(f"{count_dollar} доллара составляют {count_dollar*price_dollar} белорусских рублей")