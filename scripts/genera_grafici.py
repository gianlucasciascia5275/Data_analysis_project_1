
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_final_volcano(df, output_path="results/volcanoplot.png"):
    print("Elaborazione dati e generazione grafico...")

    # Nomi colonne presi dal tuo codice
    fold_change_col = "'clear cell renal cell carcinoma' vs 'normal' .foldChange"
    pvalue_col = "'clear cell renal cell carcinoma' vs 'normal'.pValue"

    # Pulizia dati
    df_clean = df[[ "Gene ID", "Gene Name", fold_change_col, pvalue_col ]].dropna().copy()

    # Calcoli
    df_clean["minus_log10_pvalue"] = -np.log10(df_clean[pvalue_col])

    # Classificazione
    def classify_gene(row):
        if row[pvalue_col] < 0.05 and row[fold_change_col] >= 1:
            return "Up-regulated"
        elif row[pvalue_col] < 0.05 and row[fold_change_col] <= -1:
            return "Down-regulated"
        else:
            return "Not significant"

    df_clean["Regulation"] = df_clean.apply(classify_gene, axis=1)

    # Plotting
    plt.figure(figsize=(9,7))
    colors = {"Up-regulated": "red", "Down-regulated": "blue", "Not significant": "lightgrey"}

    for category, color in colors.items():
        subset = df_clean[df_clean["Regulation"] == category]
        plt.scatter(
            subset[fold_change_col],
            subset["minus_log10_pvalue"],
            c=color, label=category, alpha=0.6, s=20
        )

    plt.axhline(-np.log10(0.05), linestyle="--", color="black", linewidth=0.8)
    plt.axvline(1, linestyle="--", color="black", linewidth=0.8)
    plt.axvline(-1, linestyle="--", color="black", linewidth=0.8)

    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10(p-value)")
    plt.title("Volcano plot: Clear cell renal cell carcinoma vs Normal")
    plt.legend()
    plt.tight_layout()

    # Salvataggio
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_output_path = os.path.join(base_path, output_path)
    os.makedirs(os.path.dirname(full_output_path), exist_ok=True)
    plt.savefig(full_output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Grafico salvato in: {full_output_path}")
    plt.close()
