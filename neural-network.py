import math
class neuron:
	label = 0


	def __init__(self, bias, isOutput, adjList, layer):
		self.bias = bias
		self.weights = {}
		self.adjList = adjList
		self.label = label
		self.layer = layer
		label += 1


	def net(self):
		net = 0.0
		for eachNode in self.adjList:
			if eachNode.layer < self.layer:
				net += eachNode.weights.key(self.label) * eachNode.output
		return net + self.bias


	def sigmoid(self, net):
		return 1 / (1 + math.exp(-1 * net))


	def output(self):
		self.output = self.sigmoid(self.net())
		return self.output


	def littleDelta(self, target):
		if self.isOutput:
			self.littleDelta = self.output * (1 - self.output) * (target - self.output)
		else:
			sumDownstream = 0.0
			for eachNode in self.adjList:
				if eachNode.layer > self.layer:
					sumDownstream += eachNode.littleDelta * eachNode.weights.key(self.label)
			self.littleDelta = self.output * (1 - self.output) * sumDownstream
		return self.littleDelta


class layer:
	layerNo = 0


	def __init__(self, bias, isOutput, numNeurons, adjList):
		self.bias = bias if bias else random.random
		self.layer = layerNo
		self.neurons = []
		self.isOutput = isOutput
		layerNo += 1

		for i in xrange(numNeurons):
			self.neurons.append(neuron(self.bias, self.isOutput, adjList, self.layer))


	def weightUpdate(self):
		for eachNeuron in self.neurons:
			delta = 0.0
			for eachNode in eachNeuron.adjList:
				if eachNode.layer > eachNeuron.layer:
					delta = eta * eachNode.littleDelta * eachNeuron.output
				eachNode.adjList.weights.key(eachNeuron.label) += delta
				eachNeuron.weights.key(eachNode.label) += delta

	def feedForward(self, input):
		for eachNeuron in self.neurons:
			if self.layer = 0:
				i = 0
				for eachNeuron in self.neurons:
					eachNeuron.output = input[i]
					i += 1
			else:
				eachNeuron.output()
