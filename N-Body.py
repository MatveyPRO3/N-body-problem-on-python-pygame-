from numpy import array, round
from math import dist, pi, sqrt
import pygame
from time import sleep
import plotly.express as px

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

clock = pygame.time.Clock()


class particle():
    def __init__(self, position, mass, start_impulse=(0, 0)) -> None:
        self.position = array(position)
        self.mass = mass
        self.velocity = array(array(start_impulse)/self.mass)
        self.acceleration = array([0, 0])
        self.force = array([0, 0])

    def update(self, time):
        self.acceleration = self.force / self.mass
        self.velocity = self.velocity+self.acceleration
        self.position = self.position+self.velocity
        # self.position = self.position + (self.velocity*time)
        # self.position = self.position + ((self.acceleration * time**2) / 2)
        # self.velocity = self.velocity + self.acceleration*time

        # d какой момант мы призваем и что хотим получить порядок вжен перепроверь

    def apply_gravity(self, particles):
        self.force = array([0, 0])
        for p in particles:
            if p is self:
                continue
            d = dist(self.position, p.position)
            vector = p.position-self.position
            self.force = self.force + G * self.mass * p.mass / d**2 * vector / d


def convert_coordinates_to_pg(x, y):
    return x+WIDTH/2, y+HEIGHT/2


def main_draw(screen):
    screen.fill("white")
    for p in particles:
        pygame.draw.circle(
            screen, "black", convert_coordinates_to_pg(* p.position), sqrt(p.mass/pi))


def get_total_impulse(particles):
    total_impulse = array([0, 0])
    for p in particles:
        total_impulse = total_impulse + p.mass*p.velocity
    return total_impulse


def get_kinetic_e(particles):
    kinetic_e = 0
    for p in particles:
        kinetic_e += (p.mass *
                      ((sqrt(p.velocity[0]**2+p.velocity[1]**2))**2)) / 2
    return kinetic_e


def get_potential_e(particles):
    potential_e = 0
    for i, p1 in enumerate(particles):
        for p2 in particles[i+1:]:
            potential_e += -G*p1.mass*p2.mass/dist(p1.position, p2.position)
    return potential_e


def get_total_e(particles):
    return get_kinetic_e(particles) + get_potential_e(particles)


G = 10
fps = 60

# particles = [particle([0, 0], 1000,(0,0)), particle(
#     [100, 20], 50, (0, 500)),particle(
#     [140, 20], 50, (0, -500))]
particles = [particle([0, 0], 1500, (0, -1000)), particle(
    [120, 0], 100, (0, 1000))]

# kinetic_es = []
# potential_es = []
# rs = []
# total_es = []
# velocities = []
# accelerations = []
while 1:

    # kinetic_es.append(get_kinetic_e(particles))
    # potential_es.append(get_potential_e(particles))
    # rs.append(dist(particles[0].position, particles[1].position))
    # total_es.append(get_total_e(particles))
    # print("E: ", get_total_e(particles),
    #       "Impulse: ", get_total_impulse(particles))
    print(get_total_impulse(particles))
    # print("Impulse: ",get_total_impulse(particles))
    # print(abs(particles[0].acceleration) == abs(particles[1].acceleration))
    # velocities.append(particles[0].velocity[0])
    # accelerations.append(particles[0].acceleration[0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # fig = px.line(x=rs, y=kinetic_es, title="Energies")
            # fig.add_scatter(x=rs, y=potential_es, mode="lines")
            # fig.add_scatter(x=rs, y=total_es, mode="lines")
            # fig.show()
            # fig = px.line(x=rs, y=accelerations, title="vel, acc")
            # fig.add_scatter(x=rs, y=velocities, mode="lines")
            # fig.show()
            raise SystemExit()

    for p in particles:
        p.apply_gravity(particles)

    for p in particles:
        p.update(1)

    main_draw(screen)
    pygame.display.flip()
    clock.tick(fps)
