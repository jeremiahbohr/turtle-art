
import turtle

def draw_pixel(x, y, color, pixel_size):
    """Draws a single pixel (a filled square) at the given coordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(pixel_size)
        turtle.right(90)
    turtle.end_fill()

def create_pixel_art(art_data, pixel_size=20):
    """Creates pixel art from a 2D list of color data."""
    start_x = -len(art_data[0]) * pixel_size / 2
    start_y = len(art_data) * pixel_size / 2
    
    turtle.speed(0)  # Set the drawing speed to the fastest
    turtle.hideturtle()
    turtle.bgcolor("black")

    for i, row in enumerate(art_data):
        for j, color_code in enumerate(row):
            if color_code != 0:  # 0 can represent a transparent or empty pixel
                x = start_x + j * pixel_size
                y = start_y - i * pixel_size
                # Simple color mapping, can be expanded
                if color_code == 1:
                    color = "darkgreen"
                elif color_code == 2:
                    color = "lightgreen"
                elif color_code == 3:
                    color = "brown"
                else:
                    color = "blue" # Default color for other numbers
                draw_pixel(x, y, color, pixel_size)

if __name__ == "__main__":
    # Example of a turtle shape
    # 0 = transparent, 1 = dark green, 2 = light green, 3 = brown
    turtle_data = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],  # Head
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0],  # Head
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],  # Neck
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Shell
        [0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0],  # Shell
        [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0],  # Shell
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # Base
        [0, 0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0],  # Legs
        [0, 0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0],  # Legs
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Tail
    ]

    screen = turtle.Screen()
    screen.title("Turtle Pixel Art")
    
    create_pixel_art(turtle_data)
    
    turtle.done()
