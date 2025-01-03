import streamlit as st
import numpy as np
import plotly.graph_ob as go

# Streamlit 標題
st.title("Damped Oscillation Animation")
st.markdown("This app demonstrates a damped oscillation using Plotly's animation capabilities.")

# 用戶輸入
mass = st.number_input("Mass (kg, 0.1 to 0.25):", min_value=0.1, max_value=0.25, value=0.2, step=0.01)
amplitude = st.number_input("Initial Amplitude (m, 0.01 to 0.05):", min_value=0.01, max_value=0.05, value=0.03, step=0.001)
thickness = st.number_input("Copper Plate Thickness (mm, 2 to 10):", min_value=2, max_value=10, value=5, step=1)
height = st.number_input("Initial Equilibrium Height (m, 0.03 to 0.08):", min_value=0.03, max_value=0.08, value=0.05, step=0.001)
spring_constant = st.number_input("Spring Constant (N/m, 10 to 25):", min_value=10, max_value=25, value=15, step=1)

# 驗證輸入
if height <= amplitude:
    st.error("Height must be greater than the amplitude!")
else:
    # 計算參數
    T = 2 * np.pi * np.sqrt(mass / spring_constant)
    k = 0.00000299634
    b = k * (height ** -3) * (mass ** -0.75) * (np.exp(-2.63 / thickness))

    # 計算時間序列和位移
    time_values = np.linspace(0, 15, 500)
    displacement_values = amplitude * np.exp(-b * time_values) * np.cos(2 * np.pi * time_values / T)

    # 創建 Plotly 動畫
    fig = go.Figure()
    for i, t in enumerate(time_values):
        fig.add_trace(
            go.Scatter(
                x=[0],
                y=[displacement_values[i]],
                mode="markers",
                marker=dict(size=12, color="red"),
                name=f"Time {t:.2f}s"
            )
        )

    # 更新圖表配置
    fig.update_layout(
        title="Damped Oscillation Animation",
        xaxis=dict(range=[-0.1, 0.1], title="Position"),
        yaxis=dict(range=[-amplitude, amplitude], title="Displacement"),
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(label="Play", method="animate", args=[None, dict(frame=dict(duration=50, redraw=True))]),
                    dict(label="Pause", method="animate", args=[[None], dict(frame=dict(duration=0, redraw=False))]),
                ],
            )
        ],
    )

    # 設定動畫幀
    frames = [go.Frame(data=[go.Scatter(x=[0], y=[displacement_values[i]], mode="markers")]) for i in range(len(time_values))]
    fig.frames = frames

    # 顯示動畫
    st.plotly_chart(fig, use_container_width=True)
