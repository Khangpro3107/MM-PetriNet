from pygame import init, time, font, display, Rect, Color, draw, event, KEYDOWN, KEYUP, QUIT, K_SPACE,\
    K_s, K_c, K_e, K_u, K_r, K_f, K_UP, K_DOWN, K_BACKSPACE, K_ESCAPE, MOUSEBUTTONDOWN
from pygame.font import SysFont

# Initialize package
init()
font.init()
screen = display.set_mode((800, 600))
display.set_caption("Petri Net")

# Configuration for the package
font = SysFont('Calibri', 24, True)             # Fonts
title_font = SysFont('Segoe UI', 36, True)
choice_font = SysFont('Segoe UI', 24, True)
small_font = SysFont('Consolas', 16, True)
tiny_font = SysFont('Consolas', 12, True)
color_black = (0, 0, 0)                         # Colors
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_yellow = (255, 255, 0)
background_main = (24, 239, 242)
place_radius = 25                               # Radius of places, transitions
transition_width = 40
line_width = 2


def print_text(msg: str, color, posX: int, posY: int, _font, _antialias=True):
    # Draw the text at position posX, posY
    text = _font.render(msg, _antialias, color)
    screen.blit(text, (posX, posY))


def print_text_box(msg: str, posX: int, posY: int, _color, _font, _antialias=True, _background=None) -> None:
    # Draw the text box at position posX, posY
    text = _font.render(msg, _antialias, _color, _background)
    text_rect = text.get_rect()
    text_rect.center = (posX, posY)
    screen.blit(text, text_rect)


def draw_choice_box(text_color, background_color, choice_text, posY, posX=400) -> None:
    # Draw a choice box at the menu
    print_text_box(choice_text, posX, posY, text_color,
                   choice_font, True, background_color)


def user_choice(current_pos: int) -> None:
    # Draw choice boxes and texts at the menu
    print_text_box("Petri Net Modeling", 400, 70,
                   color_black, title_font, True)
    draw_choice_box(color_red, color_green, '  Simulate Item 1  ',
                    150, max(current_pos, 400))
    draw_choice_box(color_red, color_green, '  Simulate Item 2  ',
                    210, max(current_pos + 25, 400))
    draw_choice_box(color_red, color_green, '  Simulate Item 3  ',
                    270, max(current_pos + 50, 400))
    draw_choice_box(color_red, color_green, '  Simulate Item 4  ',
                    330, max(current_pos + 75, 400))
    print_text_box('Choose: UP & DOWN  Confirm: Spacebar',
                   400, 560, color_black, tiny_font)


def show_menu():
    # The loop runs the menu & user choice
    item_index = -1
    run = True
    flag_continue = False
    current_pos = 900
    speed = 0.75            # The speed of the moving text box at the start
    while run:
        current_pos -= speed
        screen.fill(background_main)
        user_choice(current_pos)
        if item_index == 0:             # If a specific text box is chosen then change its color
            draw_choice_box(color_black, color_yellow,
                            '  Simulate Item 1  ', 150)
            print_text_box('Simulate the Petri Net of Item 1: Patient Network',
                           400, 500, color_black, tiny_font)
        elif item_index == 1:
            draw_choice_box(color_black, color_yellow,
                            '  Simulate Item 2  ', 210)
            print_text_box('Simulate the Petri Net of Item 2: Specialist Network',
                           400, 500, color_black, tiny_font)
        elif item_index == 2:
            draw_choice_box(color_black, color_yellow,
                            '  Simulate Item 3  ', 270)
            print_text_box('Simulate the Petri Net of Item 3: Superimposed Network',
                           400, 500, color_black, tiny_font)
        elif item_index == 3:
            draw_choice_box(color_black, color_yellow,
                            '  Simulate Item 4  ', 330)
            print_text_box('Simulate the Petri Net of Item 4: Reachable Marking',
                           400, 500, color_black, tiny_font)
        for _event in event.get():
            if _event.type == QUIT:
                run = False
            elif _event.type == KEYDOWN:
                if current_pos <= 400:
                    if _event.key == K_DOWN:
                        if item_index == 3:
                            item_index = 0
                        else:
                            item_index += 1
                    if _event.key == K_UP:
                        if item_index == 0:
                            item_index = 3
                        elif item_index >= 0:
                            item_index -= 1
                if _event.key == K_SPACE:
                    if item_index == -1:
                        continue
                    run = False
                    flag_continue = True
            elif _event.type == KEYUP:
                pass
        display.update()
    return item_index, flag_continue


