df = df.rename(columns={
    "Unnamed: 0" : "NULL",
    "Unnamed: 1" : "Date",
    "Unnamed: 2" : "Year",
    "Unnamed: 3" : "Year-month",
    "Unnamed: 4" : "Point",
    "Unnamed: 5" : "Brand",
    "Unnamed: 6" : "Product",
    "Unnamed: 7" : "Amount",
    "Unnamed: 8" : "Sales",
    "Unnamed: 9" : "Cost price",
})

df = df.drop(columns={'NULL'})

df.to_pickle("Part5/cache_table.pkl")
#!Renamed and delete some columns

###############################################################


df = df.drop(index=0)
df['Date'] = pd.to_datetime(df['Date'], errors="coerce")
df['Amount'] = pd.to_numeric(df['Amount'], errors="coerce")
df['Sales'] = pd.to_numeric(df['Sales'], errors="coerce")
df['Cost price'] = pd.to_numeric(df['Cost price'], errors="coerce")
df['Year'] = pd.to_datetime(df['Year'], errors="coerce")
df['Year-month'] = pd.to_datetime(df['Year-month'], errors="coerce")
df['Year'] = df['Year'].dt.year
df['Year-month'] = df['Year-month'].dt.to_period("M")

print(df.dtypes)

df.to_pickle("Part5/cache_table.pkl")
#!Change types of columns

####################################################################