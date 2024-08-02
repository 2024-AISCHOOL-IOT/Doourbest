#!/usr/bin/env python
# coding: utf-8

# #### 대조군 비교 모델
# - KNN
# - DT
# - RF

# In[2]:


# 환경셋팅
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier  # knn 분류 모델
from sklearn.tree import DecisionTreeClassifier # dt 분류 모델
from sklearn.ensemble import RandomForestClassifier # rf 분류 모델
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


# #### 데이터 전처리

# In[4]:


# def data_preprocessing():
#     """
#     - pd.read_csv('./archive/games.csv') 이 경로는 환경에 맞게 고쳐주세요!
#     - 모든 모델 공통
#     """
#     # 데이터를 불러와서 data 변수에 담기
#     data = pd.read_csv('./archive/games.csv')
#     # 결측치 처리
#     data['PTS_home'].isnull().sum()
#     # 데이터 가공
#     data[data['PTS_home'].isnull()][['PTS_home','FG_PCT_home','FT_PCT_home','FG3_PCT_home','AST_home','REB_home']].isna().sum()
#     data1 = data.dropna()
#     return data1


# #### 모델 훈련 준비

# In[6]:


# def prepare_model_training(data1):
def prepare_model_training():
    """
    - pd.read_csv('./archive/preprocessed_games.csv') 이 경로는 환경에 맞게 고쳐주세요!
    - 모든 경기에 대해서 학습을 시킬겁니다.
    - 문제 컬럼: 'FG_PCT_home','FG_PCT_away','FT_PCT_home','FT_PCT_away'
      답 컬럼: 'HOME_TEAM_WINS'
    - 모든 모델 공통
    """
    # 데이터를 불러와서 data 변수에 담기
    data1 = pd.read_csv('./data/preprocessed_games.csv')
    # 문제와 답 (열 분리)
    # 훈련셋과 테스트셋 분리 (행 분리)
    test_data = data1[['FG_PCT_home','FG_PCT_away','FT_PCT_home','FT_PCT_away','HOME_TEAM_WINS']]
    X_train = test_data.iloc[:,:4]
    y_train = test_data.iloc[:,4]
    return X_train,y_train


# #### KNN 모델 훈련

# In[8]:


def knn_model_training(X_train,y_train):
    """
    - 모든 경기에 대해서 학습을 시킬겁니다.
    """
    # 모델 객체 생성 (+ 하이퍼 파라미터 설정)
    knn_model = KNeighborsClassifier(n_neighbors=56)
    # 모델 학습
    knn_model.fit(X_train,y_train)
    return knn_model


# #### DT 모델 훈련

# In[10]:


def tree_model_training(X_train,y_train):
    """
    - 모든 경기에 대해서 학습을 시킬겁니다.
    """
    # 모델 객체 생성 (+ 하이퍼 파라미터 설정)
    tree_model = DecisionTreeClassifier(max_depth=4)
    # 모델 학습
    tree_model.fit(X_train, y_train)
    return tree_model


# #### RF 모델 훈련

# In[12]:


def rf_model_training(X_train,y_train):
    """
    - 모든 경기에 대해서 학습을 시킬겁니다.
    """
    # 모델 객체 생성 (+ 하이퍼 파라미터 설정)
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=8, 
                                min_samples_leaf=6, min_samples_split=2, random_state=5)
    # 모델 학습
    rf_model.fit(X_train, y_train)
    return rf_model


# #### KNN 모델 예측

# In[14]:


def knn_model_prediction(knn_model,FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away):
    """
    홈 팀 기준에서 예측한 결과가 반환됩니다.
    """
    X_test=pd.DataFrame([[FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away]],columns=['FG_PCT_home','FG_PCT_away','FT_PCT_home','FT_PCT_away'])
    return knn_model.predict(X_test) 


# #### DT 모델 예측

# In[16]:


def tree_model_prediction(tree_model,FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away):
    """
    홈 팀 기준에서 예측한 결과가 반환됩니다.
    """
    X_test=pd.DataFrame([[FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away]],columns=['FG_PCT_home','FG_PCT_away','FT_PCT_home','FT_PCT_away'])
    return tree_model.predict(X_test) 


# #### RF 모델 예측

# In[18]:


