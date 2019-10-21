from math import sqrt

# Constants
MU_SOL = 1.32712440042 * (10**20)
RAD_SOL = 695510000

MU_EARTH = 3.986004418 * (10**14)
RAD_EARTH = 6378000


def calc_delta_v(initial_alt, target_perigee):
    initial_alt *= 1000
    target_perigee *= 1000

    v1 = sqrt(MU_EARTH/(initial_alt + RAD_EARTH))
    sm_axis = (initial_alt + target_perigee) / 2 + RAD_EARTH
    v2 = sqrt(MU_EARTH * (2/(initial_alt + RAD_EARTH) - (1 / sm_axis)))

    return abs(v2 - v1)


if __name__ == '__main__':
    print("Delta-V for a 600km to 800km transfer")
    print(calc_delta_v(600, 800))
