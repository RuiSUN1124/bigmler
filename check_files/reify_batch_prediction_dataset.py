from bigml.api import BigML
api = BigML()

source1 = api.create_source("iris.csv")
api.ok(source1)

dataset1 = api.create_dataset(source1, \
    {'name': u'iris'})
api.ok(dataset1)

model1 = api.create_model(dataset1, \
    {'name': u'iris'})
api.ok(model1)

batchprediction1 = api.create_batch_prediction(model1, dataset1, \
    {'name': u'iris dataset with iris', 'output_dataset': True})
api.ok(batchprediction1)

dataset2 = api.get_dataset(batchprediction1['object']['output_dataset_resource'])
api.ok(dataset2)

dataset2 = api.update_dataset(dataset2, \
    {'name': u'my_dataset_from_batch_prediction_name'})
api.ok(dataset2)
