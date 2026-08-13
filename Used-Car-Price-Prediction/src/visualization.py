import matplotlib.pyplot as plt
def plot_model_ranking(results_df):
    plt.figure(figsize=(12,6))
    plt.bar(results_df["Model"],results_df["R2 Score"])
    plt.xticks(rotation=40)
    plt.ylabel("R2 Score")
    plt.title("Regression Model Comparison")
    plt.tight_layout()
    plt.savefig(
        "../outputs/figures/model_comparison.png",
        dpi=300
    )
    plt.show()