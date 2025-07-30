import matplotlib.pyplot as plt
import seaborn as sns
import random
import sys
from matplotlib import animation

# 🟦 Command-line arguments
number_of_frames = int(sys.argv[1])
rolls_per_frame = int(sys.argv[2])
actual_total = int(sys.argv[3])
display_total = int(sys.argv[4])
output_path = sys.argv[5]  # path to output video

# 🟦 Chart setup
sns.set_style('whitegrid')
fig = plt.figure(figsize=(8, 5))
values = list(range(1, 7))
frequencies = [0] * 6
all_rolls = [random.randint(1, 6) for _ in range(actual_total)]
index = [0]

# 🟦 Frame update function
def update(frame):
    rolls = all_rolls[index[0]:index[0] + rolls_per_frame]
    for roll in rolls:
        frequencies[roll - 1] += 1
    index[0] += rolls_per_frame

    plt.cla()
    ax = sns.barplot(x=values, y=frequencies, palette='bright')
    ax.set_title(f'{display_total:,} rolls')
    ax.set(xlabel='Dice Value', ylabel='Frequency')
    ax.set_ylim(top=max(frequencies) * 1.10)

    for bar, freq in zip(ax.patches, frequencies):
        percent = freq / sum(frequencies)
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{freq}\n{percent:.3%}',
            ha='center',
            va='bottom'
        )

# 🟦 Save the animation as an .mp4 video
anim = animation.FuncAnimation(
    fig,
    update,
    frames=number_of_frames,
    interval=100,
    repeat=False
)

anim.save(
    output_path,
    fps=10,
    writer='ffmpeg',
    extra_args=['-vcodec', 'libx264', '-pix_fmt', 'yuv420p']
)
