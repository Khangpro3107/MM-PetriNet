import pygame as pg

pg.init()
pg.font.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Petri Net")
font = pg.font.SysFont('Calibri', 24, True)
title_font = pg.font.SysFont('Consolas', 36, True)
choice_font = pg.font.SysFont('Consolas', 24, True)
small_font = pg.font.SysFont('Calibri', 16, True)
tiny_font = pg.font.SysFont('Consolas', 10)

color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_yellow = (255, 255, 0)
background_main = (24, 239, 242)
place_radius = 25
transition_width = 40
line_width = 2

def draw_choice_box(text_color, background_color, choice_text, posY, posX=400) -> None:
    text = choice_font.render(choice_text, True, text_color, background_color)
    text_rect = text.get_rect()
    text_rect.center = (posX, posY)
    screen.blit(text, text_rect)

def user_choice() -> None:
    title_text = title_font.render("This is the title", True, color_black)
    title_text_rect = title_text.get_rect()
    title_text_rect.center = (400, 50)
    screen.blit(title_text, title_text_rect)
    draw_choice_box(color_red, color_green, '  Demo Item 1  ', 150)
    draw_choice_box(color_red, color_green, '  Demo Item 2  ', 210)
    draw_choice_box(color_red, color_green, '  Demo Item 3  ', 270)
    draw_choice_box(color_red, color_green, '  Demo Item 4  ', 330)
    guide_text = tiny_font.render(
        'Press arrow keys to choose and press spacebar key to confirm.', True, color_black)
    guide_text_rect = guide_text.get_rect()
    guide_text_rect.center = (400, 560)
    screen.blit(guide_text, guide_text_rect)

def show_menu():
    exercise_index = -1
    run = True
    flag_continue = False
    while run:
        screen.fill(background_main)
        user_choice()
        if exercise_index == 0:
            draw_choice_box(color_black, color_yellow, '  Demo Item 1  ', 150)
        elif exercise_index == 1:
            draw_choice_box(color_black, color_yellow, '  Demo Item 2  ', 210)
        elif exercise_index == 2:
            draw_choice_box(color_black, color_yellow, '  Demo Item 3  ', 270)
        elif exercise_index == 3:
            draw_choice_box(color_black, color_yellow, '  Demo Item 4  ', 330)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    if exercise_index == 3:
                        exercise_index = 0
                    else:
                        exercise_index += 1
                if event.key == pg.K_UP:
                    if exercise_index == 0:
                        exercise_index = 3
                    elif exercise_index >= 0:
                        exercise_index -= 1
                if event.key == pg.K_SPACE:
                    flag_continue = True
                    run = False
            elif event.type == pg.KEYUP:
                pass
        pg.display.update()
    return exercise_index, flag_continue

def input_promt1():
    user_input = ["", "", ""]
    text_wait = font.render("wait", True, color_black)
    text_inside = font.render("inside", True, color_black)
    text_done = font.render("done", True, color_black)
    flag_continue = False
    input_rect = [pg.Rect(200, 200, 80, 24), pg.Rect(
        400, 200, 80, 24), pg.Rect(600, 200, 80, 24)]
    color_active = pg.Color(color_yellow)
    color_passive = pg.Color(color_white)
    color = [color_passive, color_passive, color_passive]
    active = [False, False, False]
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in range(3):
                    if input_rect[i].collidepoint(event.pos):
                        active[i] = True
                        color[i] = color_active
                    else:
                        active[i] = False
                        color[i] = color_passive
            if event.type == pg.KEYDOWN:
                for i in range(3):
                    if active[i]:
                        if event.key == pg.K_BACKSPACE:
                            user_input[i] = user_input[i][:-1]
                        else:
                            temp = event.unicode
                            if temp <= '9' and temp >= '0':
                                user_input[i] += temp
                if event.key == pg.K_SPACE:
                    flag_continue = True
                    running = False
            if event.type == pg.KEYUP:
                pass
        screen.fill(background_main)
        screen.blit(text_wait, (150, 200))
        screen.blit(text_inside, (335, 200))
        screen.blit(text_done, (550, 200))
        util_text = font.render("Please input the amount of tokens in each place", True, color_black)
        util_text_rect = util_text.get_rect()
        util_text_rect.center = (400, 100)
        screen.blit(util_text, util_text_rect)
        for i in range(3):
            text_surface = font.render(user_input[i], True, color_black)
            pg.draw.rect(screen, color[i], input_rect[i])
            screen.blit(
                text_surface, (input_rect[i].x, input_rect[i].y))
        pg.display.update()
    for i in range(3):
        if len(user_input[i]):
            user_input[i] = int(user_input[i])
        else:
            user_input[i] = 0
    return user_input, flag_continue

