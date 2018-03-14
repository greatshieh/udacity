'''
explore epsilon function
'''


import matplotlib.pyplot as plt
# import seaborn as sns

import numpy as np

t = np.linspace(1, 2001, 2000)

plt.figure()

for a in range(500, 2100, 100):
    s = 1 / (1 + 0.1 * np.exp(0.09 * (t - a)))
    label = 'a = {}'.format(a)
    plt.plot(t, s, label=label)

plt.legend(loc='upper right', ncol=3)


'''
for a in [0.1, 0.5, 0.9]:
    if a == 0.1:
        color = 'gold'
    elif a == 0.5:
        color = 'red'
    else:
        color = 'blue'
    for b in [0.009, 0.09]:
        if b == 0.009:
            linestyle = '--'
        else:
            linestyle = '-'
        for c in [500, 1000, 3000]:
            s = 1 / (1 + a * np.exp(b * (t - c)))
            # s = (1 - a*np.exp(-np.exp(-1.0*b*(t-c))))
            label = '{},{},{}'.format(a, b, c)
            linewidth = c / 500
            plt.plot(
                t,
                s,
                label=label,
                linewidth=linewidth,
                linestyle=linestyle,
                color=color)

plt.legend(loc='upper right', ncol=3)
'''
plt.grid()

plt.show()