def input_promt1():
    # Handling user input for item 1
    user_input = ["", "", ""]                           # Storing user inputs
    # Boolean variables to keep the game running
    flag_continue = False
    showing_menu = False
    # Draw the text boxes in which the user will enter inputs
    input_rect = [Rect(200, 200, 80, 24), Rect(
        400, 200, 80, 24), Rect(600, 200, 80, 24)]
    # Color changes if a text box is being selected
    color_active = Color(color_yellow)
    color_passive = Color(color_white)
    color = [color_passive, color_passive, color_passive]
    # Active status of the three text boxes
    active = [False, False, False]
    running = True
    while running:
        for _event in event.get():
            if _event.type == QUIT:
                running = False
            if _event.type == MOUSEBUTTONDOWN:                  # Mouse click
                for i in range(3):
                    # If mouse click is inside a text box -> Make it active and change color
                    if input_rect[i].collidepoint(_event.pos):
                        active[i] = True
                        color[i] = color_active
                    else:
                        # If mouse click is outside a text box -> Make it not active and change color
                        active[i] = False
                        color[i] = color_passive
            if _event.type == KEYDOWN:                          # Key press down
                # One iteration for each text box
                for i in range(3):
                    if active[i]:
                        if _event.key == K_BACKSPACE:           # 'Backspace' is pressed -> Delete user input on the left by 1 character
                            user_input[i] = user_input[i][:-1]
                        else:
                            temp = _event.unicode               # If it is not 'Backspace'
                            # Only accept number keys
                            if not (len(user_input[i]) == 0 and temp == '0') and (temp <= '9' and temp >= '0'):
                                if len(user_input[i]) >= 1:
                                    # Make the input smaller or equal to 10
                                    user_input[i] = '10'
                                else:
                                    # Enter the number the user typed to the box
                                    user_input[i] += temp
                # 'Spacebar' is pressed -> Confirm user input and go to the net screen
                if _event.key == K_SPACE:
                    flag_continue = True
                    running = False
                    showing_menu = False
                if _event.key == K_ESCAPE:                      # 'Esc' is pressed -> Go back to the previous screen
                    running = False
                    showing_menu = True
                    flag_continue = True
            if _event.type == KEYUP:
                pass
        # Draw needed stuff
        screen.fill(background_main)
        print_text('wait', color_black, 150, 200, font)
        print_text('inside', color_black, 335, 200, font)
        print_text('done', color_black, 550, 200, font)
        print_text_box('Enter the initial number of tokens in each place',
                       400, 110, color_black, font)
        print_text_box('Item 1: Patient Network', 400,
                       50, color_black, title_font)
        print_text_box('Delete: Backspace  Confirm: Spacebar  Back: Esc',
                       400, 545, color_black, tiny_font)
        print_text_box('Click on a box to enter the required number',
                       400, 560, color_black, tiny_font)
        print_text_box('Note: You can only enter numbers. If a box is empty, a default value of 0 will be entered.',
                       400, 590, color_black, tiny_font)
        print_text_box('The maximum number of tokens a place can receive as input is 10',
                       400, 575, color_black, tiny_font)
        for i in range(3):
            text_surface = font.render(user_input[i], True, color_black)
            draw.rect(screen, color[i], input_rect[i])
            screen.blit(
                text_surface, (input_rect[i].x, input_rect[i].y))
        display.update()
    for i in range(3):
        if len(user_input[i]):
            user_input[i] = int(user_input[i])
        else:
            user_input[i] = 0
    return user_input, flag_continue, showing_menu


