import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_confusion_matrix(cm, model_name="Model", save_path=None):
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['REAL', 'FAKE'], yticklabels=['REAL', 'FAKE'], ax=ax)
    ax.set_xlabel('Predicted Label', fontsize=12)
    ax.set_ylabel('True Label', fontsize=12)
    ax.set_title(f'Confusion Matrix - {model_name}', fontsize=14, fontweight='bold')
    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        plt.close()
    return fig

def plot_model_comparison(results, save_path=None):
    models = list(results.keys())
    accuracies = [results[m]["accuracy"] * 100 for m in models]
    f1_scores = [results[m]["f1_score"] * 100 for m in models]

    x = np.arange(len(models))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, accuracies, width, label='Accuracy (%)', color='#3b82f6')
    ax.bar(x + width/2, f1_scores, width, label='F1-Score (%)', color='#8b5cf6')

    ax.set_ylabel('Score (%)', fontsize=12)
    ax.set_title('Fake News Classification Algorithm Benchmark Comparison', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(models, rotation=15, ha='right', fontsize=10)
    ax.legend()
    ax.set_ylim(0, 105)
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        plt.close()
    return fig
