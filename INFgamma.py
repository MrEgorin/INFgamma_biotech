import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Симуляція даних (замініть на ваші реальні дані)
np.random.seed(0)
plasmid_data = np.random.normal(loc=100, scale=10, size=30)  # Вихід із плазмідою (середнє 100 мг/л)
phage_data = np.random.normal(loc=110, scale=15, size=30)    # Вихід із бактеріофагом (середнє 110 мг/л)

# Створення DataFrame
df = pd.DataFrame({
    'Technology': ['Plasmid']*30 + ['Phage']*30,
    'Yield': np.concatenate([plasmid_data, phage_data])
})

# Статистичний аналіз: t-тест
t_stat, p_value = stats.ttest_ind(plasmid_data, phage_data)
print(f"T-статистика: {t_stat:.2f}, p-значення: {p_value:.4f}")

# Візуалізація: коробчаста діаграма
sns.boxplot(x='Technology', y='Yield', data=df)
plt.title('Порівняння виходу IFN-γ між технологіями')
plt.ylabel('Вихід IFN-γ (мг/л)')
plt.show()

# Інтерпретація результатів
if p_value < 0.05:
    print("Існує статистично значуща різниця у виході IFN-γ між плазмідною та бактеріофаговою технологіями.")
else:
    print("Немає статистично значущої різниці у виході IFN-γ між технологіями.")