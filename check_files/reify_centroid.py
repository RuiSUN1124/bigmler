from bigml.api import BigML
api = BigML()

source1 = api.create_source("iris.csv")
api.ok(source1)

dataset1 = api.create_dataset(source1, \
    {'name': u'iris dataset'})
api.ok(dataset1)

cluster1 = api.create_cluster(dataset1, \
    {'name': u"iris dataset's cluster"})
api.ok(cluster1)

centroid1 = api.create_centroid(cluster1, \
    {u'petal length': 0.5,
     u'petal width': 0.5,
     u'sepal length': 1,
     u'sepal width': 1,
     u'species': u'Iris-setosa'}, \
    {'name': u'my_centroid_name'})
api.ok(centroid1)