def input_promt2():
    user_input = ["", "", ""]
    text_free = font.render("free", True, color_black)
    text_busy = font.render("busy", True, color_black)
    text_docu = font.render("docu", True, color_black)
    flag_continue = False
    input_rect = [pg.Rect(200, 200, 80, 24), pg.Rect(
        400, 200, 80, 24), pg.Rect(600, 200, 80, 24)]
    color_active = pg.Color(color_yellow)
    color_passive = pg.Color(color_white)
    color = [color_passive, color_passive, color_passive]
    active = [False, False, False]
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in range(3):
                    if input_rect[i].collidepoint(event.pos):
                        active[i] = True
                        color[i] = color_active
                    else:
                        active[i] = False
                        color[i] = color_passive
            if event.type == pg.KEYDOWN:
                for i in range(3):
                    if active[i]:
                        if event.key == pg.K_BACKSPACE:
                            user_input[i] = user_input[i][:-1]
                        else:
                            temp = event.unicode
                            if temp <= '9' and temp >= '0':
                                user_input[i] += temp
                if event.key == pg.K_SPACE:
                    flag_continue = True
                    running = False
            if event.type == pg.KEYUP:
                pass
        screen.fill(background_main)
        screen.blit(text_free, (150, 200))
        screen.blit(text_busy, (350, 200))
        screen.blit(text_docu, (550, 200))
        util_text = font.render("Please input the amount of tokens in each place", True, color_black)
        util_text_rect = util_text.get_rect()
        util_text_rect.center = (400, 100)
        screen.blit(util_text, util_text_rect)
        for i in range(3):
            text_surface = font.render(user_input[i], True, color_black)
            pg.draw.rect(screen, color[i], input_rect[i])
            screen.blit(
                text_surface, (input_rect[i].x, input_rect[i].y))
        pg.display.update()
    for i in range(3):
        if len(user_input[i]):
            user_input[i] = int(user_input[i])
        else:
            user_input[i] = 0
    return user_input, flag_continue

