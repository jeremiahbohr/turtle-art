
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

def create_pixel_art(art_data, color_map, pixel_size=20):
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
                color = color_map.get(color_code, "blue") # Use color_map, default to blue
                draw_pixel(x, y, color, pixel_size)

def check_symmetry(data):
    """Checks if the 2D data array is symmetrical along its vertical axis."""
    for row in data:
        # Filter out transparent pixels (0) for symmetry check if they are just padding
        # For perfect symmetry, we need to check the actual pixel data.
        # Assuming 0s are part of the symmetry if they are within the bounds of the turtle.
        # For now, a simple row reversal check.
        if len(row) % 2 != 0: # Odd number of columns, middle column is its own mirror
            left_half = row[:len(row)//2]
            right_half = row[len(row)//2 + 1:]
        else:
            left_half = row[:len(row)//2]
            right_half = row[len(row)//2:]
        
        if left_half != right_half[::-1]:
            return False
    return True

if __name__ == "__main__":
    # 0 = transparent

    # Side view turtle data
    side_view_turtle_data = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],  # Head
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0],  # Head
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],  # Neck
        [0, 0, 0, 1, 3, 1, 1, 3, 1, 1, 0, 0, 0, 0, 0, 0],  # Shell (with brown accents)
        [0, 0, 1, 2, 3, 2, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0],  # Shell (with brown accents)
        [0, 1, 2, 3, 2, 2, 2, 2, 3, 2, 1, 0, 0, 0, 0, 0],  # Shell (with brown accents)
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],  # Base (with brown accents, shortened)
        [0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],  # Legs (light green)
        [0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],  # Legs (light green)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Tail (removed/transparent)
    ]

    # Aerial view turtle data
    aerial_view_turtle_data = [
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],  # Head (outlined)
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Neck (wider)
        [0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0],  # Top of shell
        [0, 0, 2, 2, 1, 1, 1, 3, 3, 1, 1, 1, 2, 2, 0, 0],  # Front Legs and Shell
        [0, 0, 2, 2, 1, 1, 1, 3, 3, 1, 1, 1, 2, 2, 0, 0],  # Shell
        [0, 0, 0, 0, 1, 1, 3, 1, 1, 3, 1, 1, 0, 0, 0, 0],  # Shell (middle
        [0, 0, 0, 0, 1, 1, 3, 1, 1, 3, 1, 1, 0, 0, 0, 0],  # Shell (middle)
        [0, 0, 2, 2, 1, 1, 1, 3, 3, 1, 1, 1, 2, 2, 0, 0],  # Shell
        [0, 0, 2, 2, 1, 1, 1, 3, 3, 1, 1, 1, 2, 2, 0, 0],  # Back Legs and Shell
        [0, 0, 0, 0, 0, 1, 3, 1, 1, 3, 1, 0, 0, 0, 0, 0],  # Bottom of shell
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Rounded bottom
        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],  # More rounded bottom
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Empty row for spacing
    ]

    print(f"Aerial view data symmetry: {check_symmetry(aerial_view_turtle_data)}")

    # Color schemes
    color_schemes = {
        "default": {
            1: "darkgreen",
            2: "lightgreen",
            3: "brown"
        },
        "ocean": {
            1: "darkblue",
            2: "lightblue",
            3: "gray"
        },
        "desert": {
            1: "orange",
            2: "yellow",
            3: "saddlebrown"
        }
    }

    def get_user_choices(default_perspective=None, default_scheme=None):
        if default_perspective and default_scheme:
            return default_perspective, default_scheme

        perspective = ""
        while perspective not in ["side", "aerial"]:
            perspective = input("Enter perspective (side or aerial): ").lower()
            if perspective not in ["side", "aerial"]:
                print("Invalid perspective. Please choose 'side' or 'aerial'.")

        scheme = ""
        while scheme not in color_schemes:
            scheme = input(f"Enter color scheme ({', '.join(color_schemes.keys())}): ").lower()
            if scheme not in color_schemes:
                print(f"Invalid color scheme. Please choose from {', '.join(color_schemes.keys())}.")
        return perspective, scheme

    perspective_choice, color_scheme_choice = get_user_choices()

    screen = turtle.Screen()
    screen.title("Turtle Pixel Art")

    if perspective_choice == "side":
        selected_art_data = side_view_turtle_data
    else:
        selected_art_data = aerial_view_turtle_data
    
    selected_color_map = color_schemes[color_scheme_choice]
    
    create_pixel_art(selected_art_data, selected_color_map)
    
    turtle.done()
