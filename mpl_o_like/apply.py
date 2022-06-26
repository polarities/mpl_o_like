import matplotlib as mpl

"""
Famous plotting software like stylesheet for matplotlib.

References
- https://stackoverflow.com/questions/59222659/making-pythons-matplotlib-graphics-look-like-graphics-created-using-originpro
"""


def update(default_figsize_x_y):
    """
    TODO: Fig-size responsive stylesheet. mpl event connector maybe helpful?
    """
    mpl.rcParams.update({
        "figure.subplot.left": 0.177,
        "figure.subplot.right": 0.946,
        "figure.subplot.bottom": 0.156,
        "figure.subplot.top": 0.965,

        "xtick.major.size": 7,
        "xtick.minor.size": 3.5,
        "xtick.major.width": 1.1,
        "xtick.minor.width": 1.1,
        "xtick.major.pad": 5,
        "xtick.minor.visible": True,

        "ytick.major.size": 7,
        "ytick.minor.size": 3.5,
        "ytick.major.width": 1.1,
        "ytick.minor.width": 1.1,
        "ytick.major.pad": 5,
        "ytick.minor.visible": True,

        "lines.markersize": 10,
        "lines.markeredgewidth": 0.8,

        "axes.titlesize": 24,
        "axes.titlepad": 20,
        "axes.titleweight": "bold",

        "axes.labelsize": 20,
        "axes.labelweight": "bold",

        "axes.facecolor": 'white',
        'axes.xmargin': 0,
        'axes.ymargin': 0,
        'axes.linewidth': 1.1,
        'axes.labelpad': 5.0,
        'axes.formatter.useoffset': False,

        "xtick.labelsize": 17,
        "ytick.labelsize": 17,

        "font.family": 'sans-serif',
        "font.sans-serif": 'Arial',

        "figure.facecolor": 'white',
        "figure.edgecolor": 'white',
        "figure.figsize": [12, 6],

        "legend.fontsize": 17,


    })
