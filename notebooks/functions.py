
from pathlib import Path
from sklearn.base import BaseEstimator, TransformerMixin, clone
from sklearn.utils.metaestimators import available_if
from sklearn.utils.validation import check_is_fitted
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


def generate_source_filename(name=None, year=2017):
    if name == 'depot': 
        return 'depots_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)
    elif name == 'secteur': 
        return 'secteurs_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)
    elif name == 'transaction': 
        return 'transactions_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)
    elif name == 'contrat': 
        return 'contrats_deneigement_saison_{s}-{e}.csv'.format(s=year,e=year+1)        
    else:
        raise 'name should be depot, secteur, transaction, contrat'
        return None

def generate_source_path(name=None,year=2017, prepath='./'):
    if name == 'depot':
        return Path(prepath,'data','depot',generate_source_filename(name,year))
    if name == 'secteur':
        return Path(prepath,'data','secteur',generate_source_filename(name,year))    
    if name == 'transaction':
        return Path(prepath,'data','transaction',generate_source_filename(name,year))
    if name == 'contrat':
        return Path(prepath,'data','contrat',generate_source_filename(name,year))
    else:
        return None
    


def _classifier_has(attr):
    """Check if we can delegate a method to the underlying classifier.

    First, we check the first fitted classifier if available, otherwise we
    check the unfitted classifier.
    """
    return lambda estimator: (
        hasattr(estimator.classifier_, attr)
        if hasattr(estimator, "classifier_")
        else hasattr(estimator.classifier, attr)
    )

class InductiveClusterer(BaseEstimator):
    def __init__(self, clusterer, classifier):
        self.clusterer = clusterer
        self.classifier = classifier

    def fit(self, X, y=None):
        self.clusterer_ = clone(self.clusterer)
        self.classifier_ = clone(self.classifier)
        y = self.clusterer_.fit_predict(X)
        self.classifier_.fit(X, y)
        return self

    @available_if(_classifier_has("predict"))
    def predict(self, X):
        check_is_fitted(self)
        return self.classifier_.predict(X)

    @available_if(_classifier_has("decision_function"))
    def decision_function(self, X):
        check_is_fitted(self)
        return self.classifier_.decision_function(X)

    @available_if(_classifier_has("score"))
    def score(self, X, y=None):
        check_is_fitted(self)
        return self.classifier_.score(X,y)       


class KMeansTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, **kwargs):
        # The purpose of 'self.model' is to contain the
        # underlying cluster model-
        self.model = KMeans(**kwargs)
        #super(KMeansTransformer, self).__init__(**kwargs)
        #super().__init__(**kwargs)
        

    def fit(self, X):
        self.X = X
        self.model.fit(X)


    def transform(self, X):
        pred = self.model.predict(X)
        return np.hstack([self.X, pred.reshape(-1, 1)])


    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)    
        



        
def year_month_date_to_string(date):
    return date.strftime('%Y%m')

def resample(df, index):
    d = df.set_index(index)
    return d.resample('1T', kind='timestamp').bfill()

def datetime_attributes(df, column, attribute=['year', 'month', 'day', 'hour', 'dayofyear', 'quarter']):
    # define generator expression of series, one for each attribute
    date_gen = (getattr(df[column].dt, i).rename(i) for i in attribute)
    return pd.concat(date_gen, axis=1)

def datetime_isocalendar(df, column, attribute=['year','week', 'weekday']):
    date_gen =  df.apply(lambda x: x[column].isocalendar(), axis=1, result_type='expand')
    return date_gen.rename(columns= dict((i,j) for i,j in enumerate(attribute)) )
       
