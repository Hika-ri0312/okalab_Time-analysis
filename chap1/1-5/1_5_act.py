import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import data_fix

def fixed_data_index():
    #データ確認
    df_historical = pd.read_csv('m_quote_fix.csv', encoding="shift-jis")
    # ここで、手動でカラム名'data'と付けた

    #カラム'data'をインデックスに設定
    # df_i = df_historical.set_index('data')
    df_i = df_historical.rename(columns={'':'data'})
    return df_i

def main():
    data_fix.datafile_fixed()
    df_i = fixed_data_index()
    #24ヶ月移動平均
    df_i_24 = df_i.USD.rolling(window=24).mean()
    #48ヶ月移動平均
    df_i_48 = df_i.USD.rolling(window=48).mean()

    df_i.USD.plot()
    df_i_24.plot()
    df_i_48.plot()
    plt.savefig("mean_3data.png")
    plt.show()
    
if __name__ == "__main__":
    main()