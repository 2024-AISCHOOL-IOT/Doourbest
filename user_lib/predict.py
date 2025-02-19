import pandas as pd
from sklearn.neighbors import KNeighborsClassifier # knn 분류 모델
from sklearn.tree import DecisionTreeClassifier # tree 분류 모델
from sklearn.ensemble import RandomForestClassifier # rf 분류 모델

merged_df = pd.read_csv('./data/refined.csv',encoding='utf-8')
home_df = merged_df[['BLK_home', 'DREB_home', 'FG3_PCT_home', 'FG_PCT_home', 'FT_PCT_home', 'STL_home', 'TO_home']]
away_df = merged_df[['BLK_away', 'DREB_away', 'FG3_PCT_away', 'FG_PCT_away', 'FT_PCT_away', 'STL_away', 'TO_away']]


X = home_df.subtract(away_df.values)
X.columns = ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']
y = merged_df['HOME_TEAM_WINS']


_knn_model = KNeighborsClassifier()
_knn_model.fit(X,y)
_tree_model = DecisionTreeClassifier(max_depth=6,max_leaf_nodes=45,min_samples_leaf=86,min_samples_split=2)
_tree_model.fit(X,y)
_rf_model = RandomForestClassifier(max_depth=40, min_samples_leaf=4, min_samples_split=5,n_estimators=400)
_rf_model.fit(X,y)


def pre_knn(X):    
        '''
        데이터는 home팀기준 away팀과의 박스스코어 차이\n
        예측에 필요한 컬럼은\n
        ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']\n
        결과 값은 홈팀의 우승여부
        '''              
        if X is not None and _knn_model is not None:
                return _knn_model.predict(X)[0]
        else:
                print("정상적인데이터를 넣어주세요")
                return X

def pre_tree(X):
        '''
        데이터는 home팀기준 away팀과의 박스스코어 차이\n
        예측에 필요한 컬럼은\n
        ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']\n
        결과 값은 홈팀의 우승여부
        '''
        if X is not None and _tree_model is not None:
                return _tree_model.predict(X)[0]
        else:
                print("정상적인데이터를 넣어주세요")
                return X

def pre_rf(X):
        '''
        데이터는 home팀기준 away팀과의 박스스코어 차이\n
        예측에 필요한 컬럼은\n
        ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']\n
        결과 값은 홈팀의 우승여부
        '''
        if X is not None and _rf_model is not None:
                return _rf_model.predict(X)[0]
        else:
                print("정상적인데이터를 넣어주세요")
                return X