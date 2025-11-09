import numpy as np
import pandas as pd
from faker import Faker
import matplotlib.pyplot as plt
import seaborn as sns

#Объявляем Faker
generate = Faker('ru_RU')
st_amount = 200

#Generate inf about student
names = [generate.name() for _ in range(st_amount)]
years = np.random.choice([2022, 2023, 2024, 2025], size=st_amount)
ad_form = np.random.choice(["Очная", "Заочная"], size=st_amount)

#Generate exams scores and make limits on scores
math_score = np.random.normal(loc=90, scale=5, size=st_amount)
math_score = np.clip(math_score, 80, 100)
phys_score = np.random.normal(loc=85, scale=7, size=st_amount)
phys_score = np.clip(phys_score, 80, 100)
lang_score = np.random.normal(loc=90, scale=5, size=st_amount)
lang_score = np.clip(lang_score, 80, 100)

exam_scores = [x + y + z for x, y, z in zip(math_score, phys_score, lang_score)]
exam_scores = np.clip(exam_scores, 230, 300)

certificate_score = np.random.normal(loc=9.0, scale=0.5, size=st_amount)
certificate_score = np.clip(certificate_score, 7, 10)

total_score = [x + y * 10 for x, y in zip(exam_scores, certificate_score)]

speciality = np.random.choice(["ПИ", "КБ", "РФ", "ИнтЭл"], size=200)
addreses = [generate.address() for _ in range(st_amount)]
numbers = [generate.phone_number() for _ in range(st_amount)]

#create dataframe with students info
data = pd.DataFrame({
"ФИО" : names,
"Год поступления" : years,
"Форма образования" : ad_form,
"Результат ЦЭ/ЦТ математика" : math_score,
"Результат ЦЭ/ЦТ физика" : phys_score,
"Результат ЦЭ/ЦТ язык" : lang_score,
"Результаты экзаменов ЦТ/ЦЭ" : exam_scores,
"Балл аттестата" : certificate_score,
"Общий балл" : total_score,
"Специальность" : speciality,
"Адрес регистрации" : addreses,
"Номер телефона" : numbers,
})

#* average ex score plot
num_ex = 3
data["Средний балл ЦЭ/ЦТ"] = data["Результаты экзаменов ЦТ/ЦЭ"] / num_ex
av_score = data.groupby("Год поступления")["Средний балл ЦЭ/ЦТ"].mean()

plt.figure(figsize=(10, 7))
sns.lineplot(data=av_score)
plt.title("Динамика среднего балла ЦЭ/ЦТ")
plt.xlabel("Год поступления")
plt.ylabel("Средний балл ЦЭ/ЦТ")
plt.savefig("av_score.png", dpi=300)

#* average certificate score plot
av_cert_score = data.groupby("Год поступления")["Балл аттестата"].mean()
plt.figure(figsize=(10, 7))
sns.lineplot(data=av_cert_score)
plt.title("Динамика балла аттестата")
plt.xlabel("Год поступления")
plt.ylabel("Балл аттестата")
plt.savefig("av_cert_score.png", dpi=300, bbox_inches='tight')

#* average pass score plot
av_pass_score = data.groupby("Год поступления")["Общий балл"].mean()
plt.figure(figsize=(10, 7))
sns.lineplot(data=av_pass_score)
plt.title("Динамика проходного балла")
plt.xlabel("Год поступления")
plt.ylabel("Проходной балл")
plt.savefig("av_pass_score.png", dpi=300)

spec_count = data['Специальность'].value_counts()
print(spec_count)
plt.figure(figsize=(10,6))
sns.barplot(x=spec_count.index, y=spec_count.values, palette="viridis")
plt.title("Количество поступивших студентов по специальностям")
plt.xlabel("Специальность")
plt.ylabel("Количество студентов")
plt.xticks(rotation=45)  # чтобы подписи не накладывались
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # подгоняет макет
plt.show()