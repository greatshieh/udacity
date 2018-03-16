'''
根据商店的id，合并train.csv， test.csv和store.csv中的数据
'''
import pandas as pd 
import pickle
from util import dataset

train = pd.read_csv('../data/train.csv')
test = pd.read_csv('../data/test.csv')

print(len(test['Open']==1))