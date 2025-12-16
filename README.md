# Differential Expression Analysis (EMBL Data)

Analysis of differential gene expression using public data from the EMBL database. The project focuses on comparing **Control vs. Treated** samples to identify significant changes in gene expression.
This project analyzes differential gene expression in Renal Cell Carcinoma (RCC), using data from the E-PROT-59 study. Red points indicate significant up-regulation, while blue points represent down-regulation.

## Project Overview
I developed a custom pipeline in Python to process raw TSV data, filter for statistical significance, and visualize the results. The goal was to build reusable functions for differential analysis.

**Key features:**
* **Data Processing:** Parsing and cleaning TSV files using Pandas.
* **Statistical Analysis:** Filtering genes based on Fold Change and P-value.
* **Visualization:**
    * **Volcano Plots:** To visualize significant Up/Down-regulated genes.
    * **Heatmaps:** To inspect expression clusters across different samples.

## Tools Used
* **Python**
* **Pandas & NumPy** (Data manipulation)
* **Matplotlib & Seaborn** (Data visualization)

## Repository Structure
* `Data/`: Contains the raw dataset (TSV format).
* `notebooks/`: Jupyter notebooks with the step-by-step analysis.
* `results/`: Output images and exported tables.
* `scripts/`: Python scripts containing the custom functions used in the notebooks.

## How to run
1.  Clone the repository.
2.  Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```
3.  Open the notebooks in the `notebooks/` folder to explore the analysis.