def input_promt2():
    # Handling user input for item 2
    user_input = ["", "", ""]
    flag_continue = False
    showing_menu = False
    input_rect = [Rect(200, 200, 80, 24), Rect(
        400, 200, 80, 24), Rect(600, 200, 80, 24)]
    color_active = Color(color_yellow)
    color_passive = Color(color_white)
    color = [color_passive, color_passive, color_passive]
    active = [False, False, False]
    running = True
    while running:
        for _event in event.get():
            if _event.type == QUIT:
                running = False
            if _event.type == MOUSEBUTTONDOWN:
                for i in range(3):
                    if input_rect[i].collidepoint(_event.pos):
                        active[i] = True
                        color[i] = color_active
                    else:
                        active[i] = False
                        color[i] = color_passive
            if _event.type == KEYDOWN:
                for i in range(3):
                    if active[i]:
                        if _event.key == K_BACKSPACE:
                            user_input[i] = user_input[i][:-1]
                        else:
                            temp = _event.unicode
                            if not (len(user_input[i]) == 0 and temp == '0') and (temp <= '9' and temp >= '0'):
                                if len(user_input[i]) >= 1:
                                    user_input[i] = '10'
                                else:
                                    user_input[i] += temp
                if _event.key == K_SPACE:
                    flag_continue = True
                    running = False
                if _event.key == K_ESCAPE:
                    running = False
                    showing_menu = True
                    flag_continue = True
            if _event.type == KEYUP:
                pass
        screen.fill(background_main)
        print_text('free', color_black, 150, 200, font)
        print_text('busy', color_black, 350, 200, font)
        print_text('docu', color_black, 550, 200, font)
        print_text_box('Enter the initial number of tokens in each place',
                       400, 110, color_black, font)
        print_text_box('Item 2: Specialist Network',
                       400, 50, color_black, title_font)
        print_text_box('Delete: Backspace  Confirm: Spacebar  Back: Esc',
                       400, 545, color_black, tiny_font)
        print_text_box('Click on a box to enter the required number',
                       400, 560, color_black, tiny_font)
        print_text_box('Note: You can only enter numbers. If a box is empty, a default value of 0 will be entered.',
                       400, 590, color_black, tiny_font)
        print_text_box('The maximum number of tokens a place can receive as input is 10',
                       400, 575, color_black, tiny_font)
        for i in range(3):
            text_surface = font.render(user_input[i], True, color_black)
            draw.rect(screen, color[i], input_rect[i])
            screen.blit(
                text_surface, (input_rect[i].x, input_rect[i].y))
        display.update()
    for i in range(3):
        if len(user_input[i]):
            user_input[i] = int(user_input[i])
        else:
            user_input[i] = 0
    return user_input, flag_continue, showing_menu


def input_promt3():
    # Handling user input for item 3 (and 4)
    user_input = ["", "", "", "", "", ""]
    flag_continue = False
    showing_menu = False
    input_rect = [Rect(200, 200, 80, 24), Rect(
        400, 200, 80, 24), Rect(600, 200, 80, 24), Rect(200, 400, 80, 24), Rect(400, 400, 80, 24), Rect(600, 400, 80, 24)]
    color_active = Color(color_yellow)
    color_passive = Color(color_white)
    color = [color_passive, color_passive, color_passive,
             color_passive, color_passive, color_passive]
    active = [False, False, False, False, False, False]
    running = True
    while running:
        for _event in event.get():
            if _event.type == QUIT:
                running = False
            if _event.type == MOUSEBUTTONDOWN:
                for i in range(6):
                    if input_rect[i].collidepoint(_event.pos):
                        active[i] = True
                        color[i] = color_active
                    else:
                        active[i] = False
                        color[i] = color_passive
            if _event.type == KEYDOWN:
                for i in range(6):
                    if active[i]:
                        if _event.key == K_BACKSPACE:
                            user_input[i] = user_input[i][:-1]
                        else:
                            temp = _event.unicode
                            if not (len(user_input[i]) == 0 and temp == '0') and (temp <= '9' and temp >= '0'):
                                if len(user_input[i]) >= 1:
                                    user_input[i] = '10'
                                else:
                                    user_input[i] += temp
                if _event.key == K_SPACE:
                    flag_continue = True
                    running = False
                if _event.key == K_ESCAPE:
                    running = False
                    showing_menu = True
                    flag_continue = True
            if _event.type == KEYUP:
                pass
        screen.fill(background_main)
        print_text('free', color_black, 150, 200, font)
        print_text('busy', color_black, 335, 200, font)
        print_text('docu', color_black, 550, 200, font)
        print_text('wait', color_black, 150, 400, font)
        print_text('inside', color_black, 335, 400, font)
        print_text('done', color_black, 550, 400, font)
        print_text_box('Enter the initial number of tokens in each place',
                       400, 110, color_black, font)
        print_text_box('Item 3: Superimposed Network',
                       400, 50, color_black, title_font)
        print_text_box('Delete: Backspace  Confirm: Spacebar  Back: Esc',
                       400, 545, color_black, tiny_font)
        print_text_box('Click on a box to enter the required number',
                       400, 560, color_black, tiny_font)
        print_text_box('Note: You can only enter numbers. If a box is empty, a default value of 0 will be entered.',
                       400, 590, color_black, tiny_font)
        print_text_box('The maximum number of tokens a place can receive as input is 10',
                       400, 575, color_black, tiny_font)
        for i in range(6):
            text_surface = font.render(user_input[i], True, color_black)
            draw.rect(screen, color[i], input_rect[i])
            screen.blit(
                text_surface, (input_rect[i].x, input_rect[i].y))
        display.update()
    for i in range(6):
        if len(user_input[i]):
            user_input[i] = int(user_input[i])
        else:
            user_input[i] = 0
    return user_input, flag_continue, showing_menu


def draw_arrow(start_pos, end_pos, other_pos1, other_pos2, color=color_black) -> None:
    # Draw an arrow on the game window
    draw.line(screen, color, start_pos, end_pos, line_width)
    draw.line(screen, color, other_pos1, end_pos, line_width)
    draw.line(screen, color, other_pos2, end_pos, line_width)


