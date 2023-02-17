import io
import requests
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    #月ごとの旅客機の乗客数データ
    url = "https://www.analyticsvidhya.com/wp-content/uploads/2016/02/AirPassengers.csv"
    stream = requests.get(url).content
    df_content = pd.read_csv(io.StringIO(stream.decode('utf-8')))
    passengers = df_content['#Passengers']
    
    return passengers

def auto_relation():
    passengers = get_data()
    
    #偏自己相関
    #olsは最小二乗法による推定を意味する
    p_pacf = sm.tsa.stattools.pacf(passengers, method='ols')
    print(p_pacf)

def main():
    passengers = get_data()
    auto_relation()
    
    #偏自己相関係数コレログラムの作成 : plot_pacf関数
    #lags : 時間差の度合い
    sm.graphics.tsa.plot_pacf(passengers,lags=35)
    plt.savefig('side_correlogram.png')
    plt.show()
    
if __name__ == '__main__':
    main()
    