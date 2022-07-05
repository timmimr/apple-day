class Stats():
    """инициализирует статистику"""
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        self.high_score = 0
        with open("config.txt", "r") as f:
            self.high_score = int(f.readline())
    """статистика изменяющаяся во время игры"""
    def reset_stats(self):
        self.guns_left = 3
        self.score = 0

        
    
