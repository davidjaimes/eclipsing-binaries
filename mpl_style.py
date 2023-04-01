def pro_plot(title, subtitle, caption, title_offset=0.0, caption_offset=0.0, fig=None, ax=None, plt=None):
    ax.yaxis.tick_right()
    ax.plot([0.12, .9], [1.07+title_offset, 1.07+title_offset],
        transform=fig.transFigure,
        clip_on=False, 
        color='w', 
        linewidth=.6)
    ax.add_patch(plt.Rectangle((0.12, 1.07+title_offset), 0.04, -0.02,
        transform=fig.transFigure, 
        clip_on=False))
    ax.text(x=0.12, y=.98+title_offset,
        s=rf"{title}",
        transform=fig.transFigure,
        ha='left',
        fontsize=14,
        color='w')
    ax.text(x=0.12, y=.92+title_offset,
        s=rf"{subtitle}",
        transform=fig.transFigure,
        ha='left',
        fontsize=12,
        color='C7')
    ax.text(x=0.12, y=-0.10+caption_offset,
        s=rf"{caption}Graphic by David Jaimes (www.davidjaimes.com)",
        transform=fig.transFigure,
        ha='left',
        va='bottom',
        fontsize=9,
        color='C7')

pro = {
    # Patches
    'patch.linewidth': 0.0,
    'patch.facecolor': 'w',

    # Lines
    'lines.linewidth': 2.5,
    'lines.color': 'deepskyblue',

    # Font
    'font.size': 18.0,

    # Axes
    'axes.facecolor': 'black',
    'axes.edgecolor': 'C7',
    'axes.linewidth': 0.3,
    'axes.grid': True,
    'axes.grid.axis': 'y',
    'axes.grid.which': 'major',
    'axes.labelcolor': 'C7',
    'axes.axisbelow': True,
    'axes.titlepad': 20.0,
    'axes.titlecolor': 'C7',
    'axes.titlelocation': 'left',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,

    # X-Ticks
    'xtick.labelsize': 12.0,
    'xtick.major.size': 5,
    'xtick.color': 'C7',

    # Y-Ticks
    'ytick.labelsize': 12.0,
    'ytick.major.size': 0.0,
    'ytick.color': 'C7',
    'ytick.major.pad': 2.0,

    # Grid
    'grid.color': 'C7',
    'grid.linestyle': 'solid',
    'grid.linewidth': 0.3,

    # Legend
    'legend.facecolor': 'whitesmoke',
    'legend.framealpha': 1.0,
    'legend.fontsize': 12.0,

    # Figure
    'figure.figsize': (8, 4),
    'figure.facecolor': 'black',

    # Errorbar Plots
    'errorbar.capsize': 3.0,

    # Other
    'savefig.dpi': 300,
    'savefig.transparent': True,
    'savefig.bbox': 'tight',
}