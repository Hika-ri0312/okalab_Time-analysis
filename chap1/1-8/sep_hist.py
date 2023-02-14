import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def fixed_data_index():
    #データ確認
    df_historical = pd.read_csv('m_quote_fix.csv', encoding="shift-jis")
    # ここで、手動でカラム名'data'と付けた

    #カラム'data'をインデックスに設定
    df_i = df_historical.rename(columns={'':'data'})
    return df_i

def sep_cal(month):
    df_historical = fixed_data_index()
    
    ma_months = df_historical.USD.rolling(month).mean()
    diff_ma24 = (df_historical.USD - ma_months) / ma_months * 100
    
    return diff_ma24
    

def main():
    diff_ma24 = sep_cal(24)
    
    #diff_ma24.plot()
    diff_ma24.plot.hist()
    
    plt.savefig("diff_ma24_hist.png")
    plt.show()
    
if __name__ == "__main__":
    main()