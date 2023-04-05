#In-Class Exercise 1
import pandas as pd

df = pd.DataFrame(
    {
        'col1': range(10),
        'col2': range(10, 20)
    },
    index=list('acgfhibdje')
)

df.sort_index(inplace=True)
result = df.loc['b':'e', 'col1']

print(result)

print(type(result))

# In-Class Exercise 2
df = pd.DataFrame(
    {
        'col1': range(10),
        'col2': range(10, 20)
    },
    index=list('acgfhibdje')
)

result = df.loc[['b', 'd', 'f', 'j'],['col1']]

print(result)

print(type(result))

#In-Class Exercise 3
df = pd.DataFrame(
    {
        'col1': range(0, 20),
        'col2': range(20, 40),
        'col3': range(40, 60)
    }
)

rows = list(range(0, len(df), 2))
result = df.iloc[rows, [1]]
print(result)


