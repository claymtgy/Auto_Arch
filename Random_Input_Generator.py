import random
rand_integer=random.randint(1,8)
rand_input = 0

up_input = ('up')
down_input = ('down')
left_input = ('left')
right_input = ('right')
a_input = ('A')
b_input = ('B')
select_input = ('select')
start_input = ('start')


match rand_integer:
    case 1: rand_input = up_input
    case 2: rand_input = down_input
    case 3: rand_input = left_input
    case 4: rand_input = right_input
    case 5: rand_input = a_input
    case 6: rand_input = b_input
    case 7: rand_input = select_input
    case 8: rand_input = start_input


print(rand_input)