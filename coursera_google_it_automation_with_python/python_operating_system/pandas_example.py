import pandas as pd

visitors = [12345, 6424, 9345, 8664, 2345]
errors = [23, 45, 33, 45, 76]

df = pd.DataFrame( {"visitors" : visitors, "errors" : errors}, index=["Mon","Tues","Wed","Thu", "Fri"])
print(df)

print(df["errors"].mean())