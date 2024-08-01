from user_lib.preprocessing import return_dict as rd
from sklearn.neighbors import KNeighborsClassifier # knn 분류 모델
from sklearn.tree import DecisionTreeClassifier # tree 분류 모델

_knn_model = None
_tree_model = None

merged_df = rd()
home_df = merged_df[['BLK_home', 'DREB_home', 'FG3_PCT_home', 'FG_PCT_home', 'FT_PCT_home', 'STL_home', 'TO_home']]
away_df = merged_df[['BLK_away', 'DREB_away', 'FG3_PCT_away', 'FG_PCT_away', 'FT_PCT_away', 'STL_away', 'TO_away']]


X = home_df.subtract(away_df.values)
X.columns = ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']
y = merged_df['HOME_TEAM_WINS']


_knn_model = KNeighborsClassifier()
_knn_model.fit(X,y)
_tree_model = DecisionTreeClassifier(max_depth=6,max_leaf_nodes=45,min_samples_leaf=86,min_samples_split=2)
_tree_model.fit(X,y)



def pre_knn(X):    
        '''
        데이터는 home팀기준 away팀과의 박스스코어 차이\n
        예측에 필요한 컬럼은\n
        ['BLK','DREB','FG3_PCT','FG_PCT','FT_PCT','STL','TO']\n
        결과 값은 홈팀의 우승여부
        '''              
        if X is not None and _knn_model is not None:
                return _knn_model.predict(X)
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
                return _tree_model.predict(X)
        else:
                print("정상적인데이터를 넣어주세요")
                return X