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
    
    #自己相関
    p_acf = sm.tsa.stattools.acf(passengers)
    print(p_acf)

def main():
    passengers = get_data()
    auto_relation()
    
    #自己相関係数のコレログラムの作成 : plot_acf関数
    #lags : 時間差の度合い
    sm.graphics.tsa.plot_acf(passengers,lags=40)
    plt.savefig('correlogram.png')
    plt.show()
    
if __name__ == '__main__':
    main()
    