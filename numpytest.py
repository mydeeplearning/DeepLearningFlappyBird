#encoding=utf-8

import numpy as np


def test1():

    x_t1 = np.ones((2, 2))
    x_t2 = np.ones((2, 2))
    x_t2[:,:] = 2
    x_t3 = np.ones((2, 2))
    x_t3[:,:] = 3
    x_t4 = np.ones((2, 2))
    x_t4[:,:] = 4 
    s_t = np.stack((x_t1, x_t2, x_t3, x_t4), axis=2)
    x_t = np.zeros((2, 2, 1))
    s_t1 = np.append(x_t, s_t[:, :, :3], axis=2)
    # print s_t[:, :, :3]
    print s_t1

    return

def test2():
    import sys
    sys.path.append("game/")
    import wrapped_flappy_bird as game
    game_state = game.GameState()
    do_nothing = np.zeros(2)
    do_nothing[0] = 1
    i = 0
    while True:
        x_t, r_0, terminal = game_state.frame_step(do_nothing)
        i += 1
        print i
    return

if __name__ == '__main__':
    # test1()
    test2()