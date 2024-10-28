import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
# 1. 准备数据
# 假设特征数据为 features，标签数据为 labels
# features 是一个二维数组，每行代表一个样本的特征向量
# labels 是一个一维数组，包含每个样本的对应类别
dataset1 = pd.read_csv('../Data/train.csv')
features,labels = dataset1.iloc[:,:-1],dataset1.label
dataset2 = pd.read_csv('../Data/test.csv')

# 2. 数据预处理
# 标签编码
label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, labels_encoded, test_size=0.2, random_state=42)



# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, labels_encoded, test_size=0.2, random_state=42)

# 3. 构建模型
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(107,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(6, activation='softmax')  # 输出层使用 softmax 激活函数
])

# 4. 编译模型
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 5. 训练模型
model.fit(X_train, y_train, epochs=500, batch_size=32, validation_data=(X_test, y_test))

# 6. 模型评估
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)