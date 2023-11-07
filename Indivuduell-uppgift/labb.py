import requests
import json
import pandas as pd
import os

os.system("cls")


api_url = "https://www.elprisetjustnu.se/api/v1/prices/2023/07-10_SE3.json"

# Hämta resultatet av api_url
url_requested = requests.get(api_url)
# läs innehållet som sträng
url_string = url_requested.text
# Eftersom den är i json-format så omvandlar vi den
response_url_dict = json.loads(url_string)
# Sedan gör vi det till en tabell
df = pd.DataFrame(response_url_dict)

# Gör om tabellen till html
#df = df.to_html
print("Hela tabellen:")
print(df)
print()
print("-"*50)
print()

print("Kolumnen vi vill ändra: ")
selected_column = df[["time_start"]]    # dubbla hakparenteser för att få med rubriken
print(selected_column)

print()
print("-"*50)
print("Kolumnens datatyp:", type((df["time_start"]))) # Kolumnen är ingen sträng, utan är är "pandas.core.series.Series"
print(type(str(df["time_start"])))  # Det går att omvandla hela kolumnen till en sträng
print(type(df["time_start"][0])) # varje rad är en sträng däremot, utan konvertering, skapa en funktion som ändrar varje rad?
print("-"*50)
print()

print("Before:")
row = df["time_start"][23]
print(row)
print("After")
slice_the_whole_string = row[11:16] # Gör allting på en och samma gång
print(slice_the_whole_string)
print("-"*50)
print()







"""
# Kan jag ändra kolumnerna enklare?
# Behövs detta ens? Jag kan göra detta i endpoint funktionen.
def slice_times(DataFrame, old_column_name, new_column_name):
    #Function takes a pandas DataFrame column and slices it
    Args:
        DataFrame (_type_): Pandas DataFrame
        old_column_name (_type_): Name of column one wish to change
        new_column_name (_type_): Name of the new modified column

    Returns:
        _type_: _Returns new modified column_
    
    DataFrame[new_column_name] = DataFrame[old_column_name].str[11:16]    # Omvandla kolumnen till en sträng och slica den.
    return DataFrame

modified_time_start = slice_times(df, "time_start", "Time_start") # Nya kolumnen läggs till i slutet på nuvarande
modified_time_end = slice_times(df, "time_end", "Time_end")
del df["time_start"]    # Tar bort gamla kolumner
del df["time_end"]

print("Ändrade kolumner: ")
print(df)


"""

