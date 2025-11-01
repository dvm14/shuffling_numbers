import math
from statsmodels.stats.power import TTestIndPower

effect_size = 0.5
alpha = 0.05
power = 0.8

analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='larger')

print("Sample size=", sample_size)
