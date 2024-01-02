# %%
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(layout='wide')

# Updated plot function to highlight called numbers
def plot_bingo_board_with_highlights(board_numbers, called_numbers):
    fig, ax = plt.subplots(figsize=(10, 2))  # Aspect ratio is set to match the provided bingo board
    ax.set_aspect('equal')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.box(on=None)  # Turn off the box frame

    # Create the grid
    for x in range(6):
        ax.axhline(x, lw=2, color='black', zorder=5)
        ax.axvline(x, lw=2, color='black', zorder=5)

    # Fill in the numbers and circles
    for i, row in enumerate(board_numbers):
        for j, num in enumerate(row):
            y = 2 - i  # Invert the y axis to plot from top to bottom
            if num != "Free":
                # Check if the number has been called
                if num in called_numbers:
                    fill_color = 'red'
                    circle_edge_color = 'darkred'
                else:
                    fill_color = 'none'
                    circle_edge_color = 'grey'

                # Draw the number and circle
                circle = patches.Circle((j + 0.5, y + 0.5), 0.4, fill=True, facecolor=fill_color, edgecolor=circle_edge_color, lw=2, zorder=10)
                ax.add_patch(circle)
                ax.text(j + 0.5, y + 0.5, str(num), va='center', ha='center', zorder=10)

    # Set limits to match the provided image size
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 3)

    return fig


# Given the bingo board numbers from the image provided by the user
# Plade 139
bingo_board_numbers_139 = [
    [4, 32, 56, 75, 85],
    [26, 34, 44, 58, 77],
    [16, 29, 37, 59, 63]  # Assuming the middle cell is 'Free'
]

bingo_board_numbers_140 = [
    [24, 30, 45, 74, 81],
    [6, 27, 31, 48, 82],
    [10, 28, 54, 69, 76]  # Assuming the middle cell is 'Free'
]

# Initialize the list of called numbers
# called_numbers = [3, 89, 73, 4, 6, 33, 7, 9, 12, 23, 84, 31, 13, 15, 61, 16,
#                   18, 5, 17, 20, 24, 37, 21, 26, 80, 27, 1, 29, 52, 30, 10, 32,
#                   45, 14, 34, 25, 54, 2, 36, 22, 41, 38, 46, 78, 51, 47, 64,
#                   49, 53, 48, 76, 87, 65, 56, 35, 57, 69, 60, 42, 62, 77, 63,
#                   11, 39, 66, 43, 68, 40, 70, 59, 58, 74, 19, 71, 79]

# called_numbers = [21, 46, 73, 26, 49, 60, 38, 14, 25, 90, 9, 30, 89, 35, 88,
#                   79, 87, 11, 16, 28, 40, 27, 6, 75, 59, 78, 69, 47, 24, 67,
#                   50, 81, 83, 77, 51, 5, 29, 80, 56, 8, 64, 74, 12, 4, 65,
#                   57, 72, 54, 68, 3, 15, 71, 76, 82, 48, 20, 31, 22, 45, 84,
#                   86, 58, 42, 39, 62, 66, 2, 10, 70, 63, 23, 44, 18, 17, 13,
#                   7, 61, 36, 55, ]

called_numbers = [29, 67, 37, 16, 86, 23, 10, 34, 63, 55, 25, 75, 66, 24, 22,
                  79, 88, 14, 32, 82, 43, 17, 20, 52, 27, 35, 76, 83, 19, 12,
                  39, 70, 28, 60, 50, 89, 81, 4, 49, 68, 41, 53, 58, 13, 11,
                  51, 31, 15, 74, 33, 45, 5, 77, 30, 71, 54, 80, 42, 57, 3,
                  47, 9, 85, 1, 90, 48, 38, 21, 65, 36, 87, 46, 18, 7, 64, 6,
                  69, 44, 59, 2, 72, 8, ]

# Example usage: Add the numbers 26 and 75 as they are called
called_numbers.extend([])

# Plot the board with the called numbers highlighted
fig_139 = plot_bingo_board_with_highlights(bingo_board_numbers_139, called_numbers)
fig_140 = plot_bingo_board_with_highlights(bingo_board_numbers_140, called_numbers)

st.title("Bingo Bango Board")

col1, col2 = st.columns([1, 1])

# Plot the bingo board
with col1:
    st.header("Borad: 139")
    st.pyplot(fig_139)

with col2:
    st.header("Borad: 140")
    st.pyplot(fig_140)
