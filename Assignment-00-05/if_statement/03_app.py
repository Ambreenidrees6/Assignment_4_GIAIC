from graphics import Canvas
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def create_grid(canvas):
    """Creates a grid of blue cells on the canvas."""
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

def create_eraser(canvas):
    """Creates the eraser at the mouse click position."""
    canvas.wait_for_click()
    last_click_x, last_click_y = canvas.get_last_click()

    eraser = canvas.create_rectangle(
        last_click_x,
        last_click_y,
        last_click_x + ERASER_SIZE,
        last_click_y + ERASER_SIZE,
        'pink'
    )
    return eraser

def erase_objects(canvas, eraser):
    """Erases (sets to white) objects touching the eraser."""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

def move_eraser(canvas, eraser):
    """Moves the eraser with the mouse and erases cells it touches."""
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)
        time.sleep(0.05)

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    create_grid(canvas)
    eraser = create_eraser(canvas)
    move_eraser(canvas, eraser)

if __name__ == '__main__':
    main()