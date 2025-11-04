## This script was enhanced by Claude Sonnet 4.5 on 11/2/25

# imports

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import t as t_dist, probplot

# load displacement data

df = pd.read_csv('../data/mean_displacements.csv')

# drop index column

df = df.drop(columns=['Unnamed: 0'])

# converting to long form for easier plotting

df_long = pd.melt(df, var_name='material', value_name='displacement')

# Descriptive statistics tests

plastic_data = df['plastic']
paper_data = df['paper']

plastic_mean = plastic_data.mean()
plastic_sd = plastic_data.std()
plastic_n = len(plastic_data)

paper_mean = paper_data.mean()
paper_sd = paper_data.std()
paper_n = len(paper_data)

print(f"Plastic: M = {plastic_mean:.2f}, SD = {plastic_sd:.2f}, n = {plastic_n}")
print(f"Paper: M = {paper_mean:.2f}, SD = {paper_sd:.2f}, n = {paper_n}")

# Assumption checks for stats test

# 1. Normality - Shapiro-Wilk test

shapiro_plastic = stats.shapiro(plastic_data)
shapiro_paper = stats.shapiro(paper_data)

print(f"Shapiro-Wilk Test (Plastic): W = {shapiro_plastic.statistic:.4f}, p = {shapiro_plastic.pvalue:.4f}")
print(f"Shapiro-Wilk Test (Paper): W = {shapiro_paper.statistic:.4f}, p = {shapiro_paper.pvalue:.4f}")

if shapiro_plastic.pvalue > 0.05 and shapiro_paper.pvalue > 0.05:
    print(" Normality assumption met (p > .05 for both groups)")
else:
    print(" Normality assumption violated for at least one group")

# 2. Homogeneity of variance - Levene's test
levene_result = stats.levene(plastic_data, paper_data)
print(f"Levene's Test: F = {levene_result.statistic:.4f}, p = {levene_result.pvalue:.4f}")

if levene_result.pvalue > 0.05:
    print(" Homogeneity of variance assumption met (p > .05)")
    equal_var = True
else:
    print(" Variances are unequal")
    equal_var = False

# 3. Independent samples t-test

t_result = stats.ttest_ind(plastic_data, paper_data, equal_var=equal_var)

print(f"p-value: {t_result.pvalue:.4f}")

if t_result.pvalue < 0.001:
    print("Result: p < .001 (highly significant)")
elif t_result.pvalue < 0.05:
    print(f"Result: p = {t_result.pvalue:.3f} (significant)")
else:
    print(f"Result: p = {t_result.pvalue:.3f} (not significant)")
print()

# visualizations

# box plot
plt.figure(figsize=(8, 6))
sns.boxplot(data=df_long, x='material', y='displacement')
plt.title('Box Plot: Displacement by Material', fontsize=14, fontweight='bold')
plt.xlabel('Material', fontsize=12)
plt.ylabel('Mean Displacement Distance', fontsize=12)
plt.tight_layout()
plt.savefig('../plots/boxplot.png', dpi=300, bbox_inches='tight')

# violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(data=df_long, x='material', y='displacement')
plt.title('Violin Plot: Displacement by Material', fontsize=14, fontweight='bold')
plt.xlabel('Material', fontsize=12)
plt.ylabel('Mean Displacement Distance', fontsize=12)
plt.tight_layout()
plt.savefig('../plots/violinplot.png', dpi=300, bbox_inches='tight')


# histogram
plt.figure(figsize=(10, 6))
plt.hist(plastic_data, alpha=0.6, label='Plastic', bins=15, edgecolor='black', color='steelblue')
plt.hist(paper_data, alpha=0.6, label='Paper', bins=15, edgecolor='black', color='coral')
plt.title('Histogram: Distribution Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Mean Displacement Distance', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend(fontsize=11)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('../plots/histogram.png', dpi=300, bbox_inches='tight')


# q-q plot plastic
plt.figure(figsize=(8, 8))
probplot(plastic_data, dist="norm", plot=plt)
plt.title('Q-Q Plot: Plastic (Normality Check)', fontsize=14, fontweight='bold')
plt.xlabel('Theoretical Quantiles', fontsize=12)
plt.ylabel('Ordered Values', fontsize=12)
plt.grid(alpha=0.3)
# Change marker color
ax = plt.gca()
ax.get_lines()[0].set_markerfacecolor('steelblue')
ax.get_lines()[0].set_markeredgecolor('steelblue')
ax.get_lines()[0].set_markersize(6)
plt.tight_layout()
plt.savefig('../plots/qq_plot_plastic.png', dpi=300, bbox_inches='tight')

# q-q plot paper
plt.figure(figsize=(8, 8))
probplot(paper_data, dist="norm", plot=plt)
plt.title('Q-Q Plot: Paper (Normality Check)', fontsize=14, fontweight='bold')
plt.xlabel('Theoretical Quantiles', fontsize=12)
plt.ylabel('Ordered Values', fontsize=12)
plt.grid(alpha=0.3)
# Change marker color
ax = plt.gca()
ax.get_lines()[0].set_markerfacecolor('coral')
ax.get_lines()[0].set_markeredgecolor('coral')
ax.get_lines()[0].set_markersize(6)
plt.tight_layout()
plt.savefig('../plots/qq_plot_paper.png', dpi=300, bbox_inches='tight')

