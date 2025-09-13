import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return np.sin(np.log(x))

a = 3
b = 8
n = 20  
x_points = np.linspace(a, b, n)
y_values = f(x_points)
print("Точки разбиения отрезка [a, b]:")
print(np.round(x_points, 4))
print("\nЗначения функции y = sin(ln(x)) в этих точках:")
print(np.round(y_values, 4))

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_values, 
         color='royalblue', 
         linewidth=2.5, 
         label=r'$y = \sin(\ln(x))$')
plt.title('График функции $y = \\sin(\\ln(x))$ на отрезке [3, 8]', 
          fontsize=16, 
          fontweight='bold', 
          pad=20)
plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('y', fontsize=14, fontweight='bold', rotation=0)
plt.legend(fontsize=12, 
           loc='upper right', 
           framealpha=0.9, 
           shadow=True)
plt.tight_layout()
plt.show()

plt.scatter(x_points, y_values, 
           marker='D',          
           color=(0.2, 0.4, 0.6),  
           s=60,               
           alpha=0.8,           
           linewidth=0.5,      
           label=r'$y = \sin(\ln(x))$')
plt.title('Точечный график функции $y = \\sin(\\ln(x))$ на отрезке [3, 8]', 
          fontsize=16, 
          fontweight='bold', 
          pad=20)
plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('y', fontsize=14, fontweight='bold', rotation=0)
plt.grid(True, 
         color=(0.7, 0.7, 0.7),  
         alpha=0.4,              
         linestyle='-',          
         linewidth=0.8)
plt.legend(fontsize=12, 
           loc='upper right', 
           framealpha=0.9,
           shadow=True)
plt.tight_layout()
plt.show()

n = 100
low, high = 0, 100
uniform_sample = np.random.randint(low, high + 1, n)
normal_sample = np.clip(np.random.normal(50, 15, 100), 0, 100).astype(int)
plt.hist(uniform_sample, 
         bins=15,  
         color=(0.2, 0.6, 0.8),  
         alpha=0.7, 
         edgecolor='black', 
         linewidth=0.8, 
         density=True,  
         label='Равномерное распределение')
plt.hist(normal_sample, 
         bins=25, 
         color=(0.8, 0.4, 0.4), 
         alpha=0.7,  
         edgecolor='black',  
         linewidth=0.8,  
         density=True,  
         label='Нормальное распределение')
plt.title('Сравнение равномерного и нормального распределений', 
          fontsize=16, 
          fontweight='bold', 
          pad=20)
plt.tight_layout()
plt.show()

sample = np.random.randint(1, 5, 50)
unique, counts = np.unique(sample, return_counts=True)
frequency = dict(zip(unique, counts))
colors = [
    (0.8, 0.2, 0.2),
    (0.2, 0.6, 0.8),
    (0.4, 0.8, 0.4),
    (0.8, 0.6, 0.2)
]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
wedges, texts, autotexts = ax1.pie(counts,
                                   labels=[f'Число {x}' for x in unique],
                                   colors=colors,
                                   autopct='%1.1f%%',
                                   startangle=90,
                                   shadow=True)
ax1.set_title('Круговая диаграмма частот чисел\n(50 чисел от 1 до 5)', 
              fontsize=14, fontweight='bold', pad=20)
bars = ax2.bar(unique, counts, 
               color=colors,
               linewidth=1.2,
               alpha=0.8)
ax2.set_title('Столбчатая диаграмма частот чисел', 
              fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Число', fontsize=12, fontweight='bold')
ax2.set_ylabel('Количество', fontsize=12, fontweight='bold')
for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{count}', ha='center', va='bottom',
             fontsize=11, fontweight='bold')
plt.suptitle('Распределение 50 целых чисел от 1 до 5', 
             fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()

def f(x1, x2):
    return (x1 - 3)**2 + x2
x1 = np.linspace(0, 6, 100)
x2 = np.linspace(0, 6, 100)
X1, X2 = np.meshgrid(x1, x2)
Z = f(X1, X2)
constraint_mask = -2*X1 + 3*X2 >= 4
Z_constrained = np.where(constraint_mask, Z, np.nan)
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X1, X2, Z, alpha=0.3, cmap='viridis', 
                      label='Целевая функция')
surf_constrained = ax.plot_surface(X1, X2, Z_constrained, alpha=0.7, 
                                  color='red', label='Допустимая область')
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')
ax.set_zlabel('f(x₁, x₂)')
plt.tight_layout()
plt.show()

selected_styles = ['default', 'ggplot', 'dark_background', 'seaborn-v0_8']
def style_selector(style_name):
    plt.style.use(style_name)
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes[0, 0].plot(x_points, y_values, 'b-', linewidth=2, label='y = sin(ln(x))')
    axes[0, 0].set_title('График функции y = sin(ln(x))', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('y')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    axes[0, 0].set_facecolor('#f0f8ff')
    axes[0,1].scatter(x_points, y_values, 
            marker='D',          
            color=(0.2, 0.4, 0.6),  
            s=60,               
            alpha=0.8,           
            linewidth=0.5,      
            label='y = sin(ln(x))')
    axes[0, 1].set_title('Точечный график функции y = sin(ln(x))', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('y')
    axes[0, 1].grid(True, alpha=0.3)
    wedges, texts, autotexts = axes[1, 0].pie(counts,
                                    labels=[f'Число {x}' for x in unique],
                                    colors=colors,
                                    autopct='%1.1f%%',
                                    startangle=90,
                                    shadow=True)
    axes[1, 0].set_title('Круговая диаграмма частот чисел\n(50 чисел от 1 до 5)', 
                fontsize=14, fontweight='bold', pad=20)
    ax = fig.add_subplot(2, 2, 4, projection='3d')
    surf = ax.plot_surface(X1, X2, Z, alpha=0.3, cmap='viridis', 
                        label='Целевая функция')
    surf_constrained = ax.plot_surface(X1, X2, Z_constrained, alpha=0.7, 
                                    color='red', label='Допустимая область')
    ax.set_xlabel('x₁')
    ax.set_ylabel('x₂')
    ax.set_zlabel('f(x₁, x₂)')
    plt.show()
for style in selected_styles:
    style_selector(style)