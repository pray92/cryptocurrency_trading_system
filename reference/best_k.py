import pyupbit
import numpy as np

# 변동성 돌파에서 가장 좋은 k 값을 반환
def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC", count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


if __name__ == '__main__':
	for k in np.arange(0.1, 1.0, 0.1):
		ror = get_ror(k)
		print("%.1f %f" % (k, ror))