# Newton.py

from basic_linalg import *
import imageio
import matplotlib.pyplot as plt

# from https://en.wikipedia.org/wiki/Gravitational_constant
G = 6.67408 * 10 ** (-11)  # units: N · (m/kg)² or m³ ⋅ kg⁻¹ ⋅ s⁻²


class Body:
    name: str
    position: Vector
    mass: float
    velocity: Vector
    diameter: float
    color: str
    applied_force: Vector
    acceleration: Vector

    def __init__(
        self,
        name: str,
        position: Vector,
        mass: float,
        velocity: Vector,
        diameter: float,
        applied_force: Vector,
        acceleration: Vector,
    ):
        self.name = name
        self.position = position
        self.mass = mass
        self.velocity = velocity
        self.diameter = diameter
        self.color = 'black'
        self.applied_force = applied_force
        self.acceleration = acceleration

    def disp(self):
        return (
            f'Name: {self.name}, '
            f'Position: {self.position!r}, '
            f'Velocity: {self.velocity!r}, '
            f'Mass: {self.mass} \n'
        )


def calculate_force(obj1: Body, obj2: Body) -> Vector:
    force_direction = vector_addition(
        obj2.position,
        vector_multiplication_by_scalar(-1.0, obj1.position)
    )
    distance = vector_length(force_direction)
    total_force = (G * obj1.mass * obj2.mass) / (distance ** 2)
    return vector_multiplication_by_scalar(total_force / distance, force_direction)


class SpaceImage:
    bodies: List[Body]

    def __init__(self, bodies: List[Body]):
        self.bodies = bodies

    def next_image(self, jump: int):
        new_bodies: List[Body] = []
        for obj in self.bodies:

            obj.position = vector_addition(
                obj.position,
                vector_multiplication_by_scalar(jump, obj.velocity)
            )
            obj.velocity = vector_addition(
                obj.velocity,
                vector_multiplication_by_scalar(jump, obj.acceleration)
                )
            new_bodies.append(obj)

        self.bodies = new_bodies
        new_bodies = []
        for obj in self.bodies:
            resulting_force = [0.0, 0.0]
            for other_obj in self.bodies:
                if other_obj.position != obj.position:
                    resulting_force = vector_addition(
                        resulting_force,
                        calculate_force(obj, other_obj),
                    )

            obj.applied_force = resulting_force
            obj.acceleration = vector_multiplication_by_scalar(1 / obj.mass, resulting_force)
            new_bodies.append(obj)

        self.bodies = new_bodies

    def add_body(self, body: Body):
        self.bodies.append(body)

    def show(self):
        for body in self.bodies:
            plt.scatter(
                body.position[0],
                body.position[1],
                body.diameter / 10 ** 5,
                edgecolors='none',
            )

    def save(self, file_name, axis, second):
        plt.axis(axis)
        plt.title(f'{second} seconds')
        for body in self.bodies:
            plt.scatter(
                body.position[0],
                body.position[1],
                body.diameter / 10 ** 5,
                edgecolors='none',
            )
            if vector_length(body.applied_force) and vector_length(body.velocity) != 0:
                plt.quiver(
                    body.position[0],
                    body.position[1],
                    body.applied_force[0],
                    body.applied_force[1],
                    color=['r'],
                    scale_units='height',
                )
                plt.quiver(
                    body.position[0],
                    body.position[1],
                    body.velocity[0],
                    body.velocity[1],
                    color=['b'],
                )

        plt.savefig(file_name, bbox_inches='tight')
        plt.clf()
        return file_name