def input_promt3():
    user_input = ["", "", "", "", "", ""]
    text_wait = font.render("wait", True, color_black)
    text_inside = font.render("inside", True, color_black)
    text_done = font.render("done", True, color_black)
    text_free = font.render("free", True, color_black)
    text_busy = font.render("busy", True, color_black)
    text_docu = font.render("docu", True, color_black)
    flag_continue = False
    input_rect = [pg.Rect(200, 200, 80, 24), pg.Rect(
        400, 200, 80, 24), pg.Rect(600, 200, 80, 24), pg.Rect(200, 400, 80, 24), pg.Rect(400, 400, 80, 24), pg.Rect(600, 400, 80, 24)]
    color_active = pg.Color(color_yellow)
    color_passive = pg.Color(color_white)
    color = [color_passive, color_passive, color_passive, color_passive, color_passive, color_passive]
    active = [False, False, False, False, False, False]
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in range(6):
                    if input_rect[i].collidepoint(event.pos):
                        active[i] = True
                        color[i] = color_active
                    else:
                        active[i] = False
                        color[i] = color_passive
            if event.type == pg.KEYDOWN:
                for i in range(6):
                    if active[i]:
                        if event.key == pg.K_BACKSPACE:
                            user_input[i] = user_input[i][:-1]
                        else:
                            temp = event.unicode
                            if temp <= '9' and temp >= '0':
                                user_input[i] += temp
                if event.key == pg.K_SPACE:
                    flag_continue = True
                    running = False
            if event.type == pg.KEYUP:
                pass
        screen.fill(background_main)
        screen.blit(text_free, (150, 200))
        screen.blit(text_busy, (335, 200))
        screen.blit(text_docu, (550, 200))
        screen.blit(text_wait, (150, 400))
        screen.blit(text_inside, (335, 400))
        screen.blit(text_done, (550, 400))
        util_text = font.render("Please input the amount of tokens in each place", True, color_black)
        util_text_rect = util_text.get_rect()
        util_text_rect.center = (400, 100)
        screen.blit(util_text, util_text_rect)
        for i in range(6):
            text_surface = font.render(user_input[i], True, color_black)
            pg.draw.rect(screen, color[i], input_rect[i])
            screen.blit(
                text_surface, (input_rect[i].x, input_rect[i].y))
        pg.display.update()
    for i in range(6):
        if len(user_input[i]):
            user_input[i] = int(user_input[i])
        else:
            user_input[i] = 0
    return user_input, flag_continue

def draw_arrow(start_pos, end_pos, other_pos1, other_pos2, color=color_black) -> None:
    pg.draw.line(screen, color, start_pos, end_pos, line_width)
    pg.draw.line(screen, color, other_pos1, end_pos, line_width)
    pg.draw.line(screen, color, other_pos2, end_pos, line_width)

class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.in_arcs = []
        self.out_arcs = []
        self.posX = -1
        self.posY = -1
        self.label_position = 'D'


class Arc:
    def __init__(self, src, dst) -> None:
        self.src = src
        self.dst = dst
        src.out_arcs.append(self)
        dst.in_arcs.append(self)

    def draw(self, start_pos: int, end_pos: int, edge_pos1: int, edge_pos2: int, color=color_black) -> None:
        draw_arrow(start_pos, end_pos, edge_pos1, edge_pos2, color)


class Place:
    def __init__(self, num_tokens: int, name: str) -> None:
        self.holding = num_tokens
        self.name = name
        self.in_arcs = []
        self.out_arcs = []

    def show_tokens(self, posX: int, posY: int, color=color_black) -> None:
        text = font.render(str(self.holding), True, color)
        text_rect = text.get_rect()
        text_rect.center = (posX, posY)
        screen.blit(text, text_rect)

    def draw(self, posX: int, posY: int, color=color_black, position='D') -> None:
        pg.draw.circle(screen, color, (posX, posY), place_radius, line_width)
        text = font.render(self.name, True, color)
        text_rect = text.get_rect()
        if position == 'D':
            text_rect.center = (posX, posY + place_radius + 10)
        else:
            text_rect.center = (posX, posY - place_radius - 12)
        screen.blit(text, text_rect)
        self.show_tokens(posX, posY + 3, color)


class Transition(Node):
    def is_active(self) -> bool:
        for in_arc in self.in_arcs:
            if in_arc.src.holding < 1:
                return False
        return True

    def fire(self) -> None:
        if self.is_active():
            for in_arc in self.in_arcs:
                in_arc.src.holding -= 1
            for out_arc in self.out_arcs:
                out_arc.dst.holding += 1

    def undo_fire(self) -> None:
        for in_arc in self.in_arcs:
            in_arc.src.holding += 1
        for out_arc in self.out_arcs:
            out_arc.dst.holding -= 1

    def draw(self, posX: int, posY: int, color=color_black, label_position='D') -> None:
        self.posX = posX
        self.posY = posY
        self.label_position = label_position
        pg.draw.rect(screen, color, pg.Rect(
            posX, posY, transition_width, transition_width), line_width)
        text = font.render(self.name, True, color)
        text_rect = text.get_rect()
        if label_position == 'D':
            text_rect.center = (posX + 20, posY + transition_width + 15)
        else:
            text_rect.center = (posX + 20, posY - 15)
        screen.blit(text, text_rect)


