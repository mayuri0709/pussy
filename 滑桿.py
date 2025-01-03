#引入函式庫
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import sys
# Streamlit 標題
st.header("從阻尼震盪到數據預測：銅金屬渦電流與磁阻尼機制的動力學研究")  # 顯示整個頁面的主標題，說明研究主題


# Streamlit 敘述
st.subheader("阻尼震盪軌跡預測")  # 顯示子標題，介紹第一部分的內容
st.text("不考慮震幅過大導致物體與銅板產生碰撞的情況。")  # 提供額外說明，避免誤解模擬範圍
# 使用者輸入
mass = st.slider('質量 (kg)', min_value=0.1, max_value=0.25, value=0.1, step=0.01)  # 透過滑桿讓使用者選擇物體的質量
amplitude = st.slider('原始震幅 (m)', min_value=0.01, max_value=0.1, value=0.01, step=0.01)  # 透過滑桿設定初始震幅
height = st.slider('高度 (m)', min_value=0.01, max_value=0.08, value=0.01, step=0.01)  # 透過滑桿選擇物體與銅板的初始距離
spring_constant = st.slider('彈力常數 (N/m)', min_value=10, max_value=20, value=10, step=1)  # 設定彈簧的彈力常數
thickness= st.slider('銅板厚度 (mm)', min_value=2, max_value=10, value=2, step=1)  # 設定銅板厚度
if st.button("執行 anima.py 動畫"):
    try:
        anima()
        st.success("動畫執行完成！")
    except Exception as e:
        st.error(f"執行 anima.py 時發生錯誤！")
        st.text("錯誤訊息：")

# 定義周期與阻尼系數
T = (2 * math.pi * (mass / spring_constant) ** 0.5)  # 根據質量和彈簧常數計算系統的振盪周期


k = 0.00000299634  # 固定比例常數，用於計算阻尼係數
b = k * (height ** -3) * (mass ** -0.75) * (np.e ** (-2.63 / thickness))  # 計算阻尼係數，考慮高度、質量與厚度


# 圖表生成
fig1, ax1 = plt.subplots(figsize=(8, 5))  # 初始化第一個圖表，設置大小
ax1.set_title('Y-T Plot')  # 設置圖表標題，表示位移隨時間變化
ax1.set_xlabel('Time(s)')  # 設置橫軸標籤
ax1.set_ylabel('Displacement (m)')  # 設置縱軸標籤
ax1.grid(True)  # 顯示網格線


# 計算位移
time_values = np.linspace(0, 15, 1500)  # 時間點範圍，模擬15秒的運動
# 根據位移公式計算位移值
displacement_values = amplitude * np.exp(-b * time_values) * np.cos(2 * np.pi * time_values / T)
ax1.plot(time_values, displacement_values, label="Displacement")  # 在圖表中繪製位移曲線，並設置標籤
ax1.legend()  # 添加圖例


# 展示圖表
st.pyplot(fig1)  # 使用 Streamlit 在網頁上顯示第一個圖表


# 使用者輸入 - 力學能衰減
st.subheader("力學能衰減-銅板厚度")  # 顯示子標題，介紹第二部分內容


# 再次定義阻尼係數公式
mass_1 = st.slider('質量 (kg)', min_value=0.1, max_value=0.25, value=0.1, step=0.01, key='mass_1')  # 質量滑桿，影響力學能計算
amplitude_1 = st.slider('原始震幅 (m)', min_value=0.01, max_value=0.1, value=0.01, step=0.01, key='amplitude_1')  # 初始震幅滑桿
height_1 = st.slider('高度 (m)', min_value=0.01, max_value=0.08, value=0.01, step=0.01, key='height_1')  # 高度滑桿
spring_constant_1 = st.slider('彈力常數 (N/m)', min_value=10, max_value=20, value=10, step=1, key='spring_constant_1')  # 彈簧常數滑桿
thicknesses_1 = [2, 4, 6, 8, 10]  # 不同的銅板厚度值，用於比較


# 周期與阻尼係數
T = lambda mass_1: (2 * math.pi * (mass_1 / spring_constant_1) ** 0.5)  # 動態計算振盪周期
b = lambda thickness_1, mass_1, height_1: k * (height_1 ** -3) * (mass_1 ** -0.75) * (np.e ** (-2.63 / thickness_1))  # 動態計算阻尼係數


# 初始化圖表
fig2, ax2 = plt.subplots(figsize=(8, 6))  # 初始化第二個圖表


for thickness_1 in thicknesses_1:  # 遍歷不同的銅板厚度值
   b_value = b(thickness_1, mass_1, height_1)  # 計算當前厚度的阻尼係數
   # 根據力學公式計算位移、速度與力學能
   displacement_values = amplitude_1 * np.exp(-b_value * time_values) * np.cos(2 * np.pi * time_values / T(mass_1))
   velocity_values = (
       amplitude_1 * np.exp(-b_value * time_values) *
       (-b_value * np.cos(((spring_constant_1 / mass_1) ** 0.5) * time_values) +
        ((spring_constant_1 / mass_1) ** 0.5) * np.sin(((spring_constant_1 / mass_1) ** 0.5) * time_values))
   )
   energy_k = 0.5 * mass_1 * (velocity_values ** 2)  # 動能
   elongation = (mass_1 * 9.8) / spring_constant_1  # 彈簧伸長量
   energy_s = 0.5 * spring_constant_1 * (elongation - displacement_values) ** 2  # 彈性勢能
   energy_g = mass_1 * 9.8 * (height_1 + displacement_values)  # 重力勢能
   energy_sum = energy_k + energy_s + energy_g  # 總力學能


   ax2.plot(time_values, energy_sum, label=f'Thickness = {thickness_1} mm')  # 在圖表中繪製曲線，標註當前厚度


# 設置圖表
ax2.set_xlabel('Time (s)')  # 設置橫軸標籤
ax2.set_ylabel('Mechanical Energy (J)')  # 設置縱軸標籤
ax2.set_title('Simulated Dynamics of Mechanical Energy Attenuation at Varying Thicknesses')  # 設置圖表標題
ax2.legend()  # 顯示圖例
ax2.grid(True)  # 顯示網格線
st.pyplot(fig2)  # 使用 Streamlit 在網頁上顯示第二個圖表
mass = float(input('質量 (kg) (限制數值在0.1到0.25之間): '))  # 質量
amplitude = float(input('初始震幅 (m) (限制數值在0.01到0.05之間): '))  # 初震幅
thickness = float(input('銅板厚度 (mm) (限制數值在2到10之間): '))  # 銅板厚度
height = float(input('初平衡點距離銅板高度 (m) (限制數值在0.03到0.08之間，必須大於初始震幅): '))  # 初平衡點距離銅板高度
spring_constant = float(input('彈力常數 (N/m) (限制數值在10到25之間): '))  # 彈力常數

def anima() :
# 驗證輸入值是否在範圍內
    if mass > 0.25 or mass < 0.1:
       st.error('輸入數值不在預設範圍')
    elif amplitude > 0.05 or amplitude < 0.01:
       st.error('輸入數值不在預設範圍')
    elif thickness > 10 or thickness < 2:
       st.error('輸入數值不在預設範圍')
    elif height > 0.08 or height < 0.03:
       st.error('輸入數值不在預設範圍')
    elif spring_constant > 25 or spring_constant < 10:
       st.error('輸入數值不在預設範圍')
    elif height <= amplitude:
       st.error('輸入數值不在預設範圍')
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
