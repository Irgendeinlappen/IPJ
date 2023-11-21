import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('Goals.csv', sep=';' )     #read file

    delta_vals_pv = compute_deltas(df['PV'])
    delta_vals_ons = compute_deltas(df['Onshore'])
    delta_vals_ofs= compute_deltas(df['Offshore'])
    delta_vals_reptwh = compute_deltas(df['Erzeugung'])
    delta_vals_repgwh = [val * 1_000 for val in delta_vals_reptwh]

    plot(delta_vals_reptwh)
   
   # delta_vals_repgwh = [val * 1_000 for val in delta_vals_reptwh]
    #plt.plot(delta_vals_repgwh)
    #plt.savefig('chart.png')
    # Delete 0 entries
    #delta_vals_pv = delta_vals_pv[delta_vals_pv != 0]



    print(delta_vals_pv)
    print('___________________')
    print(delta_vals_ons)
    print('___________________')
    print(delta_vals_ofs)
    print('___________________')
    print(delta_vals_repgwh)
    print('___________________')
   
    print('___________________')


def compute_deltas(data: pd.Series) -> np.ndarray:
    delta_vals: np.ndarray = np.zeros(data.size - 1, dtype=int)

    for i, item in enumerate(delta_vals):
        delta_vals[i] = data[i+1] - data[i]

    return delta_vals

def plot(variable):
    plt.plot(variable)
    plt.savefig('chart.png')
    


if __name__ == '__main__':
    main()
