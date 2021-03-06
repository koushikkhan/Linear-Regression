# -*- coding: utf-8 -*-

"""
@author: koushik

Here we'll try to find the estimates of the parameters in a linear regression
model using "Gradient Descent" (also known as batch gradient descent) cost
(or loss) minimization algorithm. First we simulate the dummy data specifying
the parameters and then we build our own code for BGD to find the estimates of
the paremeters.

model:--> "y = a_0 + a_1 * x1 + a_2 * x2 + a_3 * x3 + error"
parameters:--> a_0, a_1, a_2, a_3
specified values:--> 5, 2, 0.85, 3.5
no. of training examples:--> 1000000
"""
import numpy as np


def batch_gradient_descent(init, learning_rate, data_train,
                           target_train, precision):
    """
    init: initial set of parameters
    learning_rate: learning rate for BGD to converge
    data_train: training data (predictors)
    target_train: training data (responses or the targets)
    return: minimum cost and optimized parameters
    """
    N = data_train.shape[0]  # no. of training example available
    step = 1  # no. of step required to converge

    def _gradient(param_vector):
        """
        type: private function
        param_vector: vector of parameters
        return: gradient vector evaluated at
                the given set of parameters
        """
        # prediction error
        error = (target_train - np.dot(data_train, param_vector))
        # gradient vector
        g = (-1 / N) * np.dot(np.transpose(data_train), error)
        return g

    def _cost_function(param_vector):
        """
        type: private function
        param: vector of parameters
        return: cost function evaluated at
                the parameter vector supplied
        """
        target_pred = np.dot(
            data_train, param_vector)  # predicted values of the targets
        cost = np.sum(np.square(target_train - target_pred)) / \
            (2 * N)  # cost due to prediction error
        return cost

    converged = False
    while not converged:
        cost_current = _cost_function(init)
        param_new = init - (learning_rate * _gradient(init))  # learning rule
        cost_new = _cost_function(param_new)  # updated cost

        # absolute value of the cost difference
        cost_diff = abs(cost_new - cost_current)
        converged = bool(cost_diff < precision)
        if step % 20 == 0:
            # prints the summary after each 50th step
            print("Step:{}\tUpdated cost:{:0.4f}\tCost difference:{}\tUpdated parameters:{}".format(
                step, _cost_function(param_new), cost_diff, param_new))
        init = param_new
        step = step + 1

    print("\Batch Gradient Descent Converged!\n")
    print("Minimum cost: {: 0.4f}\tFinal Parameter Estimates: {}".format(
        _cost_function(init), init))
    return _cost_function(init), init


if __name__ == '__main__':
    # Simulation of toy data
    np.random.seed(0)  # set the seed
    X = np.column_stack((np.ones((1000000, 1)), np.random.rand(1000000, 3)))
    error = np.random.randn(1000000)
    y = np.dot(X, np.array([5, 2, 0.85, 3.5]), out=None) + error
    # ---------------------------------------------------------------------- #
    p = np.random.randint(1, 8, size=4)  # initial values of the parameters
    data_train = X
    target_train = y
    learning_rate = 0.00003
    precision = 0.000001
    try:
        batch_gradient_descent(p, learning_rate, data_train,
                               target_train, precision)
    except TypeError:
        print("Please specify the parameters carefully!")
