import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing


data = pd.read_csv('./CarPrice_Assignment.csv')


def training_data_norm(data):
    symbolic_index = ['fueltype', 'aspiration', 'doornumber', 'carbody',
                      'drivewheel', 'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem']
    data_numeric = data.copy()
    for item in symbolic_index:
        symbols = data[item].unique()
        for i in range(len(symbols)):
            symbol = symbols[i]
            data_numeric.loc[data_numeric[item] == symbol, item] = i
    train_data = data_numeric.copy()
    train_data.drop(['car_ID', 'CarName'], inplace=True, axis=1)
    # 规范化到 [0,1] 空间
    min_max_scaler = preprocessing.MinMaxScaler()
    train_data_norm = min_max_scaler.fit_transform(train_data)
    return train_data_norm

def elbow_method(data):
    train_data_norm = training_data_norm(data)
    N = range(1, 20)
    sse = []
    for k in N:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(train_data_norm)
        sse.append(kmeans.inertia_)
    x = N
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.plot(x, sse, 'o-')
    plt.show()


def K_means(data, n_clusters):
    train_data_norm = training_data_norm(data)
    # 使用KMeans聚类
    kmeans = KMeans(n_clusters)
    kmeans.fit(train_data_norm)
    predict_y = kmeans.predict(train_data_norm)

    result = data.copy()
    result['CarBrand'] = [x.split(' ')[0] for x in result['CarName']]
    result['聚类结果'] = predict_y
    return result


def vw_competetor(result):
    result_vw = pd.concat([result[result['CarBrand'] == 'volkswagen'],
                           result[result['CarBrand'] == 'vw'],
                           result[result['CarBrand']=='vokswagen']])
    competetor = []
    for i in result_vw['聚类结果'].unique():
        competetor += list(result[result['聚类结果'] == i]['CarBrand'].unique())
    competetor = list(set(competetor))
    competetor.remove('volkswagen')
    competetor.remove('vw')
    competetor.remove('vokswagen')
    return competetor

def main():
    elbow_method(data)
    result = K_means(data, n_clusters=6)
    competetor = vw_competetor(result)
    print("Volkswagen品牌竞品：")
    print(competetor)


if __name__ == "__main__":
    main()