class Node:
    # The parent class for class 'Transition'
    def __init__(self, name: str) -> None:
        self.name = name            # The label of the node
        self.in_edges = []           # List of edges pointing to this node
        self.out_edges = []          # List of edges pointing away from this node
        self.posX = -1              # posX and posY for drawing this node on the game window
        self.posY = -1
        # Decides whether to put the label above or below its node on the game window
        self.label_position = 'D'


class Edge:
    # Represents a directed edge in a Petri Net
    def __init__(self, src, dst) -> None:
        self.src = src                  # The source node of this edge
        self.dst = dst                  # The destination of this edge
        # Constructor automatically links src and dst using this node
        src.out_edges.append(self)
        dst.in_edges.append(self)

    def draw(self, start_pos: int, end_pos: int, edge_pos1: int, edge_pos2: int, color=color_black) -> None:
        # Draw this edge on the game window
        draw_arrow(start_pos, end_pos, edge_pos1, edge_pos2, color)


class Place:
    # Represents a place in a Petri Net
    def __init__(self, num_tokens: int, name: str) -> None:
        self.holding = num_tokens       # Number of tokens of this place
        self.name = name                # This place's label
        self.in_edges = []              # List of edges pointing to this place
        self.out_edges = []             # List of edges pointing away from this place

    def show_tokens(self, posX: int, posY: int, color=color_black) -> None:
        # Print this place's number of tokens on the game window
        print_text_box(str(self.holding), posX, posY, color, font)

    def draw(self, posX: int, posY: int, color=color_black, position='D') -> None:
        # Draw this place on the game window
        draw.circle(screen, color, (posX, posY), place_radius, line_width)
        # If position is 'D' (down), put the place's label below it
        if position == 'D':
            print_text_box(self.name, posX, posY +
                           place_radius + 10, color, font)
        else:
            print_text_box(self.name, posX, posY -
                           place_radius - 12, color, font)
        self.show_tokens(posX, posY + 3, color)


class Transition(Node):
    # Represents a transition in a Petri Net
    def is_enabled(self) -> bool:
        # Return true if this transition is enabled i.e. all of the places
        # pointing to this transition has at least 1 token
        for in_edge in self.in_edges:
            if in_edge.src.holding < 1:
                return False
        return True

    def fire(self) -> None:
        # Fire this transtion if it is enabled. Each place pointing to this transitions
        # gives away 1 token. Each place pointed to by this transitions
        # receives 1 token.
        if self.is_enabled():
            for in_edge in self.in_edges:
                in_edge.src.holding -= 1
            for out_edge in self.out_edges:
                out_edge.dst.holding += 1

    def undo_fire(self) -> None:
        # The opposite of the fire method
        for in_edge in self.in_edges:
            in_edge.src.holding += 1
        for out_edge in self.out_edges:
            out_edge.dst.holding -= 1

    def draw(self, posX: int, posY: int, color=color_black, label_position='D') -> None:
        # Draw this transition on the game window
        self.posX = posX
        self.posY = posY
        self.label_position = label_position
        draw.rect(screen, color, Rect(
            posX, posY, transition_width, transition_width), line_width)
        if label_position == 'D':
            print_text_box(self.name, posX + 20, posY +
                           transition_width + 15, color, font)
        else:
            print_text_box(self.name, posX + 20, posY - 15, color, font)


class PetriNet:
    # Represents a Petri Net
    def __init__(self) -> None:
        self.transitions = []       # The list of transitions in this Petri Net
        self.places = []            # The list of places in this Petri Net

    def add_transitions(self, *args) -> None:
        # Add a transition to this Petri Net
        for arg in args:
            self.transitions.append(arg)

    def add_places(self, *args) -> None:
        # Add a place to this Petri Net
        for arg in args:
            self.places.append(arg)

    def show_marking(self, color=color_black) -> None:
        # Print the current marking on the game window
        printing_str = "Current marking: ["
        i = 0
        places_length = len(self.places)
        for place in self.places:
            if i == places_length - 1:
                printing_str = printing_str + \
                    str(place.holding) + "." + place.name + "]"
            else:
                printing_str = printing_str + \
                    str(place.holding) + "." + place.name + ","
            i += 1
        print_text_box(printing_str, 400, 500, color, font)

    def terminate(self, color=color_black) -> bool:
        # Return true if this Petri Net is terminated i.e. all of its transitions are not enabled
        for transition in self.transitions:
            if transition.is_enabled():
                return False
        print_text_box("This Petri Net has reached its terminal marking!",
                       400, 540, color, font)
        return True

    def reset(self):
        # Reset this Petri Net
        self.transitions = []
        self.places = []


