import numpy as np
from collections import Counter

class Node:
    #*, value=None => value must be passed as keyword argument (explicitly named)
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    #only leaf nodes have value
    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    #n_features = number of features, greedy search over all the features, can loop over the randomized subset
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None #start of tree traversal

    #X = ([samples], [features])
    def fit(self, X, y):
        #if n_features is none choose maximum number of features, check if the n_features is not greater than the max
        if self.n_features:
                min(X.shape[1], self.n_features)
        else:
            self.n_features = X.shape[1]
        #print("X.shape[1]: ", X.shape[1])
        #print("X: ", X)
        self.root = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        #stopping criteria
        if depth >= self.max_depth or n_samples < self.min_samples_split or n_labels == 1:
            counter = Counter(y)
            leaf_value = counter.most_common(1)[0][0] #the most common
            return Node(value=leaf_value)

        feature_indexes = np.random.choice(n_features, self.n_features, replace=False)
        best_threshold, best_feature = self._best_split(X, y, feature_indexes)

        left_indexes, right_indexes = self._split(X[:, best_feature], best_threshold)
        left = self._grow_tree(X[left_indexes,: ], y[left_indexes], depth+1)
        right= self._grow_tree(X[right_indexes,: ], y[right_indexes], depth+1)
        return Node(best_feature, best_threshold, left, right)

    def _best_split(self, X, y, feat_idxs):
        best_gain = -1
        split_index, split_threshold = None, None
        for feature_index in feat_idxs:
            X_column = X[:, feature_index]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self._information_gain(y, X_column, threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_threshold = threshold
                    split_index = feature_index
        return split_threshold, split_index

    #how much information is gained by splitting on different features
    def _information_gain(self, y, X_column, threshold):
        #information gain = entropy(parent) - [average entropy(children)]
        parent_entropy = self._entropy(y)

        left_indexes, right_indexes = self._split(X_column, threshold)

        n_left = len(left_indexes)
        n_right = len(right_indexes)

        if not(n_left or n_right):
            return 0

        n_both = len(y)

        left_entropy = self._entropy(y[left_indexes])
        right_entropy = self._entropy(y[right_indexes])
        average_child_entropy = (n_left/n_both) * left_entropy +  (n_right/n_both) * right_entropy

        information_gain = parent_entropy - average_child_entropy
        return information_gain

    #split by split_threshold, left <= threshold
    def _split(self, X_column, split_threshold):
        left_indexes = [index for index, value in enumerate(X_column) if value <= split_threshold and value is not None]
        #print(left_indexes)
        right_indexes = [index for index, value in enumerate(X_column) if value > split_threshold and value is not None]
        
        return left_indexes, right_indexes

    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist/len(y)
        return -np.sum([p * np.log(p) for p in ps if p>0])

    def _traverse_tree(self, X, node):
        if node.is_leaf_node():
            return node.value
        elif X[node.feature] <= node.threshold:
            return self._traverse_tree(X, node.left)
        else:
            return self._traverse_tree(X, node.right)

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])
