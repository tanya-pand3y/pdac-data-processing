import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

file_path = 'processed-tumour-DSP.tsv'
df = pd.read_csv(file_path, sep='\t', index_col=0).T  # transpose matrix

matplotlib.use('TkAgg')  # this is needed to run matplotlib on my laptop, otherwise cuases error: partial initialisation

pca = PCA()
pca_space = pca.fit_transform(df)  # normalise the data and its variance
pca_space_df = pd.DataFrame(pca_space, index=df.index)

clustering = KMeans(4, random_state=42)  # random state used for reproducibility
clusters = clustering.fit_predict(pca_space_df)

scatter = plt.scatter(pca_space_df[0], pca_space_df[1], c=clusters,
                      cmap='viridis', marker='o')

legend_labels = ['Tumor (glandular/poor)', 'PanIN', 'Acinar', 'Normal Ductal']  # legend names
plt.legend(handles=scatter.legend_elements()[0], labels=legend_labels, title='Clusters', loc='upper right')

plt.title('PCA plot of gene expression in 4 different patients')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

