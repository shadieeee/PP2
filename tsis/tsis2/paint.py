import pygame
import math
import datetime
from collections import deque



def flood_fill(surface, x, y, fill_color):
    target = surface.get_at((x, y))[:3]
    fill   = tuple(fill_color[:3])
    if target == fill:
        return
    w, h  = surface.get_size()
    seen  = set()
    queue = deque([(x, y)])
    seen.add((x, y))
    while queue:
        cx, cy = queue.popleft()
        surface.set_at((cx, cy), fill)
        for nx, ny in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen:
                if surface.get_at((nx, ny))[:3] == target:
                    seen.add((nx, ny))
                    queue.append((nx, ny))


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Drawing App")
    clock = pygame.time.Clock()

    canvas = pygame.Surface((1200, 600))
    canvas.fill((0, 0, 0))

    radius = 15          
    mode = 'blue'        
    points = []         
    history = []
    figures = []         
    drawing = True       
    drawing_mode = 1     
    fig_start = (0, 0)   
    BRUSH_SIZES = [2, 5, 10]   
    brush_idx   = 1            
    line_end = (0, 0)   

    
    text_active = False
    text_cursor = (0, 0)
    text_buf    = ""

    text = (
        "  Z = Draw rectangle\n"
        "  X = Draw circle\n"
        "  Q = Draw square\n"
        "  W = Draw right triangle\n"
        "  E = Draw equilateral triangle\n"
        "  R = Draw rhombus\n"
        "  L = Draw line (freehand)\n"
        "  N = Draw straight line\n"
        "  F = Flood fill\n"
        "  T = Text tool\n"
        "  C = Eraser\n"
        "  A = Clear\n"
        "  1/2/3 = Brush size\n"
        "  Ctrl+S = Save PNG"
    )

    r_btn = pygame.Rect(30, 320, 30, 30)
    g_btn = pygame.Rect(30, 370, 30, 30)
    b_btn = pygame.Rect(30, 420, 30, 30)

    # Modes that produce a "figure" (not a freehand stroke)
    FIGURE_MODES = (2, 3, 4, 5, 6, 7, 8)   # 8 = straight line


    while True:
        pressed = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        alt_held  = pressed[pygame.K_LALT]  or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                # while text tool is active, capture typing ---
                if text_active:
                    if event.key == pygame.K_RETURN:
                        tf = pygame.font.SysFont(None, 36)
                        color_map = {'red': (255,0,0), 'green': (0,255,0),
                                     'blue': (0,0,255), 'erase': (0,0,0)}
                        canvas.blit(tf.render(text_buf, True,
                                    color_map.get(mode, (255,255,255))), text_cursor)
                        text_active = False
                        text_buf    = ""
                    elif event.key == pygame.K_ESCAPE:
                        text_active = False
                        text_buf    = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text_buf = text_buf[:-1]
                    elif event.unicode and event.unicode.isprintable():
                        text_buf += event.unicode
                    continue   

                if (event.key == pygame.K_w and ctrl_held) \
                        or (event.key == pygame.K_F4 and alt_held) \
                        or event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_s and ctrl_held:
                    ts    = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    fname = f"canvas_{ts}.png"
                    pygame.image.save(canvas, fname)
                    print(f"Saved {fname}")
                    continue

                if event.key == pygame.K_1:
                    brush_idx = 0
                elif event.key == pygame.K_2:
                    brush_idx = 1
                elif event.key == pygame.K_3:
                    brush_idx = 2

                
                elif event.key == pygame.K_l:
                    drawing_mode = 1   # freehand line

                elif event.key == pygame.K_z:
                    drawing_mode = 2   # rectangle

                elif event.key == pygame.K_x:
                    drawing_mode = 3   # circle

                elif event.key == pygame.K_q:
                    drawing_mode = 4   # square

                elif event.key == pygame.K_w:
                    drawing_mode = 5   # right triangle

                elif event.key == pygame.K_e:
                    drawing_mode = 6   # equilateral triangle

                elif event.key == pygame.K_r:
                    drawing_mode = 7   # rhombus

                # --- ADDED new tools ---
                elif event.key == pygame.K_n:
                    drawing_mode = 8   # straight line

                elif event.key == pygame.K_f:
                    drawing_mode = 9   # flood fill

                elif event.key == pygame.K_t:
                    drawing_mode = 10  # text

                elif event.key == pygame.K_c:
                    mode = 'erase'
                    points = []

                elif event.key == pygame.K_a:
                    
                    history = []
                    points  = []
                    figures = []
                    canvas.fill((0, 0, 0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   
                    if drawing_mode in FIGURE_MODES:
                        fig_start = mouse_pos

                    if drawing_mode == 1:
                        points = [mouse_pos]

                    radius = BRUSH_SIZES[brush_idx]   
                    if drawing_mode == 9:
                        color_map = {'red': (255,0,0), 'green': (0,255,0),
                                     'blue': (0,0,255), 'erase': (0,0,0)}
                        flood_fill(canvas, mouse_pos[0], mouse_pos[1],
                                   color_map.get(mode, (0, 0, 255)))

                    elif drawing_mode == 10:
                        text_active = True
                        text_cursor = mouse_pos
                        text_buf    = ""

                elif event.button == 3:             
                    radius = max(1, radius - 1)

                if r_btn.collidepoint(mouse_pos):
                    mode = 'red'
                    points = []
                elif g_btn.collidepoint(mouse_pos):
                    mode = 'green'
                    points = []
                elif b_btn.collidepoint(mouse_pos):
                    mode = 'blue'
                    points = []
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if drawing_mode == 1 and points:
                        # Bake the freehand stroke onto canvas
                        for i in range(len(points) - 1):
                            drawLineBetween(canvas, i, points[i], points[i + 1], radius, mode)
                        points = []
                    elif drawing_mode in FIGURE_MODES and figures:
                        # Bake the finished shape onto canvas
                        s, e = figures[0]
                        drawfig(canvas, 0, s, e, radius, mode, drawing_mode)
                        figures = []

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:   # left button held
                    if drawing_mode == 1:
                        if points:
                            drawLineBetween(canvas, len(points), points[-1], event.pos, radius, mode)
                        points = (points + [event.pos])[-256:]
                    elif drawing_mode in FIGURE_MODES:
                        figures = [(fig_start, mouse_pos)]


        screen.blit(canvas, (0, 0))

        if drawing:
            if drawing_mode == 1:
                for i in range(len(points) - 1):
                    drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            elif drawing_mode in FIGURE_MODES and figures:
                s, e = figures[0]
                drawfig(screen, 0, s, e, radius, mode, drawing_mode)

        font = pygame.font.SysFont(None, 24)
        for line_idx, line in enumerate(text.splitlines()):
            rendered = font.render(line, True, (255, 255, 255))
            screen.blit(rendered, (0, line_idx * 20))

        # show active brush size ---
        brush_lbl = font.render(f"  Brush: {BRUSH_SIZES[brush_idx]}px", True, (255, 220, 80))
        screen.blit(brush_lbl, (0, len(text.splitlines()) * 20 + 4))

        # live text preview while typing ---
        if text_active:
            tf      = pygame.font.SysFont(None, 36)
            preview = tf.render(text_buf + "|", True, (200, 200, 255))
            screen.blit(preview, text_cursor)

        pygame.draw.rect(screen, (0, 0, 255), b_btn)
        pygame.draw.rect(screen, (255, 0, 0), r_btn)
        pygame.draw.rect(screen, (0, 255, 0), g_btn)

        pygame.display.flip()
        clock.tick(60)



def drawfig(screen, index, start, end, width, color_mode, draw_mode):
    
    x1, y1 = start
    x2, y2 = end

    diag = math.hypot(x2 - x1, y2 - y1)
    r_val = int(diag / 2)
    c1 = max(0, min(255, r_val - 256))
    c2 = max(0, min(255, r_val))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:  # 'erase'
        color = (0, 0, 0)

    # ---- Rectangle ----
    if draw_mode == 2:
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(screen, color, rect, width)

    # ---- Circle 
    elif draw_mode == 3:
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        radius = max(1, int(math.hypot(x2 - x1, y2 - y1) / 2))
        pygame.draw.circle(screen, color, (cx, cy), radius, width)

    elif draw_mode == 4:
        side = min(abs(x2 - x1), abs(y2 - y1))
        # Preserve the sign of the drag so the square follows the mouse
        sx = x1 + (side if x2 >= x1 else -side)
        sy = y1 + (side if y2 >= y1 else -side)
        rect = pygame.Rect(min(x1, sx), min(y1, sy), side, side)
        pygame.draw.rect(screen, color, rect, width)

    elif draw_mode == 5:
        pts = [(x1, y2), (x1, y1), (x2, y2)]
        pygame.draw.polygon(screen, color, pts, width)

    elif draw_mode == 6:
        base_len = abs(x2 - x1)
        apex_x   = (x1 + x2) / 2
        # Height of an equilateral triangle
        height   = (math.sqrt(3) / 2) * base_len
        apex_y   = y2 - height if y1 <= y2 else y2 + height
        pts = [(x1, y2), (x2, y2), (apex_x, apex_y)]
        pygame.draw.polygon(screen, color, pts, width)

    elif draw_mode == 7:
        # Four vertices at the midpoints of the bounding box edges:
        #   top-mid, right-mid, bottom-mid, left-mid
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        pts = [
            (mid_x, y1),   # top
            (x2,   mid_y), # right
            (mid_x, y2),   # bottom
            (x1,   mid_y), # left
        ]
        pygame.draw.polygon(screen, color, pts, width)

    #  Straight line 
    elif draw_mode == 8:
        pygame.draw.line(screen, color, start, end, max(1, width * 2))



def drawLineBetween(screen, index, start, end, width, color_mode):

    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:  # 'erase'
        color = (0, 0, 0)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress  = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()