import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# 파일 저장
data = pd.read_csv('tfidf_table.csv', index_col=0)

# 이상 값 0으로 대체
data = data.replace([np.nan, np.inf, -np.inf], 0)

# 키워드 이름 추출
feature_names = data.columns[1:]

# 0번 열 삭제 (나라 이름들)
data = data.iloc[:, 1:]

#각 키워드 별 최댓 값 추출
max_values = data.max()
print(max_values)

#0.3이 넘는 index 추출
excluded_columns = max_values[max_values > 0.3].index
print(excluded_columns)

#해당 index data 에서 열 삭제
data = data.drop(excluded_columns, axis=1)

# 키워드들 정수형으로 One-Hot incoding
df_encoded = pd.get_dummies(data)

# K-means 클러스터링
kmeans = KMeans(n_clusters=20)  # Specify the number of clusters
kmeans.fit(df_encoded)

# 데이터에 Cluster라는 열로 각 나라의 cluster 표시
data['Cluster'] = kmeans.labels_

print(data)

# 0번 열에 label이라는 이름 붙여서 추출
result = data.index.to_frame().rename(columns={0: 'label'})
# cluster 열 추출
result['Cluster'] = data['Cluster'].values

# label과 cluster열 만 csv파일로 저장
result.to_csv('clustering_result.csv', sep=',', index=False, encoding='utf-8-sig')
