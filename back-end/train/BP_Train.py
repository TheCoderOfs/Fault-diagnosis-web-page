import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# 定义BP神经网络类
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # 初始化权重和偏置
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.b1 = np.zeros((1, self.hidden_size))
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        self.b2 = np.zeros((1, self.output_size))

    def forward(self, X):
        # 前向传播
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.softmax(self.z2)
        return self.a2

    def backward(self, X, y, learning_rate):
        # 反向传播
        m = X.shape[0]

        delta2 = self.a2 - y
        dW2 = np.dot(self.a1.T, delta2) / m
        db2 = np.sum(delta2, axis=0) / m

        delta1 = np.dot(delta2, self.W2.T) * self.sigmoid_derivative(self.a1)
        dW1 = np.dot(X.T, delta1) / m
        db1 = np.sum(delta1, axis=0) / m

        # 更新权重和偏置
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # 前向传播和反向传播
            output = self.forward(X)
            self.backward(X, y, learning_rate)

            # 打印损失
            loss = self.cross_entropy_loss(output, y)
            if epoch % 100 == 0:
                print('Epoch', epoch, 'Loss:', loss)

    def predict(self, X):
        # 预测
        output = self.forward(X)
        return np.argmax(output, axis=1)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def softmax(self, x):
        exps = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exps / np.sum(exps, axis=1, keepdims=True)

    def cross_entropy_loss(self, y_pred, y_true):
        m = y_true.shape[0]
        loss = -np.sum(y_true * np.log(y_pred + 1e-8)) / m
        return loss


# 加载和准备数据，假设训练数据为train_features和train_labels，测试数据为test_features和test_labels
dataset1 = pd.read_csv('../Data/train.csv')
features,labels = dataset1.iloc[:,:-1],dataset1.label
dataset2 = pd.read_csv('../Data/test.csv')
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=42)
# 将类别标签转换为独热编码
train_labels = np.eye(6)[train_labels]
# test_labels = np.eye(6)[test_labels]
test_labels = test_labels.tolist()

# 创建BP神经网络对象
input_size = 107
hidden_size = 64
output_size = 6
nn = NeuralNetwork(input_size, hidden_size, output_size)

# 训练神经网络
epochs = 1000
learning_rate = 0.01
nn.train(train_features, train_labels, epochs, learning_rate)

# 测试神经网络
predictions = nn.predict(test_features)
predictions = predictions.tolist()
all = len(predictions)
cont = 0
for i in range(all):
    if predictions[i] == test_labels[i]:
        cont+=1
print("accuracy:"+str(cont/all))