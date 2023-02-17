import scipy.stats as stats
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
    
    #原系列のShapiro-Wilk検定
    print(stats.shapiro(df_historical.USD.values))
    
    df_diff1 = df_historical.USD.diff().dropna()
    
    #1次階差系列のShapiro-Wilk検定
    print(stats.shapiro(df_diff1.values))
    
    
if __name__ == '__main__':
    main()