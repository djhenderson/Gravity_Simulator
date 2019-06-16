# Simuation.py

import sys
import imageio
from typing import List
from Newton import SpaceImage, Body

Axises = List[float]


def create_gif(name: str, images: List[str]):
    with imageio.get_writer(name, mode='I') as writer:
        for filename in images:
            image = imageio.imread(filename)
            writer.append_data(image)

    return name


def simulate(
        space: SpaceImage,
        time_for_frame: int,
        frames: int,
        gif_name: str,
        axises: List[float],
    ):
    images = []
    for frame in range(frames):
        images.append(
            space.save(
                f'frames/sim_frame_{frame}.png',
                axises,
                frame * time_for_frame,
            )
        )
        sys.stdout.write(f'\r{int(frame * 100 / frames):3} %')
        sys.stdout.flush()
        for i in range(time_for_frame):
            space.next_image(1)

    sys.stdout.write("\r100 % - saving animated gif ...")
    create_gif(f'gifs/{gif_name}.gif', images)


def save_indata(
        name: str,
        bodies: List[Body],
        frames: int,
        seconds_frame: int,
    ):
    with open(f'indata/{name}.txt', 'w+', encoding='utf-8') as f:
        f.write(f'Name: {name}, Frames: {frames}, Seconds/Frame: {seconds_frame}')
        for body in bodies:
            f.write(body.disp())

    print(f'Input-data saved to indata/{name}.txt')


if __name__ == "__main__":
    # Example data
    # mars = Body(
        # 'Mars',  # name
        # [0.0, -3700000],  # position
        # 6.4171 * 10 ** 23,  # mass: kg - https://en.wikipedia.org/wiki/Mars
        # [3000, 0.0],  # velocity
        # 2.0 * 3_389.5 * 1000.0,  # diameter: meter - https://en.wikipedia.org/wiki/Mars
        # [0.0, 0.0],  # applied_force
        # [0.0, 0.0],  # acceleration
    # )

    # Earth centric Earth-moon system
    earth = Body(
        'Earth',  # name
        [0.0, 0.0],  # position
        5.97237 * 10 ** 24,  # mass: kg - https://en.wikipedia.org/wiki/Earth_mass
        [0.0, 0.0],  # velocity
        2.9 * 6_371.0 * 1_000.0,  # diameter: meter -
        [0.0, 0.0],  # applied_force
        [0.0, 0.0],  # acceleration
    )
    moon = Body(
        'Moon',  # name
        [0.0, 384_399.0 * 1_000.0],  # position
        7.342 * 10 ** 22,  # mass: kg - https://en.wikipedia.org/wiki/Moon
        [1_022.0 , 0.0],  # velocity
        2.0 * 1_737.1 * 1_000.0,  # diameter: meter - https://en.wikipedia.org/wiki/Moon
        [0.0, 0.0],  # applied_force
        [0.0, 0.0],  # acceleration
    )
    init_image = SpaceImage([earth, moon])
    axises = [-420_000_000.0, 420_000_000.0, -420_000_000.0, 420_000_000.0]
    seconds_frame = 60 * 60  # = 1 hour
    frames = 686
    gif_name = input('simulation name: ')
    save_indata(gif_name, [earth, moon], frames, seconds_frame)
    simulate(init_image, seconds_frame, frames, gif_name, axises)
    print(f'\nSimulation saved to gifs/{gif_name}.gif')
