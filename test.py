from user_lib import predict
import pandas as pd

#예측 모델 테스트용 파이썬

# 첫 번째 데이터프레임
data1 = {
    'BLK': [6.0],
    'DREB': [27.0],
    'FG3_PCT': [0.157143],
    'FG_PCT': [0.493643],
    'FT_PCT': [5.958],
    'STL': [13.0],
    'TO': [21.0]
}

# 두 번째 데이터프레임
data2 = {
    'BLK': [3.0],
    'DREB': [26.0],
    'FG3_PCT': [0.083333],
    'FG_PCT': [0.3755],
    'FT_PCT': [3.375],
    'STL': [11.0],
    'TO': [22.0]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
#KNN 모델 기반 home팀기준 away팀과의 박스스코어 차이를 기준으로 홈팀의 승리 예측
pre1 = predict.pre_knn(df1.subtract(df2.values))
#DecisionTree 모델 기반 home팀기준 away팀과의 박스스코어 차이를 기준으로 홈팀의 승리 예측
pre2 = predict.pre_tree(df1.subtract(df2.values))
#RandomForest 모델 기반 home팀기준 away팀과의 박스스코어 차이를 기준으로 홈팀의 승리 예측
pre3 = predict.pre_rf(df1.subtract(df2.values))

print(pre1)
print(pre2)
print(pre3)