from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier
from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')

# autoviz
# plt.style.use('dark_background')
# AV = AutoViz_Class()

# AV.AutoViz(
#     filename='',
#     dfte=df,
#     depVar='target',
#     verbose=2,  # 0: 간단히 표시; 1: 자세히 표시; 2: 파일로 저장
#     max_rows_analyzed=df.shape[0],
#     max_cols_analyzed=df.shape[1])

# autoviz end

# LazyPredict 자동으로 베스트 모델 찾아주는 패키지

y_data = df.pop('target')
x_data = df

# print(x_data.shape)
# print(y_data.shape)


x_train, x_test, y_train, y_test = train_test_split(
    x_data,
    y_data,
    test_size=0.2,
    random_state=2022,
    stratify=y_data  # 클래스 비율을 동일하게 분할한다.
)

# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)

# 모델 성능 자동비교
clf = LazyClassifier(verbose=0, predictions=True)

models, predictions = clf.fit(x_train, x_test, y_train, y_test)

# print(models)
# print(predictions.head())

# 성능 좋은 LGBMClassifier (LightGGBM) 사용

lgbm = LGBMClassifier()
lgbm.fit(x_train, y_train)
y_pred = lgbm.predict(x_test)
accuracy_score(y_pred, y_test)

# Scikit-Optimize
# Scikit-learn의 머신러닝 모델들의 파라미터 자동 튜닝 패키지
