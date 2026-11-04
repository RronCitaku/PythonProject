import pandas as pd

from Module4.while_loop import average

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

first_rows = df.head(10)
print(first_rows)

last_rows = df.tail()
print(last_rows)

country_data = df['Country']
print(country_data)

subset = df[['Country', 'Average IQ']]
print(subset)

filtered_data = subset[subset['Average IQ'] > 100]
print(filtered_data)

null_mask = df.isnull()
null_count = null_mask.sum()
print("\nCount of null in each column:")
print(null_count)

df.dropna()

print("\nDataset infomation after removing null values:")
print(df.info())

duplicated_count = df.duplicated().sum()
print('\nCount of duplicated rows:')
print(duplicated_count)

average_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()
print(average_iq_per_continent)

sorted_average_iq_per_continent = average_iq_per_continent.sort_values(ascending=False)
print(sorted_average_iq_per_continent)

df['Population - 2023'] = df['Population - 2023'].apply(lambda x: float(x.replace(',', '')))
print(df.info())

total_nobel_by_country = df.groupby('Country')['Nobel Prices'].sum()
sort_values = total_nobel_by_country.sort_values(ascending=False)
print("\nTotal nobel prizes by country", sort_values)

sort_values_nonzero = sort_values[sort_values != 0]
print("\nTotal Nobel Prizes by country, excluding countrys with Zero Nobel Prizes\n", sort_values_nonzero)