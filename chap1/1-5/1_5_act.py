import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#データ確認
df_historical = pd.read_csv('m_quote_fix.csv', encoding="shift-jis")
# ここで、手動でカラム名'data'と付けた

#カラム'data'をインデックスに設定
df_i = df_historical.set_index('data')

df_i.drop(columns=['Unnamed: 0'], inplace=True)
print(df_i)

#24ヶ月移動平均
df_i_24 = df_i.USD.rolling(window=24).mean()
#48ヶ月移動平均
df_i_48 = df_i.USD.rolling(window=48).mean()

df_i.USD.plot()
df_i_24.plot()
df_i_48.plot()
plt.savefig("mean_3data.png")
plt.show()