def print_firing_sequence(firing_sequence: list) -> None:
    # Print the firing sequence so far
    print("Firing sequence so far: ", end="")
    for i in range(len(firing_sequence)):
        print(firing_sequence[i].name, end='')
        if i != len(firing_sequence) - 1:
            print(',', end='')
    print("")


def make_edges(*args) -> list:
    # Links a place and a transition together and return a list of edges
    res = []
    for i in range(len(args) // 2):
        new_edge = Edge(args[2 * i], args[2 * i + 1])
        res.append(new_edge)
    return res


def draw_item1(color=color_black) -> None:
    # Draw stuff for item 1
    draw_arrow((75, 300), (200, 300), (195, 295), (195, 305))
    draw_arrow((240, 300), (375, 300), (370, 295), (370, 305))
    draw_arrow((425, 300), (570, 300), (565, 295), (565, 305))
    draw_arrow((610, 300), (725, 300), (720, 295), (720, 305))
    print_text_box("Start: S  Change: C  Undo: U  Back: Esc  Reset: R  Print firing sequence: F",
                   400, 570, color, tiny_font)
    print_text_box('Item 1: Patient Network', 400, 50, color_black, title_font)


def draw_item2(color=color_black) -> None:
    # Draw stuff for item 2
    draw_arrow((200, 225), (200, 380), (195, 375), (205, 375))
    draw_arrow((600, 380), (600, 225), (595, 230), (605, 230))
    draw_arrow((220, 400), (375, 400), (370, 395), (370, 405))
    draw_arrow((423, 400), (580, 400), (575, 395), (575, 405))
    draw_arrow((380, 200), (225, 200), (230, 205), (230, 195))
    draw_arrow((575, 200), (420, 200), (425, 205), (425, 195))
    print_text_box("Start: S  Change: C  End: E  Undo: U  Back: Esc  Reset: R  Print firing sequence: F",
                   400, 570, color, tiny_font)
    print_text_box('Item 2: Specialist Network',
                   400, 50, color_black, title_font)


def draw_item3(color=color_black) -> None:
    # Draw stuff for item 3
    draw_arrow((380, 150), (245, 150), (250, 155), (250, 145))
    draw_arrow((555, 150), (420, 150), (425, 155), (425, 145))
    draw_arrow((220, 175), (220, 280), (225, 275), (215, 275))
    draw_arrow((580, 280), (580, 175), (575, 180), (585, 180))
    draw_arrow((125, 300), (200, 300), (195, 305), (195, 295))
    draw_arrow((240, 300), (375, 300), (370, 305), (370, 295))
    draw_arrow((425, 300), (560, 300), (555, 305), (555, 295))
    draw_arrow((600, 300), (675, 300), (670, 305), (670, 295))
    draw_arrow((240, 320), (382, 412), (376, 412), (380, 407))
    draw_arrow((418, 412), (560, 320), (555, 319), (559, 326))
    print_text_box("Start: S  Change: C  End: E  Undo: U  Back: Esc  Reset: R  Print firing sequence: F",
                   400, 570, color, tiny_font)
    print_text_box('Item 3: Superimposed Network',
                   400, 50, color_black, title_font)


def draw_item4(color=color_black) -> None:
    # Draw stuff for item 4
    draw_arrow((380, 150), (245, 150), (250, 155), (250, 145))
    draw_arrow((555, 150), (420, 150), (425, 155), (425, 145))
    draw_arrow((220, 175), (220, 280), (225, 275), (215, 275))
    draw_arrow((580, 280), (580, 175), (575, 180), (585, 180))
    draw_arrow((125, 300), (200, 300), (195, 305), (195, 295))
    draw_arrow((240, 300), (375, 300), (370, 305), (370, 295))
    draw_arrow((425, 300), (560, 300), (555, 305), (555, 295))
    draw_arrow((600, 300), (675, 300), (670, 305), (670, 295))
    draw_arrow((240, 320), (382, 412), (376, 412), (380, 407))
    draw_arrow((418, 412), (560, 320), (555, 319), (559, 326))
    print_text_box("Start: S  Change: C  End: E  Undo: U  Back: Esc  Reset: R  Print firing sequence: F",
                   400, 570, color, tiny_font)
    print_text_box('Item 4: Reachable Marking',
                   400, 50, color_black, title_font)
    print_text_box('See explanation for item 4 on the console window.',
                   400, 80, color_black, tiny_font)


def item1(petri_net: PetriNet, input_wait: int, input_inside: int, input_done: int) -> None:
    # Simulate item 1
    petri_net.reset()
    firing_sequence = []        # List of transitions fired so far i.e. firing sequence
    # Create places and transitions
    wait = Place(input_wait, "wait")
    inside = Place(input_inside, "inside")
    done = Place(input_done, "done")
    start = Transition("start")
    change = Transition("change")
    # Add places and transitions to the Petri Net
    petri_net.add_places(wait, inside, done)
    petri_net.add_transitions(start, change)
    edges = make_edges(wait, start, start, inside,
                       inside, change, change, done)
    # Boolean variables to keep the game window running as expected
    showing_menu = False
    flag_continue = False
    running = True
    # The main loop which handles the game running
    while running:
        # Draw stuff needed
        screen.fill(background_main)
        draw_item1()
        wait.draw(50, 300)
        start.draw(200, 280)
        inside.draw(400, 300)
        change.draw(570, 280)
        done.draw(750, 300)
        petri_net.show_marking()
        if petri_net.terminate():
            pass
        # Receive key strokes event
        for _event in event.get():
            if _event.type == QUIT:
                running = False
            elif _event.type == KEYDOWN:
                if _event.key == K_s:                   # 's' is pressed -> Fire 'start'
                    if start.is_enabled():
                        start.fire()
                        print('start')
                        # Add it to the firing sequence
                        firing_sequence.append(start)
                        # Make it blink green
                        start.draw(start.posX, start.posY, color_green)
                elif _event.key == K_c:                   # 'c' is pressed -> Fire 'change'
                    if change.is_enabled():
                        change.fire()
                        print('change')
                        # Add it to the firing sequence
                        firing_sequence.append(change)
                        # Make it blink green
                        change.draw(change.posX, start.posY, color_green)
                elif _event.key == K_u:                  # 'u' is pressed -> Undo the last firing action
                    if len(firing_sequence) > 0:         # Undo only if firing sequence is not empty
                        removed: Transition
                        # Take the last transition out of the firing sequence
                        removed = firing_sequence.pop()
                        removed.undo_fire()
                        print("Undo: " + removed.name)
                        removed.draw(removed.posX, removed.posY,
                                     color_red, removed.label_position)     # Make it blink red
                elif _event.key == K_ESCAPE:             # 'Esc' is pressed -> Go back to the last screen
                    running = False
                    showing_menu = True
                    flag_continue = True
                elif _event.key == K_r:                  # 'r' is pressed -> Reset the Petri Net to the initial user input
                    print("Reset Petri Net")
                    wait.holding = input_wait
                    inside.holding = input_inside
                    done.holding = input_done
                    firing_sequence = []                 # Firing sequence is also reset
                elif _event.key == K_f:                  # 'f' is pressed -> print firing sequence to console
                    if len(firing_sequence) == 0:
                        continue
                    print_firing_sequence(firing_sequence)
            elif _event.type == KEYUP:
                pass
        # Update the game window with every action
        display.update()
        # Delay 100ms so that the blinking can be visible to the human eye
        time.delay(100)
    return flag_continue, showing_menu


def item2(petri_net: PetriNet, input_free: int, input_busy: int, input_docu: int) -> None:
    petri_net.reset()
    firing_sequence = []
    start = Transition("start")
    change = Transition("change")
    end = Transition("end")
    free = Place(input_free, "free")
    busy = Place(input_busy, "busy")
    docu = Place(input_docu, "docu")
    petri_net.add_places(free, busy, docu)
    petri_net.add_transitions(start, change, end)
    edges = make_edges(start, busy, busy, change, change,
                       docu, docu, end, end, free, free, start)
    showing_menu = False
    flag_continue = False
    running = True
    while running:
        screen.fill(background_main)
        draw_item2()
        free.draw(200, 200, color_black, 'U')
        busy.draw(400, 400)
        docu.draw(600, 200, color_black, 'U')
        start.draw(180, 380)
        change.draw(580, 380)
        end.draw(380, 180, color_black, 'U')
        petri_net.show_marking()
        if petri_net.terminate():
            pass
        for _event in event.get():
            if _event.type == QUIT:
                running = False
            elif _event.type == KEYDOWN:
                if _event.key == K_s:
                    if start.is_enabled():
                        start.fire()
                        print('start')
                        firing_sequence.append(start)
                        start.draw(start.posX, start.posY, color_green)
                elif _event.key == K_c:
                    if change.is_enabled():
                        change.fire()
                        print('change')
                        firing_sequence.append(change)
                        change.draw(change.posX, start.posY, color_green)
                elif _event.key == K_e:
                    if end.is_enabled():
                        end.fire()
                        print('end')
                        firing_sequence.append(end)
                        end.draw(end.posX, end.posY, color_green, 'U')
                elif _event.key == K_u:
                    if len(firing_sequence) > 0:
                        removed: Transition
                        removed = firing_sequence.pop()
                        removed.undo_fire()
                        print("Undo: " + removed.name)
                        removed.draw(removed.posX, removed.posY,
                                     color_red, removed.label_position)
                elif _event.key == K_ESCAPE:
                    running = False
                    showing_menu = True
                    flag_continue = True
                elif _event.key == K_r:
                    print("Reset Petri Net")
                    free.holding = input_free
                    busy.holding = input_busy
                    docu.holding = input_docu
                    firing_sequence = []
                elif _event.key == K_f:
                    if len(firing_sequence) == 0:
                        continue
                    print_firing_sequence(firing_sequence)
            elif _event.type == KEYUP:
                pass
        display.update()
        time.delay(100)
    return flag_continue, showing_menu


def item3(petri_net: PetriNet, input_free: int, input_busy: int, input_docu: int, input_wait: int, input_inside: int, input_done: int) -> None:
    petri_net.reset()
    firing_sequence = []
    start = Transition("start")
    change = Transition("change")
    end = Transition("end")
    free = Place(input_free, "free")
    busy = Place(input_busy, "busy")
    docu = Place(input_docu, "docu")
    wait = Place(input_wait, "wait")
    inside = Place(input_inside, "inside")
    done = Place(input_done, "done")
    petri_net.add_places(free, busy, docu, wait, inside, done)
    petri_net.add_transitions(start, change, end)
    edges = make_edges(start, busy, busy, change, change,
                       docu, docu, end, end, free, free, start, wait, start, start, inside, inside, change, change, done)
    running = True
    while running:
        screen.fill(background_main)
        draw_item3()
        free.draw(220, 150, color_black, 'U')
        end.draw(380, 130, color_black, 'U')
        docu.draw(580, 150, color_black, 'U')
        wait.draw(100, 300)
        start.draw(200, 280)
        busy.draw(400, 300)
        change.draw(560, 280)
        done.draw(700, 300)
        inside.draw(400, 430)
        petri_net.show_marking()
        if petri_net.terminate():
            pass
        for _event in event.get():
            if _event.type == QUIT:
                running = False
            elif _event.type == KEYDOWN:
                if _event.key == K_s:
                    if start.is_enabled():
                        start.fire()
                        print('start')
                        firing_sequence.append(start)
                        start.draw(start.posX, start.posY, color_green)
                elif _event.key == K_c:
                    if change.is_enabled():
                        change.fire()
                        print('change')
                        firing_sequence.append(change)
                        change.draw(change.posX, start.posY, color_green)
                elif _event.key == K_e:
                    if end.is_enabled():
                        end.fire()
                        print('end')
                        firing_sequence.append(end)
                        end.draw(end.posX, end.posY, color_green, 'U')
                elif _event.key == K_u:
                    if len(firing_sequence) > 0:
                        removed: Transition
                        removed = firing_sequence.pop()
                        removed.undo_fire()
                        print("Undo: " + removed.name)
                        removed.draw(removed.posX, removed.posY,
                                     color_red, removed.label_position)
                elif _event.key == K_ESCAPE:
                    running = False
                    showing_menu = True
                    flag_continue = True
                elif _event.key == K_r:
                    print("Reset Petri Net")
                    free.holding = input_free
                    busy.holding = input_busy
                    docu.holding = input_docu
                    wait.holding = input_wait
                    inside.holding = input_inside
                    done.holding = input_done
                    firing_sequence = []
                elif _event.key == K_f:
                    if len(firing_sequence) == 0:
                        continue
                    print_firing_sequence(firing_sequence)
            elif _event.type == KEYUP:
                pass
        display.update()
        time.delay(100)
    return flag_continue, showing_menu


def item4(petri_net: PetriNet, input_free: int, input_busy: int, input_docu: int, input_wait: int, input_inside: int, input_done: int) -> None:
    petri_net.reset()
    print(
        "\nitem 4: In the initial marking, the only enabled transition is 'start'. Firing this transition leads to the marking [0.free,1.busy,0.docu,2.wait,1.inside,0.done].")
    print(
        "\nAfter the 'start' transition is fired, the only enabled transition is 'change'. Firing this transition leads to the marking [0.free,0.busy,1.docu,2.wait,0.inside,1.done].")
    print(
        "\nAfter the 'change' transition is fired, the only enabled transition is 'end'. Firing this transition leads to the marking [1.free,0.busy,0.docu,2.wait,0.inside,1.done].")
    print("\nYou can simulate this Petri Net as you can with item 3.")
    firing_sequence = []
    start = Transition("start")
    change = Transition("change")
    end = Transition("end")
    free = Place(input_free, "free")
    busy = Place(input_busy, "busy")
    docu = Place(input_docu, "docu")
    wait = Place(input_wait, "wait")
    inside = Place(input_inside, "inside")
    done = Place(input_done, "done")
    petri_net.add_places(free, busy, docu, wait, inside, done)
    petri_net.add_transitions(start, change, end)
    edges = make_edges(start, busy, busy, change, change,
                       docu, docu, end, end, free, free, start, wait, start, start, inside, inside, change, change, done)
    running = True
    while running:
        screen.fill(background_main)
        draw_item4()
        free.draw(220, 150, color_black, 'U')
        end.draw(380, 130, color_black, 'U')
        docu.draw(580, 150, color_black, 'U')
        wait.draw(100, 300)
        start.draw(200, 280)
        busy.draw(400, 300)
        change.draw(560, 280)
        done.draw(700, 300)
        inside.draw(400, 430)
        petri_net.show_marking()
        if petri_net.terminate():
            pass
        for _event in event.get():
            if _event.type == QUIT:
                running = False
            elif _event.type == KEYDOWN:
                if _event.key == K_s:
                    if start.is_enabled():
                        start.fire()
                        print('start')
                        firing_sequence.append(start)
                        start.draw(start.posX, start.posY, color_green)
                elif _event.key == K_c:
                    if change.is_enabled():
                        change.fire()
                        print('change')
                        firing_sequence.append(change)
                        change.draw(change.posX, start.posY, color_green)
                elif _event.key == K_e:
                    if end.is_enabled():
                        end.fire()
                        print('end')
                        firing_sequence.append(end)
                        end.draw(end.posX, end.posY, color_green, 'U')
                elif _event.key == K_u:
                    if len(firing_sequence) > 0:
                        removed: Transition
                        removed = firing_sequence.pop()
                        removed.undo_fire()
                        print("Undo: " + removed.name)
                        removed.draw(removed.posX, removed.posY,
                                     color_red, removed.label_position)
                elif _event.key == K_ESCAPE:
                    running = False
                    showing_menu = True
                    flag_continue = True
                elif _event.key == K_r:
                    print("Reset Petri Net")
                    free.holding = input_free
                    busy.holding = input_busy
                    docu.holding = input_docu
                    wait.holding = input_wait
                    inside.holding = input_inside
                    done.holding = input_done
                    firing_sequence = []
                elif _event.key == K_f:
                    if len(firing_sequence) == 0:
                        continue
                    print_firing_sequence(firing_sequence)
            elif _event.type == KEYUP:
                pass
        display.update()
        time.delay(100)
    return flag_continue, showing_menu


if __name__ == "__main__":
    petri_net = PetriNet()      # Initialize Petri Net
    # Boolean variables to keep the game window running
    showing_menu = True
    flag_continue = True
    prompt_to_menu = True
    # This loop handles which screen is shown
    while showing_menu:
        showing_menu = False
        while flag_continue:
            flag_continue = False
            if prompt_to_menu:
                item_index, flag_continue = show_menu()
                if not flag_continue:
                    break
            if item_index == 0:
                if prompt_to_menu:
                    user_input, flag_continue, showing_menu = input_promt1()
                else:
                    flag_continue = True
                if flag_continue and not showing_menu:
                    flag_continue, showing_menu = item1(petri_net, user_input[0],
                                                        user_input[1], user_input[2])
                    if flag_continue and showing_menu:
                        user_input, flag_continue, showing_menu = input_promt1()
                        prompt_to_menu = showing_menu
                elif flag_continue and showing_menu:
                    continue
            elif item_index == 1:
                if prompt_to_menu:
                    user_input, flag_continue, showing_menu = input_promt2()
                else:
                    flag_continue = True
                if flag_continue and not showing_menu:
                    flag_continue, showing_menu = item2(petri_net, user_input[0],
                                                        user_input[1], user_input[2])
                    if flag_continue and showing_menu:
                        user_input, flag_continue, showing_menu = input_promt2()
                        prompt_to_menu = showing_menu
                elif flag_continue and showing_menu:
                    continue
            elif item_index == 2:
                if prompt_to_menu:
                    user_input, flag_continue, showing_menu = input_promt3()
                else:
                    flag_continue = True
                if flag_continue and not showing_menu:
                    flag_continue, showing_menu = item3(petri_net, user_input[0],
                                                        user_input[1], user_input[2], user_input[3], user_input[4], user_input[5])
                    if flag_continue and showing_menu:
                        user_input, flag_continue, showing_menu = input_promt3()
                        prompt_to_menu = showing_menu
                elif flag_continue and showing_menu:
                    continue
            elif item_index == 3:
                item4(petri_net, 1, 0, 0, 3, 0, 0)
