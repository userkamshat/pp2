import pygame
import math
import os
from datetime import datetime

# =====================================
# 1. INITIALIZATION
# =====================================

pygame.init()

WIDTH = 1100
HEIGHT = 720
TOOLBAR_HEIGHT = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Paint Application")

font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 15)

# The drawing area is a separate Surface
canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill((255, 255, 255))

# =====================================
# 2. COLORS AND SETTINGS
# =====================================

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
DARK_GRAY = (80, 80, 80)

current_color = BLACK
brush_size = 5
current_tool = "PENCIL"

# Colors available in the toolbar
palette = [
    BLACK,
    (255, 0, 0),
    (0, 150, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 120, 0),
    (150, 0, 150),
    WHITE
]

# =====================================
# 3. TOOLBAR
# =====================================

toolbar_items = []

# First row: drawing tools
tools = [
    "PENCIL", "LINE", "RECT", "CIRCLE",
    "ERASER", "PICK", "FILL", "TEXT"
]

for i, name in enumerate(tools):
    rect = pygame.Rect(10 + i * 105, 8, 100, 35)
    toolbar_items.append((rect, "tool", name))

# Second row: additional shapes
shapes = ["SQUARE", "RIGHT TRI", "EQUIL TRI", "RHOMBUS"]

for i, name in enumerate(shapes):
    rect = pygame.Rect(10 + i * 105, 50, 100, 30)
    toolbar_items.append((rect, "tool", name))

# Brush sizes
for i, size in enumerate([2, 5, 10]):
    rect = pygame.Rect(435 + i * 75, 50, 70, 30)
    toolbar_items.append((rect, "size", size))

# Color palette
for i, color in enumerate(palette):
    rect = pygame.Rect(670 + i * 48, 50, 35, 30)
    toolbar_items.append((rect, "color", color))


# =====================================
# 4. FLOOD FILL FUNCTION
# =====================================

def flood_fill(surface, start_x, start_y, new_color):
    """
    Changes all connected pixels of the same color.
    """

    width, height = surface.get_size()

    # Check that the starting point is inside the canvas
    if not (0 <= start_x < width and 0 <= start_y < height):
        return

    target_color = surface.get_at((start_x, start_y))[:3]

    # No need to fill if the color is already the same
    if target_color == new_color:
        return

    stack = [(start_x, start_y)]

    while stack:
        x, y = stack.pop()

        if not (0 <= x < width and 0 <= y < height):
            continue

        if surface.get_at((x, y))[:3] == target_color:

            surface.set_at((x, y), new_color)

            # Check four neighboring pixels
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))


# =====================================
# 5. DRAWING SHAPES
# =====================================

