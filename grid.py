class Grid:
    def __init__(self, width, height, obstacle_density=.2):
        self.width = width
        self.height = height
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = np.array([[0 for _ in range(self.width)] for _ in range(self.height)])

        for row in range(self.height):
            for col in range(self.width):
                if random



