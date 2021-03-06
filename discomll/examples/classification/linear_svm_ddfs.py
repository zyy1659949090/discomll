from disco.core import result_iterator

from discomll import dataset
from discomll.classification import linear_svm
from discomll.utils import model_view
from discomll.utils import accuracy


# define training dataset
train = dataset.Data(data_tag=["test:breast_cancer_disc"],
                     data_type="chunk",
                     X_indices=xrange(1, 10),
                     id_index=0,
                     y_index=10,
                     delimiter=",",
                     y_map=["2", "4"],
                     # define mapping parameter. "2" is mapped to 1, "4" is mapped to -1.
                     missing_vals=["?"])  # define missing value symbol

# define test dataset
test = dataset.Data(data_tag=["test:breast_cancer_disc_test"],
                    data_type="chunk",
                    X_indices=xrange(1, 10),
                    id_index=0,
                    y_index=10,
                    delimiter=",",
                    y_map=["2", "4"],  # define mapping parameter. "2" is mapped to 1, "4" is mapped to -1.
                    missing_vals=["?"])  # define missing value symbol

# fit model on training dataset
fit_model = linear_svm.fit(train)

# output model
model = model_view.output_model(fit_model)
print model


# start MR job to predict given test data
predictions = linear_svm.predict(test, fit_model)

# output results
for k, v in result_iterator(predictions):
    print k, v[0]

# measure accuracy
ca = accuracy.measure(test, predictions)
print ca
