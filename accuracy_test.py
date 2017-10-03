from sklearn.cross_validation import KFold
from categorizer import data_to_array, create_pipline
from database.dbase import get_db_data


def k_fold_test(data):
    k_fold = KFold(n=len(data), n_folds= 6)
    right = 0
    for train_indices, test_indices in k_fold:
        train_text = data.iloc[train_indices]['text'].values
        train_y = data.iloc[train_indices]['class'].values

        test_text = data.iloc[test_indices]['text'].values
        test_y = data.iloc[test_indices]['class'].values

        pipeline.fit(train_text, train_y)
        predictions = pipeline.predict(test_text)
        for i, y in zip(predictions, test_y):
            if i == y:
                right = right + 1
            else:
                print('WRONG: ' + i + ' =/= ' + y)

    accuracy = right/ (len(data) / 100)
    print('accuracy: ' + str(accuracy) + '%')



print('22000 articles available. About 1100 is safe for 4 gb RAM')
limit = input('Set nr of training articles: ')
dbase_data = get_db_data(limit)
data = data_to_array(dbase_data)
pipeline = create_pipline()
k_fold_test(data)