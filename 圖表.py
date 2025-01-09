import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from sklearn.linear_model import LinearRegression
import streamlit as st
html_code =f'''
<div id="glowscript" class="glowscript">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link type="text/css" href="https://www.glowscript.org/css/redmond/2.1/jquery-ui.custom.css" rel="stylesheet" />
<link type="text/css" href="https://www.glowscript.org/css/ide.css" rel="stylesheet" />
<script type="text/javascript" src="https://www.glowscript.org/lib/jquery/2.1/jquery.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/lib/jquery/2.1/jquery-ui.custom.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/package/glow.3.2.min.js"></script>
<script type="text/javascript" src="https://www.glowscript.org/package/RSrun.3.2.min.js"></script>
<script type="text/javascript"><!--//--><![CDATA[//><!--

// START JAVASCRIPT
;(function() {;
var ρσ_modules = {};
ρσ_modules.pythonize = {};

(function(){
    function strings() {
        var string_funcs, exclude, name;
        string_funcs = set("capitalize strip lstrip rstrip islower isupper isspace lower upper swapcase center count endswith startswith find rfind index rindex format join ljust rjust partition rpartition replace split rsplit splitlines zfill".split(" "));
        if (!arguments.length) {
            exclude = (function(){
                var s = ρσ_set();
                s.jsset.add("split");
                s.jsset.add("replace");
                return s;
            })();
        } else if (arguments[0]) {
            exclude = Array.prototype.slice.call(arguments);
        } else {
            exclude = null;
        }
        if (exclude) {
            string_funcs = string_funcs.difference(set(exclude));
        }
        var ρσ_Iter0 = string_funcs;
        ρσ_Iter0 = ((typeof ρσ_Iter0[Symbol.iterator] === "function") ? (ρσ_Iter0 instanceof Map ? ρσ_Iter0.keys() : ρσ_Iter0) : Object.keys(ρσ_Iter0));
        for (var ρσ_Index0 of ρσ_Iter0) {
            name = ρσ_Index0;
            (ρσ_expr_temp = String.prototype)[(typeof name === "number" && name < 0) ? ρσ_expr_temp.length + name : name] = (ρσ_expr_temp = ρσ_str.prototype)[(typeof name === "number" && name < 0) ? ρσ_expr_temp.length + name : name];
        }
    };
    if (!strings.__module__) Object.defineProperties(strings, {
        __module__ : {value: "pythonize"}
    });

    ρσ_modules.pythonize.strings = strings;
})();
async function __main__() {
"use strict";
    var display = canvas;
    var scene = canvas();

    function input(arg) {
    	arg = arg || {}
    	if (arg.prompt !== undefined && arg.prompt != '') return prompt(arg.prompt)
    	else if (typeof arg === 'string') return prompt(arg)
    	else return prompt()
    }

    var version, print, arange, __name__, type, ρσ_ls, mass, amplitude, thickness, height, spring_constant, lasted, speed, dt, T, k, b, scene, graph1, displacement_curve, copper_plate, horizontal_bar, object, spring, time, times, displacements, shift, y;
    version = ρσ_list_decorate([ "3.2", "glowscript" ]);
    Array.prototype['+'] = function(r) {return this.concat(r)}
    Array.prototype['*'] = function(r) {return __array_times_number(this, r)}
    window.__GSlang = "vpython";
    print = GSprint;
    arange = range;
    __name__ = "__main__";
    type = pytype;
    var strings = ρσ_modules.pythonize.strings;

    strings();
    sleep(.1);
    "3";
    mass = float(input("質量 (kg) (限制數值在0.1到0.25之間): "));
    (await sleep(.1));
    "4";
    amplitude = float(input("初始震幅 (m) (限制數值在0.01到0.05之間): "));
    (await sleep(.1));
    "5";
    thickness = float(input("銅板厚度 (mm) (限制數值在2到10之間): "));
    (await sleep(.1));
    "6";
    height = float(input("初平衡點距離銅板高度 (m) (限制數值在0.03到0.08之間，必須大於初始震幅): "));
    (await sleep(.1));
    "7";
    spring_constant = float(input("彈力常數 (N/m) (限制數值在10到25之間): "));
    (await sleep(.1));
    "8";
    lasted = float(input("動畫持續時間(動畫、圖表內時間）(sec)"));
    (await sleep(.1));
    "9";
    speed = float(input("位置每秒（真實時間）更新次數（hz)，預設100"));
    (await sleep(.1));
    "10";
    dt = float(input("每更新一次，記錄時刻（動畫、圖表內時間）間隔(sec)，預設0.01"));
    "12";
    if (mass[">"](.25) || mass["<"](.1)) {
        "13";
        print("輸入數值不在預設範圍");
        "14";
    } else if (amplitude[">"](.05) || amplitude["<"](.01)) {
        "15";
        print("輸入數值不在預設範圍");
        "16";
    } else if (thickness[">"](10) || thickness["<"](2)) {
        "17";
        print("輸入數值不在預設範圍");
        "18";
    } else if (height[">"](.08) || height["<"](.03)) {
        "19";
        print("輸入數值不在預設範圍");
        "20";
    } else if (spring_constant[">"](25) || spring_constant["<"](10)) {
        "21";
        print("輸入數值不在預設範圍");
        "22";
    } else if (height["<="](amplitude)) {
        "23";
        print("輸入數值不在預設範圍");
        "24";
    } else {
        "26";
        T = 2["*"](pi)["*"](Math.pow((mass["/"](spring_constant)), .5));
        "27";
        k = 299634e-11;
        "28";
        b = k["*"](Math.pow(height, 3["-u"]()))["*"](Math.pow(mass, .75["-u"]()))["*"](exp(1["-u"]()["*"](2.63)["/"](thickness)));
        "30";
        height = 5["*"](height);
        "31";
        amplitude = 5["*"](amplitude);
        "33";
        scene = ρσ_interpolate_kwargs.call(this, canvas, [ρσ_desugar_kwargs({title: "Damped Oscillation Animation", width: 750, height: 450, center: vector(0, height["/"](2)["+"](.5), 0), align: "right"})]);
        "38";
        graph1 = ρσ_interpolate_kwargs.call(this, graph, [ρσ_desugar_kwargs({title: "物體位置隨時間的變化", width: 700, height: 450, xtitle: "Time (s)", ytitle: "高度(m)", align: "left", fast: false})]);
        "39";
        displacement_curve = ρσ_interpolate_kwargs.call(this, gcurve, [ρσ_desugar_kwargs({color: color.blue, label: "軌跡"})]);
        "41";
        copper_plate = ρσ_interpolate_kwargs.call(this, box, [ρσ_desugar_kwargs({pos: vector(0, 0, 0), size: vector(1, .02, 1), color: color.orange})]);
        "42";
        horizontal_bar = ρσ_interpolate_kwargs.call(this, box, [ρσ_desugar_kwargs({pos: vector(0, 1, 0), size: vector(1, .02, .02), color: color.gray(.6)})]);
        "43";
        object = ρσ_interpolate_kwargs.call(this, box, [ρσ_desugar_kwargs({pos: vector(0, 1["-"](1["*"](.5)), 0), size: vector(.1, .1, .1), color: color.gray(.8), make_trail: true})]);
        "44";
        spring = ρσ_interpolate_kwargs.call(this, helix, [ρσ_desugar_kwargs({pos: horizontal_bar.pos, axis: object.pos["-"](1["*"](horizontal_bar.pos)), radius: .05, coils: 20, thickness: .01, color: color.gray(.6)})]);
        "50";
        time = 0;
    }
    "52";
    async function get_amplitude(time) {
        "53";
        return amplitude["*"](exp(1["-u"]()["*"](b)["*"](time)))["*"](cos(2["*"](pi)["*"](time)["/"](T)));
    };
    if (!get_amplitude.__argnames__) Object.defineProperties(get_amplitude, {
        __argnames__ : {value: ["time"]},
        __module__ : {value: null}
    });

    "55";
    times = ρσ_list_decorate([]);
    "56";
    displacements = ρσ_list_decorate([]);
    "57";
    while (time["<="](lasted)) {
        "58";
        (await rate(speed));
        "59";
        shift = .1["*"](time);
        "61";
        y = (await get_amplitude(time));
        "62";
        object.pos = vector(shift, 1["-"](1["*"](.5))["+"](y), 0);
        "63";
        spring.pos.x = shift;
        "64";
        spring.axis = object.pos["-"](1["*"](spring.pos))["+"](vector(0, .05, 0));
        "65";
        copper_plate.pos.x = shift;
        "66";
        horizontal_bar.pos.x = shift;
        "67";
        scene.center.x = shift;
        "68";
        times.append(time);
        "69";
        displacements.append(y);
        "71";
        displacement_curve.plot(time, y);
        "72";
        time=time["+"](dt);
    }
};
if (!__main__.__module__) Object.defineProperties(__main__, {
    __module__ : {value: null}
});

;$(function(){ window.__context = { glowscript_container: $("#glowscript").removeAttr("id") }; __main__() })})()
// END JAVASCRIPT

//--><!]]></script>
</div>
'''
# Streamlit 應用程式
st.title("阻尼振盪分析")  # 應用程式標題

