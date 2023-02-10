import pandas as pd
import matplotlib.pyplot as plt

def view_middle_icedata():
    df_ice = pd.read_csv('./ice_fix.csv',encoding="utf-8_sig")
    
    
    return df_ice
    
def main():
   
    ice_data = view_middle_icedata()
    df_ma = ice_data.expenditure_yen.rolling(window=12).mean().shift(-6)
    df_cma = df_ma.rolling(window=2).mean()
    
    ice_data.expenditure_yen.plot()
    df_cma.plot()
    plt.savefig("ice_data.png")
    plt.show()
    
    
if __name__ == '__main__':
    main()