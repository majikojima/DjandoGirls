from django.db import models

# Model: Maze
class Maze(models.Model):
    # ここではシンプルに迷路を文字列として保存します。
    # 迷路は、例えば'111101001'のように表現し、この場合3x3の迷路を表します（1が壁、0が通路）。
    data = models.TextField("111101001")

# Model: Player
class Player(models.Model):
    # プレーヤーの現在位置
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    # 現在プレイしている迷路
    maze = models.ForeignKey(Maze, on_delete=models.CASCADE)
    # スコア（例えば、ゴールまでの最短手数から現在の手数を引いたもの）
    score = models.IntegerField(default=0)