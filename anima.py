#引入函式庫
from vpython import *
import math
import matplotlib.pyplot as plt


# 用戶輸入
mass = float(input('質量 (kg) (限制數值在0.1到0.25之間): '))  # 質量
amplitude = float(input('初始震幅 (m) (限制數值在0.01到0.05之間): '))  # 初震幅
thickness = float(input('銅板厚度 (mm) (限制數值在2到10之間): '))  # 銅板厚度
height = float(input('初平衡點距離銅板高度 (m) (限制數值在0.03到0.08之間，必須大於初始震幅): '))  # 初平衡點距離銅板高度
spring_constant = float(input('彈力常數 (N/m) (限制數值在10到25之間): '))  # 彈力常數


# 驗證輸入值是否在範圍內
if mass > 0.25 or mass < 0.1:
   print('輸入數值不在預設範圍')
elif amplitude > 0.05 or amplitude < 0.01:
   print('輸入數值不在預設範圍')
elif thickness > 10 or thickness < 2:
   print('輸入數值不在預設範圍')
elif height > 0.08 or height < 0.03:
   print('輸入數值不在預設範圍')
elif spring_constant > 25 or spring_constant < 10:
   print('輸入數值不在預設範圍')
elif height <= amplitude:
   print('輸入數值不在預設範圍')
else:
   # 計算系統參數
   T = (2 * math.pi * (mass / spring_constant) ** 0.5)  # 震盪週期公式
   k = 0.00000299634  # 固定的比例常數
   b = k * (height ** -3) * (mass ** -0.75) * (math.e ** (-2.63 / thickness))  # 計算阻尼係數


   # 動畫效果顯著化
   height = 5 * height  # 放大高度以便於觀察動畫效果
   amplitude = 5 * amplitude  # 放大震幅以便於觀察動畫效果


   # VPython 場景建立
   scene = canvas(title="Damped Oscillation Animation",
                  width=800, height=600,
                  center=vector(0, height / 2 + 1, 0),  # 將視角中心置於彈簧和物體運動範圍
                  )


   # 創建物件與結構
   copper_plate = box(pos=vector(0, 0, 0), size=vector(1, 0.02, 1), color=color.orange)  # 銅板
   horizontal_bar = box(pos=vector(0, 1, 0), size=vector(1, 0.02, 0.02), color=color.gray(0.6))  # 橫槓
   object = box(pos=vector(0, 1 - 0.5, 0), size=vector(0.1, 0.1, 0.1), color=color.gray(0.8), make_trail=False)  # 振盪物體
   spring = helix(pos=horizontal_bar.pos,
                  axis=object.pos - horizontal_bar.pos,
                  radius=0.05, coils=20, thickness=0.01, color=color.gray(0.6))  # 彈簧


   # 時間步長
   dt = 0.01  # 每次更新的時間間隔
   time = 0  # 初始時間


   # 創建 Matplotlib 圖表
   fig, ax = plt.subplots(figsize=(8, 5))  # 初始化圖表
   ax.set_ylim(-amplitude, amplitude)  # 設定位移範圍
   ax.set_xlim(0, 15)  # 設定時間範圍
   ax.set_title('Y-T Plot')  # 設置圖表標題
   ax.set_xlabel('Time (s)')  # 橫軸標籤
   ax.set_ylabel('Displacement (m)')  # 縱軸標籤
   line, = ax.plot([], [], lw=2)  # 初始化圖表曲線


   # 位移函數
   def get_amplitude(time):
       return amplitude * math.e ** (-b * time) * math.cos(2 * math.pi * time / T)  # 計算某時刻的位移


   # 動畫
   times = []  # 用於儲存時間數據
   displacements = []  # 用於儲存位移數據
   while time <= 15:  # 模擬15秒的運動
       rate(100)  # 每秒更新100次


       y = get_amplitude(time)  # 計算當前位移
       object.pos = vector(0, 1 - 0.5 + y, 0)  # 更新物體位置
       spring.axis = object.pos - spring.pos  # 更新彈簧的軸向


       times.append(time)  # 儲存當前時間
       displacements.append(y)  # 儲存當前位移


       # 更新 Matplotlib 的 Y-T 圖
       line.set_data(times, displacements)


       time += dt  # 更新時間


   plt.show()  # 顯示圖表