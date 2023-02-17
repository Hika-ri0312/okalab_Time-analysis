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

def main():
    df_historical = fixed_data_index()
    
    #原系列のヒストグラムの表示
    df_historical.USD.plot.hist()

    #1次階差系列のヒストグラムの表示
    plt.savefig("origin_data.png")
    plt.show()
    
    
    
if __name__ == '__main__':
    main()