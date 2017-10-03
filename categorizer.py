import time

import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from database.dbase import get_db_data


def build_dataframe(dbase_data):
    rows = []
    index = []
    for i in dbase_data:
        rows.append({'text': i[1], 'class': i[2]})
        index.append(i[0])

    data_frame = DataFrame(rows, index=index)
    return data_frame


def get_user_inputs():
    lang_sample = input('Enter text: \n')
    sample = [lang_sample, ]
    print('Number of articles to train data is 22000. The higher amount,'
          ' the better results.\nWARNING: Optimal number for 4GB RAM is 1500-2000.'
          ' Too high amount may result in freezing Your PC !!!')
    limit = input('Enter number: \n')
    print('Please wait....')
    return sample, limit


def data_to_array(dbase_data):
    data = build_dataframe(dbase_data)
    data = data.reindex(numpy.random.permutation(data.index))
    return data


def create_pipline():
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())])
    return pipeline


def fit_n_predict(pipeline, data, sample):
    pipeline.fit(data['text'].values, data['class'].values)
    predictions = pipeline.predict(sample)
    return predictions[0]


if __name__ == '__main__':
    sample, limit = get_user_inputs()
    start_time = time.time()
    dbase_data = list(get_db_data(limit))
    data = data_to_array(dbase_data)
    pipeline = create_pipline()
    prediction = fit_n_predict(pipeline, data, sample)

    end_time = time.time() - start_time
    print('Language detected: ' + str(prediction))
    print('Classification time: %s seconds' % int(end_time))