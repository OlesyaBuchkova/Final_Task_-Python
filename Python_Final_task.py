import pandas as pd #добавлено
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
# Создаем столбцы, которые заполняем 0 и 1 при выполнении условий
data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robot'] = '0'
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[data['whoAmI'] != 'human', 'human'] = '0'
print(data)
