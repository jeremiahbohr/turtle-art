# Turtle Pixel Art

![Turtle Pixel Art Example](turtle.png)

This project uses Python's `turtle` library to generate pixel art drawings of a turtle based on user choices.

## Features

*   **Perspectives:** Choose between a "side" view and an "aerial" view of the turtle.
*   **Color Schemes:** Select from three different color palettes: "default", "ocean", and "desert".

## How to Run

1.  Ensure you have Python 3 installed.
2.  Run the script from your terminal:
    ```bash
    python turtle_pixel_art.py
    ```

A window will then open and draw the turtle pixel art according to your selections.

## How It Works

The script defines two main data structures:

1.  **Art Data:** A 2D list of integers (e.g., `side_view_turtle_data`) where each number corresponds to a color index.
2.  **Color Schemes:** A dictionary of color maps. Each map links the color indexes from the art data to specific color names.

## Key Functions

The script is built around a few core functions:

*   `create_pixel_art(art_data, color_map, pixel_size=20)`: This is the main drawing function.
    *   `art_data`: A 2D list representing the image to be drawn.
    *   `color_map`: A dictionary that maps the numbers in `art_data` to colors.
    *   `pixel_size`: An integer that defines the size in pixels for each square.

*   `draw_pixel(x, y, color, pixel_size)`: A helper function that draws a single colored square at a specific coordinate.
    *   `x`, `y`: The coordinates to start drawing the pixel.
    *   `color`: A string representing the fill color.
    *   `pixel_size`: The side length of the square to draw.

*   `get_user_choices()`: Prompts the user to input their preferred perspective and color scheme and validates the input.