import pandas as pd
import os
import pandas as pd
cwd = os.path.abspath('')
files = os.listdir(cwd)

# Merge the first sheet of a given files
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=True)
df.head()
df.to_excel('total_stat.xlsx', startrow=4)

# convert excel to csv
read_file = pd.read_excel (r'total_stat.xlsx')
read_file.to_csv(r'total_statistic.csv', index=None, header=True)