def draw_shape(surface, tool, start, end, color, size):

    x1, y1 = start
    x2, y2 = end

    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    if tool == "LINE":
        pygame.draw.line(surface, color, start, end, size)

    elif tool == "RECT":
        if width > 0 and height > 0:
            pygame.draw.rect(
                surface, color,
                (left, top, width, height), size
            )

    elif tool == "CIRCLE":
        radius = int(math.hypot(x2 - x1, y2 - y1))

        if radius > 0:
            pygame.draw.circle(surface, color, start, radius, size)

    elif tool == "SQUARE":
        side = min(width, height)

        if side > 0:
            square_width = side if x2 >= x1 else -side
            square_height = side if y2 >= y1 else -side

            square_x = x1 if square_width >= 0 else x1 - side
            square_y = y1 if square_height >= 0 else y1 - side

            pygame.draw.rect(
                surface, color,
                (square_x, square_y, side, side), size
            )

    elif tool == "RIGHT TRI":
        points = [
            (x1, y1),
            (x2, y1),
            (x2, y2)
        ]

        pygame.draw.polygon(surface, color, points, size)

    elif tool == "EQUIL TRI":
        points = [
            ((x1 + x2) // 2, top),
            (left, top + height),
            (left + width, top + height)
        ]

        pygame.draw.polygon(surface, color, points, size)

    elif tool == "RHOMBUS":
        points = [
            ((x1 + x2) // 2, top),
            (left + width, (y1 + y2) // 2),
            ((x1 + x2) // 2, top + height),
            (left, (y1 + y2) // 2)
        ]

        pygame.draw.polygon(surface, color, points, size)


# =====================================
# 6. SAVE FUNCTION
# =====================================

def save_canvas():
    if not os.path.exists("saved_images"):
        os.makedirs("saved_images")

    # Create a filename using the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"saved_images/painting_{timestamp}.png"

    pygame.image.save(canvas, filename)

    return filename


# =====================================
# 7. MAIN VARIABLES
# =====================================

running = True

drawing = False
start_pos = None
previous_pos = None

text_active = False
text_buffer = ""
text_position = None

status_message = "Choose a tool and start drawing!"


# =====================================
# 8. MAIN GAME LOOP
# =====================================

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # ---------------------------------
    # EVENTS
    # ---------------------------------

    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # ---------------------------------
        # KEYBOARD
        # ---------------------------------

        elif event.type == pygame.KEYDOWN:

            # Text tool keyboard input
            if text_active:

                if event.key == pygame.K_RETURN:

                    if text_buffer:
                        text_surface = font.render(
                            text_buffer, True, current_color
                        )

                        canvas.blit(text_surface, text_position)

                    text_active = False
                    text_buffer = ""

                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_buffer = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_buffer = text_buffer[:-1]

                else:
                    if event.unicode and event.unicode.isprintable():
                        text_buffer += event.unicode

            else:

                # Brush size shortcuts
                if event.key == pygame.K_1:
                    brush_size = 2

                elif event.key == pygame.K_2:
                    brush_size = 5

                elif event.key == pygame.K_3:
                    brush_size = 10

                # Save using Ctrl + S
                elif event.key == pygame.K_s and (
                    pygame.key.get_mods() & pygame.KMOD_CTRL
                ):
                    filename = save_canvas()
                    status_message = f"Saved: {filename}"

        # ---------------------------------
        # MOUSE CLICK
        # ---------------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = event.pos

            if event.button == 1:

                # Click on toolbar
                if mouse_y < TOOLBAR_HEIGHT:

                    for rect, item_type, value in toolbar_items:

                        if rect.collidepoint(event.pos):

                            if item_type == "tool":
                                current_tool = value
                                text_active = False
                                text_buffer = ""

                            elif item_type == "size":
                                brush_size = value

                            elif item_type == "color":
                                current_color = value

                            break

                # Click on canvas
                else:

                    canvas_pos = (
                        mouse_x,
                        mouse_y - TOOLBAR_HEIGHT
                    )

                    if current_tool == "TEXT":

                        text_active = True
                        text_buffer = ""
                        text_position = canvas_pos

                    elif current_tool == "FILL":

                        flood_fill(
                            canvas,
                            canvas_pos[0],
                            canvas_pos[1],
                            current_color
                        )

                    elif current_tool == "PICK":

                        current_color = canvas.get_at(canvas_pos)[:3]

                    else:

                        start_pos = canvas_pos
                        previous_pos = canvas_pos
                        drawing = True

                        # Pencil and eraser start immediately
                        if current_tool == "PENCIL":
                            pygame.draw.circle(
                                canvas, current_color,
                                canvas_pos, max(1, brush_size // 2)
                            )

                        elif current_tool == "ERASER":
                            pygame.draw.circle(
                                canvas, WHITE,
                                canvas_pos, max(1, brush_size // 2)
                            )

        # ---------------------------------
        # MOUSE MOVEMENT
        # ---------------------------------

        elif event.type == pygame.MOUSEMOTION:

            if drawing and event.buttons[0]:

                current_pos = (
                    event.pos[0],
                    event.pos[1] - TOOLBAR_HEIGHT
                )

                # Only draw if the mouse is inside the canvas
                if 0 <= current_pos[0] < WIDTH and 0 <= current_pos[1] < HEIGHT - TOOLBAR_HEIGHT:

                    if current_tool == "PENCIL":

                        pygame.draw.line(
                            canvas,
                            current_color,
                            previous_pos,
                            current_pos,
                            brush_size
                        )

                    elif current_tool == "ERASER":

                        pygame.draw.line(
                            canvas,
                            WHITE,
                            previous_pos,
                            current_pos,
                            brush_size
                        )

                    previous_pos = current_pos

        # ---------------------------------
        # MOUSE RELEASE
        # ---------------------------------

        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1 and drawing:

                end_pos = (
                    event.pos[0],
                    event.pos[1] - TOOLBAR_HEIGHT
                )

                if (
                    0 <= end_pos[0] < WIDTH
                    and 0 <= end_pos[1] < HEIGHT - TOOLBAR_HEIGHT
                ):

                    # Draw shapes permanently after releasing
                    if current_tool in [
                        "LINE", "RECT", "CIRCLE",
                        "SQUARE", "RIGHT TRI",
                        "EQUIL TRI", "RHOMBUS"
                    ]:

                        draw_shape(
                            canvas,
                            current_tool,
                            start_pos,
                            end_pos,
                            current_color,
                            brush_size
                        )

                drawing = False
                start_pos = None
                previous_pos = None

    # =================================
    # 9. DISPLAY
    # =================================

    screen.fill(WHITE)

    # Draw toolbar background
    pygame.draw.rect(
        screen, GRAY,
        (0, 0, WIDTH, TOOLBAR_HEIGHT)
    )

    # Draw toolbar buttons
    for rect, item_type, value in toolbar_items:

        if item_type == "tool":
            selected = current_tool == value

            button_color = (
                (170, 210, 255) if selected else WHITE
            )

            pygame.draw.rect(
                screen, button_color, rect, border_radius=5
            )

            label = small_font.render(
                value, True, BLACK
            )

            screen.blit(
                label,
                label.get_rect(center=rect.center)
            )

        elif item_type == "size":

            selected = brush_size == value

            button_color = (
                (170, 210, 255) if selected else WHITE
            )

            pygame.draw.rect(
                screen, button_color, rect, border_radius=5
            )

            label = small_font.render(
                str(value) + " px", True, BLACK
            )

            screen.blit(
                label,
                label.get_rect(center=rect.center)
            )

        elif item_type == "color":

            pygame.draw.rect(screen, value, rect)

            pygame.draw.rect(
                screen, BLACK, rect, 1
            )

    # Status information
    status = small_font.render(
        f"Tool: {current_tool} | Brush: {brush_size}px | {status_message}",
        True, BLACK
    )

    screen.blit(status, (10, 88))

    # Show permanent drawing
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    # ---------------------------------
    # PREVIEW FOR SHAPES
    # ---------------------------------

    if drawing and start_pos is not None:

        if current_tool in [
            "LINE", "RECT", "CIRCLE",
            "SQUARE", "RIGHT TRI",
            "EQUIL TRI", "RHOMBUS"
        ]:

            preview_canvas = canvas.copy()

            preview_end = (
                mouse_x,
                mouse_y - TOOLBAR_HEIGHT
            )

            if (
                0 <= preview_end[0] < WIDTH
                and 0 <= preview_end[1] < HEIGHT - TOOLBAR_HEIGHT
            ):

                draw_shape(
                    preview_canvas,
                    current_tool,
                    start_pos,
                    preview_end,
                    current_color,
                    brush_size
                )

                screen.blit(
                    preview_canvas,
                    (0, TOOLBAR_HEIGHT)
                )

    # ---------------------------------
    # TEXT PREVIEW
    # ---------------------------------

    if text_active and text_position is not None:

        text_surface = font.render(
            text_buffer + "|", True, current_color
        )

        screen.blit(
            text_surface,
            (
                text_position[0],
                text_position[1] + TOOLBAR_HEIGHT
            )
        )

    pygame.display.update()


# =====================================
# 10. CLOSE PYGAME
# =====================================

pygame.quit()