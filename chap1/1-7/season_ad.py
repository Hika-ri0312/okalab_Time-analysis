import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def view_middle_icedata():
    df_ice = pd.read_csv('./ice_fix.csv',encoding="utf-8_sig")
    
    
    return df_ice

def season_ad_cal():
    df_ice = view_middle_icedata()
    
    #1.中心化移動平均系列
    df_ma = df_ice.expenditure_yen.rolling(window=12).mean().shift(-6)
    df_cma = df_ma.rolling(window=2).mean()
    
    #2.原系列（df_ice.expenditure_yen）/ 中心化移動平均（df_cma）
    df_orig_div_cma = df_ice.expenditure_yen / df_cma
    
    #月ごとに加算
    orig_div_cma = df_orig_div_cma.values    
    s_index = np.zeros(12)
    counter = np.zeros(12, dtype='i')
    
    for idx in range(len(orig_div_cma)//12):
        #12ヶ月ごとにデータを抽出
        cut_orig_div_cma = orig_div_cma[idx*12:(idx+1)*12]
        mask = cut_orig_div_cma != cut_orig_div_cma
    
        #numpy.whereを使用して非数（nan）を0にして加算する
        counter += np.where(mask,0,1)
        s_index += np.where(mask,0,cut_orig_div_cma)
    

    #加算結果の各月平均
    s_index /= counter
    #全体を1200に合わせ季節指数を計算
    s_index = s_index / s_index.sum() * 1200
    
    print(s_index)
    goal = 100000000 / 1200 * s_index
    print(goal)
    
    
    #季節指数を原系列の要素と対応させる
    #原系列のスタートが1月なのでnumpy.tileで12ヶ月分の季節指数を繰り返すだけでよい
    tiled_s_index = np.tile(s_index, len(orig_div_cma)//12)
    
    #季節調整済み系列の計算
    df_adjusted_series = df_ice.expenditure_yen / tiled_s_index * 100
    
    return df_adjusted_series
    
    
def main():
    ice_data = view_middle_icedata()
    season_ad = season_ad_cal()
    
    ice_data.expenditure_yen.plot()
    season_ad.plot()
    
    plt.savefig("season_ad.png")
    plt.show()
    
    
if __name__ == '__main__':
    main()