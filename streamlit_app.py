import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd

# Tạo hàm mô phỏng tung đồng xu
def simulate_coin_toss(num_tosses):
    outcomes = {'Sấp': 0, 'Ngửa': 0}
    for _ in range(num_tosses):
        outcome = 'Sấp' if random.random() < 0.5 else 'Ngửa'
        outcomes[outcome] += 1
    return outcomes

# Tạo hàm mô phỏng tung xúc xắc
def simulate_dice_roll(num_rolls):
    outcomes = {i: 0 for i in range(1, 7)}
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        outcomes[roll] += 1
    return outcomes

# Tạo hàm mô phỏng quay kim trên bìa nhiều màu
colors = [
        'Đỏ', 'Xanh dương', 'Xanh lá', 'Vàng', 'Cam', 'Hồng', 'Tím',
        'Nâu', 'Trắng', 'Xám', 'Bạc', 'Vàng nhạt', 'Xanh ngọc',
        'Hồng phấn', 'Xanh lục', 'Be', 'Đỏ đô', 'Xanh biển', 'Tím than', 'Đen'
    ]

colors_english = [
    'red', 'blue', 'green', 'yellow', 'orange', 'pink', 'purple',
    'brown', 'white', 'gray', 'silver', 'light yellow', 'cyan',
    'light pink', 'lime', 'beige', 'maroon', 'navy', 'dark purple', 'black'
]

def simulate_spin_wheel(num_spins, num_path):
    segments = colors[:num_path]
    outcomes = {segment: 0 for segment in segments}
    for _ in range(num_spins):
        outcome = random.choice(segments)
        outcomes[outcome] += 1
    return outcomes

# Hàm vẽ sơ đồ cột và sơ đồ tròn
def plot_results(outcomes, num):
    labels = list(outcomes.keys())
    values = list(outcomes.values())
    
    # Sơ đồ cột
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Vẽ biểu đồ cột
    bars = ax1.bar(labels, values)

    # Thêm số liệu trên đầu mỗi cột
    for bar in bars:
        yval = bar.get_height()  # Lấy chiều cao (giá trị) của cột
        ax1.text(bar.get_x() + bar.get_width()/2, yval, f'{yval}', ha='center', va='bottom')

    # Thêm tiêu đề
    ax1.set_title('Biểu đồ cột')

    # Sơ đồ tròn
    # Tạo biểu đồ tròn
    mau = colors_english[:num]
    ax2.pie(values, labels=labels, colors = mau, autopct='%1.1f%%')

    # Thêm tiêu đề
    ax2.set_title('Biểu đồ tròn')

    st.pyplot(fig)

# Giao diện Streamlit
st.title("Mô Phỏng Xác Suất")

# Lựa chọn kiểu mô phỏng
simulation_type = st.selectbox("Chọn loại mô phỏng", 
                               ["Tung đồng xu", "Gieo xúc xắc", "Quay kim trên bìa màu"])

# Nhập số lần mô phỏng
num_trials = st.number_input("Số lần mô phỏng", min_value=1, value=10, step=1)
if simulation_type == "Quay kim trên bìa màu":
        num_path = st.number_input("Số tấm bìa được chọn", min_value=1, max_value=20, step=1)

# Nút mô phỏng
if st.button("Mô phỏng"):
    if simulation_type == "Tung đồng xu":
        outcomes = simulate_coin_toss(num_trials)
        num = 2
    elif simulation_type == "Tung xúc xắc":
        outcomes = simulate_dice_roll(num_trials)
        num = 6
    elif simulation_type == "Quay kim trên bìa màu":
        outcomes = simulate_spin_wheel(num_trials, num_path)
        num = num_path

    # Hiển thị kết quả dưới dạng bảng
    df = pd.DataFrame(list(outcomes.items()), columns=['Kết quả có thể', 'Số lần'])
    st.write("Kết quả mô phỏng dưới dạng bảng:")
    st.table(df)

    # Vẽ sơ đồ cột và sơ đồ tròn
    plot_results(outcomes, num)
