import pygameclass Spring:    def __init__(self, screen, color: tuple, k: float, rest_length: int, point1, point2, radius) -> None:        self.screen = screen        self.color = color        self.k = k        self.rest_length = rest_length        self.a = point1        self.b = point2        self.radius = radius    def update(self) -> None:        force = self.b.position - self.a.position        x = force.magnitude() - self.rest_length        force = force.normalize()        force *= (self.k * x)        self.a.apply_force(force)        force *= -1        self.b.apply_force(force)    def show(self) -> None:        pygame.draw.line(self.screen, self.color, (self.a.position.x, self.a.position.y), (self.b.position.x, self.b.position.y), self.radius)