import numpy as np
import networkx as nx

class Neuron:  
    def __init__(self, n_inputs, bias=0., weights=None):  
        self.b = bias
        if weights is not None:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):  # activation function (here: leaky_relu)
        return max(0.1 * x, x)   

    def __call__(self, xs):  # calculate the neuron's output
        return self._f(xs @ self.ws + self.b) 
    
class Layer:
    def __init__(self, n_neurons, n_inputs): #kazdy z kazdym
        self.layer =  np.array([Neuron(n_inputs) for i in range(n_neurons)])
    def __call__(self, xs):
        return np.array([neuron(xs) for neuron in self.layer])

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers

    def __call__(self, xs):
        for layer in self.layers:
            xs = layer(xs)
        return xs

    def generate_pos(self, n_nodes, j, last_max):
        return {i+last_max: (i, j) for i in range(n_nodes)}
    
    def generate_edges(self, cur_layer, prev_layer, G):
      for i in cur_layer:
        for j in prev_layer:
          G.add_edge(j, i)

  
    def visualize(self):
      G = nx.DiGraph()
      prev_layer = []
      cur = 0
      max = 0
      all = 0
      pos = {}
      pos_cur = {}
      for (i, layer) in enumerate(self.layers):
        nodes_to_draw = []
        all += max
        for (j, node) in enumerate(layer.layer):          
            nodes_to_draw.append(cur)
            cur += 1
        max = layer.layer.shape[0]
        pos_cur = self.generate_pos(max, i, all)
        pos.update(pos_cur)
        G.add_nodes_from(nodes_to_draw)
        self.generate_edges(nodes_to_draw, prev_layer, G)   
        nx.draw(G, pos)
        prev_layer = nodes_to_draw
               
      

input_layer = Layer(3, 3)
hidden_layer1 = Layer(4, 3)
hidden_layer2 = Layer(4, 4)
output_layer = Layer(1, 4)

ann = NeuralNetwork([input_layer, hidden_layer1, hidden_layer2, output_layer])

# result = ann(np.array([0.5, 0.1, 0.3]))
# print(result)

ann.visualize()