class PetriNet:
    def __init__(self) -> None:
        self.transitions = []
        self.places = []

    def add_transitions(self, *args) -> None:
        for arg in args:
            self.transitions.append(arg)

    def add_places(self, *args) -> None:
        for arg in args:
            self.places.append(arg)

    def show_marking(self, color=color_black) -> None:
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
        text = font.render(printing_str, True, color)
        text_rect = text.get_rect()
        text_rect.center = (400, 500)
        screen.blit(text, text_rect)

    def terminate(self, color=color_black) -> bool:
        for transition in self.transitions:
            if transition.is_active():
                return False
        text = font.render(
            "This Petri Net has reached its terminal marking!", True, color)
        text_rect = text.get_rect()
        text_rect.center = (400, 540)
        screen.blit(text, text_rect)
        return True


def make_edges(*args) -> list:
    res = []
    for i in range(len(args) // 2):
        new_arc = Arc(args[2 * i], args[2 * i + 1])
        res.append(new_arc)
    return res

def draw_exercise1(color=color_black) -> None:
    util_text = font.render(
        "Start: S  Change: C  Undo: U", True, color, (224, 92, 92))
    screen.blit(util_text, (10, 10))
    draw_arrow((75, 300), (200, 300), (195, 295), (195, 305))
    draw_arrow((240, 300), (375, 300), (370, 295), (370, 305))
    draw_arrow((425, 300), (570, 300), (565, 295), (565, 305))
    draw_arrow((610, 300), (725, 300), (720, 295), (720, 305))

def draw_exercise2(color=color_black) -> None:
    util_text = font.render(
        "Start: S  Change: C  End: E  Undo: U", True, color, (224, 92, 92))
    screen.blit(util_text, (10, 10))
    draw_arrow((200, 225), (200, 380), (195, 375), (205, 375))
    draw_arrow((600, 380), (600, 225), (595, 230), (605, 230))
    draw_arrow((220, 400), (375, 400), (370, 395), (370, 405))
    draw_arrow((423, 400), (580, 400), (575, 395), (575, 405))
    draw_arrow((380, 200), (225, 200), (230, 205), (230, 195))
    draw_arrow((575, 200), (420, 200), (425, 205), (425, 195))

def draw_exercise3(color=color_black) -> None:
    util_text = font.render(
        "Start: S  Change: C  End: E  Undo: U", True, color, (224, 92, 92))
    screen.blit(util_text, (10, 10))
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

def exercise1(petri_net: PetriNet, input_wait: int, input_inside: int, input_done: int) -> None:
    firing_sequence = []
    wait = Place(input_wait, "wait")
    inside = Place(input_inside, "inside")
    done = Place(input_done, "done")
    start = Transition("start")
    change = Transition("change")
    petri_net.add_places(wait, inside, done)
    petri_net.add_transitions(start, change)
    edges = make_edges(wait, start, start, inside,
                       inside, change, change, done)
    running = True
    while running:
        screen.fill(background_main)
        draw_exercise1()
        wait.draw(50, 300)
        start.draw(200, 280)
        inside.draw(400, 300)
        change.draw(570, 280)
        done.draw(750, 300)
        petri_net.show_marking()
        if petri_net.terminate():
            pass
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    if start.is_active():
                        start.fire()
                        print('start')
                        firing_sequence.append(start)
                        start.draw(start.posX, start.posY, color_green)
                elif event.key == pg.K_c:
                    if change.is_active():
                        change.fire()
                        print('change')
                        firing_sequence.append(change)
                        change.draw(change.posX, start.posY, color_green)
                elif event.key == pg.K_u:
                    if len(firing_sequence) > 0:
                        removed: Transition
                        removed = firing_sequence.pop()
                        removed.undo_fire()
                        print("Undo: " + removed.name)
                        removed.draw(removed.posX, removed.posY,
                                     color_red, removed.label_position)

            elif event.type == pg.KEYUP:
                pass
        pg.display.update()
        pg.time.delay(100)

def exercise2(petri_net: PetriNet, input_free: int, input_busy: int, input_docu: int) -> None:
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
    running = True
    while running:
        screen.fill(background_main)
        draw_exercise2()
        free.draw(200, 200, color_black, 'U')
        busy.draw(400, 400)
        docu.draw(600, 200, color_black, 'U')
        start.draw(180, 380)
        change.draw(580, 380)
        end.draw(380, 180, color_black, 'U')
        petri_net.show_marking()
        if petri_net.terminate():
            pass
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    if start.is_active():
                        start.fire()
                        print('start')
                        firing_sequence.append(start)
                        start.draw(start.posX, start.posY, color_green)
                elif event.key == pg.K_c:
                    if change.is_active():
                        change.fire()
                        print('change')
                        firing_sequence.append(change)
                        change.draw(change.posX, start.posY, color_green)
                elif event.key == pg.K_e:
                    if end.is_active():
                        end.fire()
                        print('end')
                        firing_sequence.append(end)
                        end.draw(end.posX, end.posY, color_green, 'U')
                elif event.key == pg.K_u:
                    if len(firing_sequence) > 0:
                        removed: Transition
                        removed = firing_sequence.pop()
                        removed.undo_fire()
                        print("Undo: " + removed.name)
                        removed.draw(removed.posX, removed.posY,
                                     color_red, removed.label_position)
            elif event.type == pg.KEYUP:
                pass
        pg.display.update()
        pg.time.delay(100)

def exercise3(petri_net: PetriNet, input_free: int, input_busy: int, input_docu: int, input_wait: int, input_inside: int, input_done: int) -> None:
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
        draw_exercise3()
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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    if start.is_active():
                        start.fire()
                        print('start')
                        firing_sequence.append(start)
                        start.draw(start.posX, start.posY, color_green)
                elif event.key == pg.K_c:
                    if change.is_active():
                        change.fire()
                        print('change')
                        firing_sequence.append(change)
                        change.draw(change.posX, start.posY, color_green)
                elif event.key == pg.K_e:
                    if end.is_active():
                        end.fire()
                        print('end')
                        firing_sequence.append(end)
                        end.draw(end.posX, end.posY, color_green, 'U')
                elif event.key == pg.K_u:
                    if len(firing_sequence) > 0:
                        removed: Transition
                        removed = firing_sequence.pop()
                        removed.undo_fire()
                        print("Undo: " + removed.name)
                        removed.draw(removed.posX, removed.posY,
                                     color_red, removed.label_position)
            elif event.type == pg.KEYUP:
                pass
        pg.display.update()
        pg.time.delay(100)

def exercise4(petri_net: PetriNet, input_free: int, input_busy: int, input_docu: int, input_wait: int, input_inside: int, input_done: int) -> None:
    pass
    '''firing_sequence = []
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
        pass'''

if __name__ == "__main__":
    petri_net = PetriNet()
    exercise_index, flag_continue = show_menu()
    if flag_continue:
        flag_continue = False
        if exercise_index == 0:
            user_input, flag_continue = input_promt1()
            if flag_continue:
                exercise1(petri_net, user_input[0],
                          user_input[1], user_input[2])
        elif exercise_index == 1:
            user_input, flag_continue = input_promt2()
            if flag_continue:
                exercise2(petri_net, user_input[0],
                          user_input[1], user_input[2])
        elif exercise_index == 2:
            user_input, flag_continue = input_promt3()
            if flag_continue:
                exercise3(petri_net, user_input[0],
                          user_input[1], user_input[2], user_input[3], user_input[4], user_input[5])
        elif exercise_index == 3:
            exercise3(petri_net, 1, 0, 0, 3, 0, 0)
