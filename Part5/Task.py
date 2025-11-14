import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

reports_dir = 'Part5/Reports'

# настройка отображения
plt.rcParams['figure.figsize'] = (12, 8)
sns.set_style("whitegrid")

# чтение данных из огурца
df = pd.read_pickle("Part5/cache_table.pkl")
print("Размер датасета:", df.shape)
print("Колонки:", df.columns.tolist())

# анализ данных
print("\n" + "="*50)
print("БАЗОВЫЙ АНАЛИЗ")
print("="*50)

print(f"Период: {df['Year-month'].min()} - {df['Year-month'].max()}")
print(f"Товаров: {df['Product'].nunique()}")
print(f"Брендов: {df['Brand'].nunique()}")
print(f"Общие продажи: {df['Sales'].sum():,.0f} руб.")
print(f"Общая прибыль: {(df['Sales'].sum() - df['Cost price'].sum()):,.0f} руб.")

# динамика продаж
print("\n" + "="*50)
print("ДИНАМИКА ПО ТОВАРАМ")
print("="*50)

# Топ-5 товаров по продажам
top_products = df.groupby('Product')['Sales'].sum().nlargest(5)
print("Топ-5 товаров по продажам:")
for product, sales in top_products.items():
    print(f"  {product}: {sales:,.0f} руб.")

# *Визуализация 
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='skyblue')
plt.title('Топ-5 товаров по объему продаж')
plt.ylabel('Продажи (руб)')
plt.tight_layout()
plt.savefig(f'{reports_dir}/top_products.png', dpi=300, bbox_inches='tight')
plt.close()

# анализ по местам продаж
print("\n" + "="*50)
print("АНАЛИЗ ПО ТОЧКАМ")
print("="*50)

point_sales = df.groupby('Point')['Sales'].sum()
print("Продажи по точкам:")
for point, sales in point_sales.items():
    print(f"  {point}: {sales:,.0f} руб.")

# *Визуализация
plt.figure(figsize=(8, 6))
point_sales.plot(kind='bar', color='lightgreen')
plt.title('Продажи по точкам реализации')
plt.ylabel('Продажи (руб)')
plt.tight_layout()
plt.savefig(f'{reports_dir}/point_sales.png', dpi=300, bbox_inches='tight')
plt.close()

# товарооборт
print("\n" + "="*50)
print("ДИНАМИКА ТОВАРООБОРОТА")
print("="*50)

monthly_sales = df.groupby('Year-month')['Sales'].sum()
print("Месячные продажи:")
for month, sales in monthly_sales.items():
    print(f"  {month}: {sales:,.0f} руб.")