def rf_model_prediction(rf_model,FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away):
    """
    홈 팀 기준에서 예측한 결과가 반환됩니다.
    """
    X_test=pd.DataFrame([[FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away]],columns=['FG_PCT_home','FG_PCT_away','FT_PCT_home','FT_PCT_away'])
    return rf_model.predict(X_test) 


# #### 교차 검증 수행

# In[20]:


# KNN 모델 교차 검증
def knn_model_cv(knn_model,X_train,y_train):
    # 교차 검증 수행
    knn_result = cross_val_score(knn_model, X_train, y_train, cv=5)
    # 결과 출력
    print(f"교차 검증 점수: {knn_result}")
    print(f"평균 교차 검증 점수: {knn_result.mean()}")


# In[21]:


# DT 모델 교차 검증
def tree_model_cv(tree_model,X_train,y_train):
    # 교차 검증 수행
    tree_result = cross_val_score(tree_model, X_train, y_train, cv=5)
    # 결과 출력
    print(f"교차 검증 점수: {tree_result}")
    print(f"평균 교차 검증 점수: {tree_result.mean()}")


# In[22]:


# RF 모델 교차 검증
def rf_model_cv(rf_model,X_train,y_train):
    # 교차 검증 수행
    rf_result = cross_val_score(rf_model, X_train, y_train, cv=5)
    # 결과 출력
    print(f"교차 검증 점수: {rf_result}")
    print(f"평균 교차 검증 점수: {rf_result.mean()}")


# #### 최종 대조군 모델 학습 함수

# In[65]:


def knn_control_model_training():
    # 데이터 전처리
    # data1=data_preprocessing()
    # 모델 훈련 준비
    X_train,y_train=prepare_model_training()
    # KNN 모델 훈련
    knn_model=knn_model_training(X_train,y_train)
    return knn_model


# In[67]:


def tree_control_model_training():
    # 데이터 전처리
    # data1=data_preprocessing()
    # 모델 훈련 준비
    X_train,y_train=prepare_model_training()
    # DT 모델 훈련
    tree_model=tree_model_training(X_train,y_train)
    return tree_model


# In[69]:


def rf_control_model_training():
    # 데이터 전처리
    # data1=data_preprocessing()
    # 모델 훈련 준비
    X_train,y_train=prepare_model_training()
    # RF 모델 훈련
    rf_model=tree_model_training(X_train,y_train)
    return rf_model


# #### 최종 대조군 모델 예측 함수

# In[24]:


def knn_control_model_prediction(knn_model,fg_pct_home,fg_pct_away,ft_pct_home,ft_pct_away):
    """
    - 모델 예측 값이 1이면 "홈 팀 승리"라고 출력하고,
      모델 예측 값이 0이면 "원정 팀 승리"라고 출력합니다.
    """
    # 데이터 전처리
    # data1=data_preprocessing()
    # 모델 훈련 준비
    # X_train,y_train=prepare_model_training(data1)
    # X_train,y_train=prepare_model_training()
    # KNN 모델 훈련
    # knn_model=knn_model_training(X_train,y_train)
    # KNN 모델 예측
    pre=knn_model_prediction(knn_model,fg_pct_home,fg_pct_away,ft_pct_home,ft_pct_away)
    return pre[0]
    # 교차 검증
    # knn_model_cv(knn_model,X_train,y_train)


# In[26]:


def tree_control_model_prediction(tree_model,FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away):
    """
    - 모델 예측 값(pre[0])이 1이면 1을 리턴하고,
      모델 예측 값(pre[0])이 0이면 0을 리턴합니다.
    """
    # DT 모델 훈련
    # tree_model=tree_model_training()
    # DT 모델 예측
    pre=tree_model_prediction(tree_model,FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away)
    return pre[0]


# #### RF 대조군 모델 최종 함수

# In[28]:


def rf_control_model_prediction(rf_model,FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away):
    """
    - 모델 예측 값(pre[0])이 1이면 1을 리턴하고,
      모델 예측 값(pre[0])이 0이면 0을 리턴합니다.
    """
    # RF 모델 훈련
    # rf_model=rf_model_training()
    # RF 모델 예측
    pre=rf_model_prediction(rf_model,FG_PCT_home,FG_PCT_away,FT_PCT_home,FT_PCT_away)
    return pre[0]


# In[71]:


# 예시
# rf_control_model_training()
# rf_control_model_prediction(0.484,0.001,0.786,0.735)
