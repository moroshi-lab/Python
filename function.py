# def hello(name):
#     print("こんにちは",name)


# name = ["あい","です"]

# hello(name)


# def hello(name_list):
#     text = "".join(name_list)
#     print("こんにちは" + text)


# name = []
# name = []
# hello(["あい","です"])
# star_draw.py
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

# 5角星の座標を作る
def star_points():
    points = []
    outer_r = 1.0
    inner_r = 0.4
    rotation = -math.pi / 2  # 上向き

    for i in range(10):
        angle = rotation + i * math.pi / 5
        r = outer_r if i % 2 == 0 else inner_r
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        points.append((x, y))
    points.append(points[0])  # 最初の点を最後にも追加
    return points

pts = star_points()
xs = [p[0] for p in pts]
ys = [p[1] for p in pts]

# 描画準備
fig, ax = plt.subplots(figsize=(4,4))
line, = ax.plot([], [], 'b')  # 線
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.axis('off')

# アニメーション更新関数
def update(num):
    line.set_data(xs[:num+1], ys[:num+1])
    return line,

ani = FuncAnimation(fig, update, frames=len(xs), interval=300, blit=True)

plt.show()
