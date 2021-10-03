import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
turtle.bgpic("day25/us_states_game/blank_states_img.gif")
screen.setup(732,505)
total_states = 50
screen.tracer(0)

data = pandas.read_csv('day25/us_states_game/50_states.csv')
states_list = data.state.to_list()

guessed_states = []
count = 0
while len(guessed_states) <= 50:
    state_input = turtle.textinput(title='Guess the U.S. States', prompt=f'{count}/50 Type the names of U.S. States')
    state_input = state_input.title()

    if state_input == 'Exit':
        break
    if state_input in states_list:
        guessed_states.append(state_input)
        my_cord = data[data.state == state_input]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(int(my_cord.x), int(my_cord.y))
        state_turtle.write(arg=state_input, align="center", font=("san", 8, "normal"))
        screen.update()
        count +=1

remaining_states = list(set(states_list) - set(guessed_states))

user_csv_info = {
    'remaining states': remaining_states,
}

user_csv = pandas.DataFrame(user_csv_info)
user_csv.to_csv('day25/us_states_game/user_study.csv')