# 上傳檔案
uploaded_file = st.file_uploader("上傳您的 CSV 檔案", type=["csv"])  # 提示用戶上傳檔案
st.text("或者讀取線上csv數據")

# 輸入 Google Sheets 的 CSV 下載鏈接
sheet_url = st.text_input(
    "請輸入 CSV 下載鏈接:", 
)
if uploaded_file or sheet_url:
    # 讀取資料
    try:
        data = pd.read_csv(uploaded_file)
    except:
        data = pd.read_csv(sheet_url)
    st.write("### 上傳的資料")  # 顯示上傳的資料標題
    st.dataframe(data)  # 顯示資料表

    # 提取欄位
    time = data['t 10']  # 時間欄位
    amplitude = data['y 10']  # 振幅欄位

    # 峰值檢測
    peaks, _ = find_peaks(amplitude)
    peak_times = time[peaks].values.reshape(-1, 1)  # 峰值時間
    peak_amplitudes = amplitude[peaks]  # 峰值振幅

    # 計算峰值振幅的自然對數
    log_peak_amplitudes = np.log(peak_amplitudes)

    # 建立峰值資料的 DataFrame
    peak_data = pd.DataFrame({
        '峰值時間': peak_times.flatten(),
        '峰值振幅': peak_amplitudes,
        'ln(峰值振幅)': log_peak_amplitudes
    })

    # 顯示峰值資料
    st.write("### Peak Data with Natural Logarithm")  # 顯示表格標題
    st.dataframe(peak_data)  # 顯示資料表

    # 繪製 振幅 vs 時間 圖
    st.write("### Amplitude vs Time")  # 圖表標題
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.plot(time, amplitude, label='Damped Oscillation')  # 繪製阻尼振盪曲線
    ax1.plot(peak_times.flatten(), peak_amplitudes, 'ro', label='Detected Peaks')  # 繪製峰值
    ax1.set_title('Amplitude vs Time')  # 圖表總標題
    ax1.set_xlabel('Time (s)')  # x 軸標題
    ax1.set_ylabel('Amplitude (m)')  # y 軸標題
    ax1.legend()  # 顯示圖例
    ax1.grid()  # 顯示格線
    st.pyplot(fig1)  # 顯示圖表

    # 線性回歸
    model = LinearRegression()
    model.fit(peak_times, log_peak_amplitudes)  # 訓練回歸模型
    slope = model.coef_[0]  # 斜率
    intercept = model.intercept_  # 截距
    log_amplitude_pred = model.predict(peak_times)  # 預測值
    r_squared = model.score(peak_times, log_peak_amplitudes)  # R 平方值

    # 繪製 ln(峰值振幅) vs 時間 圖
    st.write("### Natural Logarithm of Peak Amplitude vs Time")  # 圖表標題
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.scatter(peak_times, log_peak_amplitudes, color='red', label='Data (Natural Logarithm)')  # 資料點
    ax2.plot(peak_times, log_amplitude_pred, color='blue', label=f'Fit: ln(A) = {slope:.4f}t + {intercept:.4f}')  # 回歸線
    ax2.set_title('Natural Logarithm of Peak Amplitude vs Time')  # 圖表總標題
    ax2.set_xlabel('Time (s)')  # x 軸標題
    ax2.set_ylabel('ln(Peak Amplitude)')  # y 軸標題
    ax2.legend()  # 顯示圖例
    ax2.grid()  # 顯示格線

    # 顯示 R 平方和回歸方程
    text_x = peak_times.mean()
    text_y = log_amplitude_pred.mean()
    ax2.text(text_x + 3, text_y, f'ln(A) = {slope:.5f}t + {intercept:.5f}', fontsize=12)  # 顯示方程
    ax2.text(text_x + 3, text_y - 0.1, f'$R^2$ = {r_squared:.4f}', fontsize=12)  # 顯示 R 平方值

    st.pyplot(fig2)  # 顯示圖表

    # 顯示回歸結果
    st.write("### 回歸結果")  # 回歸結果標題
    st.write(f"斜率 (衰減率): {slope:.5f}")  # 顯示斜率
    st.write(f"截距: {intercept:.5f}")  # 顯示截距
    st.write(f"R 平方值: {r_squared:.4f}")  # 顯示 R 平方值
