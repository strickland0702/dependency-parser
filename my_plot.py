# import torch 
# import numpy as np

# tensor1 = torch.Tensor([[1,2,3,4], [2,4,6,8]])

# print(tensor1)
# print(tensor1.pow(3))

import seaborn as sns
import matplotlib.pyplot as plt

index = [1,2,3,4,5]
data_1 = [76.89, 81.16, 83.16, 84.07, 84.80]
data_2 = [76.26, 80.48, 82.34, 83.88, 83.91]
data_3 = [76.67, 80.92, 83.13, 83.89, 84.79]

ref_data = [82.33, 85.48, 86.51, 87.57, 88.00]
new_data = [82.48, 86.48, 87.34, 87.82, 88.48]

# sns.lineplot(x=index, y=data_1, label = "original model")
# sns.lineplot(x=index, y=data_2)
# sns.lineplot(x=index, y=data_3)

sns.lineplot(x=index, y=data_1, label = "original model")
sns.lineplot(x=index, y=ref_data, label = "reference model")
sns.lineplot(x=index, y=new_data, label = "new model")

plt.title("UAS Score For Each Training Epoch")
plt.xlabel("Epoch")
plt.ylabel("UAS Score")
plt.savefig("compare_uas_score.jpg")
plt.show()
