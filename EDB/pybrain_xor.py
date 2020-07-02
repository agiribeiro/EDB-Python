from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers.backprop import BackpropTrainer


dataset = SupervisedDataSet(2, 1)

dataset.addSample([1, 1], [0])
dataset.addSample([1, 0], [1])
dataset.addSample([0, 1], [1])
dataset.addSample([0, 0], [0])

network = buildNetwork(dataset.indim, 2, dataset.outdim, bias=True)

trainer = BackpropTrainer(network, dataset, learningrate=0.01, momentum=0.99)

for epoch in range(1000):
    trainer.train()

test_data = SupervisedDataSet(2, 1)
test_data.addSample([1, 1], [0])
test_data.addSample([1, 0], [1])
test_data.addSample([0, 1], [1])
test_data.addSample([0, 0], [0])

trainer.testOnData(test_data, verbose=True)
