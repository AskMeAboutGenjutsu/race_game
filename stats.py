class Stats:

    def __init__(self):
        self.run_game = True
        self.reset_stats()
        self.get_high_score()

    def reset_stats(self):
        self.user_car_left = 3
        self.score = 0

    def get_high_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = int(f.readline())
        except FileNotFoundError:
            self.high_score = 0