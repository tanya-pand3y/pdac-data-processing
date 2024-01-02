import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy.random as rnd
import pandas as pd
from sklearn.decomposition import PCA

file_path = 'processed-tumour-DSP.tsv'  # directory
df = pd.read_csv(file_path, sep='\t', header=None, dtype=str)
list_of_lists = df.values.tolist()
data_list = df.values
modified_data_list = [inner_list[1:] for inner_list in data_list]  # rid of row
final_modified_data_list = modified_data_list[1:]  # rid of first row mixed data

data = np.array(final_modified_data_list)  # convert to NumPy array

# pca = PCA(n_components=2)
# principal_components = pca.fit_transform(data)  # normalise data var=1, unit=0
#
# matplotlib.use('TkAgg')
# # plt.scatter(data[:, 0], data[:, 1], label='Original Data', alpha=0.5)
# plt.scatter(principal_components[:, 0], principal_components[:, 1],
#             label='Original Data', alpha=0.5)
# plt.quiver(0, 0, pca.components_[0, 0], pca.components_[0, 1], scale=3,
#            scale_units='xy', color='red', label='PC1')
# plt.quiver(0, 0, pca.components_[1, 0], pca.components_[1, 1], scale=3,
#            scale_units='xy', color='blue', label='PC2')
# plt.title('PCA of Pancreatic Cancer Cell Types')
# plt.xlabel('Principal Component 1')
# plt.ylabel('Principal Component 2')
# plt.legend()
# plt.show()

matplotlib.use('TkAgg')
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data)

pc1 = principal_components[:, 0]
pc2 = principal_components[:, 1]

plt.scatter(pc1, pc2, c=range(len(pc1)), cmap='viridis', label='Original Data',
            alpha=0.5)
plt.quiver(0, 0, pca.components_[0, 0], pca.components_[0, 1], scale=3,
           scale_units='xy', color='red', label='PC1')
plt.quiver(0, 0, pca.components_[1, 0], pca.components_[1, 1], scale=3,
           scale_units='xy', color='blue', label='PC2')
plt.title('PCA of Pancreatic Cancer Cell Types')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.colorbar(label='Data Point Index')
plt.show()
