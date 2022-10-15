# hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()

# hurdle 3
def step_forward():
    if not wall_in_front():
        while not wall_in_front():
            move()
        jump()
        move()
        turn_right()
        move()
        turn_left()
        if not front_is_clear():
            jump()
            move()
            turn_right()
            move()
            turn_left()
    elif not front_is_clear():
        jump()
        move()
        turn_right()
        move()
        turn_left()
        while not wall_in_front():
            move()
            
while not at_goal():
    step_forward()
