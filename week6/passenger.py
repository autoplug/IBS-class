import random


def take_random_seat(seats):
    seat = random.choice(seats)
    return take_a_seat(seat, seats)


def take_a_seat(seat, seats):
    return_seats = seats
    return_seats.remove(seat)
    return return_seats


def check_seats(seat, seats):
    return seat in seats


def fill_the_plane(N):
    seats = list(range(N))

    # drung ppl
    seats = take_random_seat(seats)

    for ppl in range(1, N):
        if ppl == N-1:
            return 1 if check_seats(ppl, seats) else 0
        if check_seats(ppl, seats):
            seats = take_a_seat(ppl, seats)
        else:
            seats = take_random_seat(seats)


def get_probability(M, N):
    sum = 0
    for i in range(M):

        res = fill_the_plane(N)
        sum += res

    return sum / M


# HW try to optimalize it
print(get_probability(1_000_000, 2))
