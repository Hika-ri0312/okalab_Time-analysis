import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def datafile_fixed():
    #データ確認
    df_historical = pd.read_csv('./m_quote.csv', encoding="shift-jis")

    #データ修正
    #1行目のデータを取得
    new_clm = df_historical.loc[0,:]

    #元々のファイルのカラム名を1行目のデータに変更
    new_df = df_historical.rename(columns=new_clm)

    #変換後の0行目を削除
    new_df.drop(index=0, inplace=True)
    new_df_r = new_df.reset_index(drop=True)

    new_df_r.to_csv('./m_quote_fix.csv')

