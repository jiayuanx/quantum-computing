from IPython.core.display import HTML, display
import random
import numpy as np
import math
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

def circle_notation(
    state, rows=None, side_spacing=0.2, top_spacing=0.1, bottom_spacing=0.8, 
    subplot_size=0.5, fontsize=12, labels=True,
    circle_color='lightblue', outline_color='black', line_color='blue'):
    assert state.ndim == 1
    n = len(state)
    if not rows:
        rows = math.ceil(math.sqrt(n))
    assert rows > 0
    cols = -((-n)//rows)
    
    swidth = cols*(2+side_spacing*2)
    sheight = rows*(2+bottom_spacing)+top_spacing
    width = subplot_size*swidth
    height = subplot_size*sheight
    fig = plt.figure(figsize=(width, height))
    plt.axis('off')
    ax = fig.axes[0]
    for j in range(rows):
        for k in range(cols):
            i = j*cols + k
            if i < n:
                value = state[i]
                radius = np.absolute(value)
                cx = (1+side_spacing)+(2+side_spacing*2)*k
                cy = (1+bottom_spacing)+(2+bottom_spacing)*(rows-j-1)
                x = np.imag(value)
                y = np.real(value)
                ax.add_patch(Circle((cx,cy), radius=radius, fill=True, ec='none', fc=circle_color))
                ax.add_line(Line2D((cx,cx+x), (cy,cy+y), c=line_color))
                ax.add_patch(Circle((cx,cy), radius=1, fill=False, ec=outline_color))
                if labels:
                    ax.text(cx,cy-1-(bottom_spacing/2), 
                            "$\\left | {} \\right \\rangle$".format(i),
                            va='center', ha='center', fontsize=fontsize)
    ax.set_xlim(0, swidth)
    ax.set_ylim(0, sheight)
    fig.tight_layout()
    plt.show()