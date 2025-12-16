# Differential Gene Expression Analysis (EMBL Data)

## 📌 Project Overview
This project performs a differential expression analysis comparing **Control vs. Treated** samples. The dataset was obtained from the **EMBL (European Molecular Biology Laboratory)** database.

The goal of this analysis is to identify significantly differentially expressed genes (DEGs) and visualize the results using custom Python functions.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Input Data:** TSV format (Tab-Separated Values)

## 📊 Key Features
* **Data Preprocessing:** Loading and cleaning raw TSV data from EMBL.
* **Custom Analysis Functions:** Python functions created to automate the statistical filtering and processing.
* **Visualization:**
    * **Volcano Plot:** To visualize the relationship between Fold Change and Statistical Significance (P-value).
    * **Heatmap:** To display expression patterns across samples.

## 📂 Project Structure
```text
├── Data/               # Raw data files (TSV from EMBL)
├── notebooks/          # Jupyter Notebooks with analysis (e.g., Analysis.ipynb)
├── results/            # Output images and processed files
├── scripts/            # Python scripts (.py) containing custom functions
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
