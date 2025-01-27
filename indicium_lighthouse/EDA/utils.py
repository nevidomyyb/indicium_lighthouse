import matplotlib.pyplot as plt
import numpy as np

def criar_tabela(ax, data, titulo):
    ax.axis('tight')
    ax.axis('off')
    
    table = ax.table(
        cellText=data.values,
        colLabels=data.columns,
        loc='center',
        cellLoc='center', 
        colColours=['#f5f5f5']*data.shape[1]
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    
    ax.set_title(titulo, fontsize=15)