# *Визуализация 
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', linewidth=2, markersize=6)
plt.title('Динамика общего товарооборота')
plt.xlabel('Месяц')
plt.ylabel('Продажи (руб)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'{reports_dir}/monthly_sales.png', dpi=300, bbox_inches='tight')
plt.close()

# анлиз ьрендов
print("\n" + "="*50)
print("АНАЛИЗ ПО БРЕНДАМ")
print("="*50)

brand_stats = df.groupby('Brand').agg({
    'Sales': 'sum',
    'Cost price': 'sum',
    'Amount': 'sum'
})
brand_stats['Profit'] = brand_stats['Sales'] - brand_stats['Cost price']
brand_stats['Margin'] = (brand_stats['Profit'] / brand_stats['Sales'] * 100).round(1)

print("Продажи по брендам:")
print(brand_stats[['Sales', 'Profit', 'Margin']])

# *Визуализация 
plt.figure(figsize=(10, 6))
brand_stats['Sales'].plot(kind='bar', color='orange', alpha=0.7)
plt.title('Продажи по брендам')
plt.ylabel('Продажи (руб)')
plt.tight_layout()
plt.savefig(f'{reports_dir}/brand_sales.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Прогноз продаж
print("\n" + "="*50)
print("ПРОГНОЗ ПРОДАЖ")
print("="*50)

# средние продажи по товарам
product_sales = df.groupby('Product')['Sales'].sum().nlargest(10)
print("Топ-10 товаров для прогноза:")
print(product_sales)

# Создаем простой прогноз на основе средних значений
forecast_data = []
for product, total_sales in product_sales.items():
    product_data = df[df['Product'] == product]
    avg_monthly_sales = total_sales / len(product_data['Year-month'].unique())
    forecast = avg_monthly_sales * 1.1  # Простой прогноз +10%
    
    forecast_data.append({
        'Product': product,
        'Total Sales': total_sales,
        'Avg Monthly': avg_monthly_sales,
        'Forecast': forecast,
        'Growth': '↑ 10%'
    })

forecast_df = pd.DataFrame(forecast_data)
print("\nПрогноз продаж на следующий месяц:")
print(forecast_df[['Product', 'Avg Monthly', 'Forecast', 'Growth']].to_string(index=False))

# Визуализация прогноза
plt.figure(figsize=(12, 6))
products = forecast_df['Product']
avg_sales = forecast_df['Avg Monthly']
forecast_sales = forecast_df['Forecast']

x = range(len(products))
width = 0.35

plt.bar(x, avg_sales, width, label='Средние продажи', alpha=0.7, color='blue')
plt.bar([i + width for i in x], forecast_sales, width, label='Прогноз (+10%)', alpha=0.7, color='red')

plt.xlabel('Товары')
plt.ylabel('Продажи (руб)')
plt.title('Сравнение средних продаж и прогноза (топ-10 товаров)')
plt.xticks([i + width/2 for i in x], products, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig(f'{reports_dir}/forecast_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

#! делаем отчет
print("\n" + "="*50)
print("СВОДНЫЙ ОТЧЕТ")
print("="*50)

total_sales = df['Sales'].sum()
total_cost = df['Cost price'].sum()
total_profit = total_sales - total_cost
margin = (total_profit / total_sales * 100)

print(f"ОБЩИЕ РЕЗУЛЬТАТЫ:")
print(f"▪ Объем продаж: {total_sales:,.0f} руб.")
print(f"▪ Себестоимость: {total_cost:,.0f} руб.")
print(f"▪ Прибыль: {total_profit:,.0f} руб.")
print(f"▪ Рентабельность: {margin:.1f}%")
print(f"▪ Товаров в ассортименте: {df['Product'].nunique()}")
print(f"▪ Период анализа: {len(df['Year-month'].unique())} месяцев")

print(f"\nЛУЧШИЕ ПОКАЗАТЕЛИ:")
print(f"▪ Лучший товар: {top_products.index[0]} ({top_products.iloc[0]:,.0f} руб.)")
print(f"▪ Лучший бренд: {brand_stats['Sales'].idxmax()} ({brand_stats['Sales'].max():,.0f} руб.)")
print(f"▪ Самая высокая маржа: {brand_stats['Margin'].idxmax()} ({brand_stats['Margin'].max():.1f}%)")

print(f"\nВЫВОДЫ:")
print(f"▪ Всего проанализировано {len(df)} записей о продажах")
print(f"▪ Товарооборот показывает {'рост' if monthly_sales.iloc[-1] > monthly_sales.iloc[0] else 'снижение'}")
print(f"▪ Прогноз основан на средних значениях с учетом роста +10%")

# где какие графики сохранены
print("▪ top_products.png - Топ-5 товаров")
print("▪ point_sales.png - Продажи по точкам") 
print("▪ monthly_sales.png - Динамика товарооборота")
print("▪ brand_sales.png - Продажи по брендам")
print("▪ forecast_comparison.png - Сравнение прогноза")

#сохраняем отчеты
top_products.to_csv(f'{reports_dir}/top_products.csv')
point_sales.to_csv(f'{reports_dir}/point_sales.csv')
monthly_sales.to_csv(f'{reports_dir}/monthly_sales.csv')
brand_stats.to_csv(f'{reports_dir}/brand_stats.csv')
forecast_df.to_csv(f'{reports_dir}/forecast.csv', index=False)
