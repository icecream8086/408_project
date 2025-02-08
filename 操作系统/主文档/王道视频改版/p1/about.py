import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 读取JSON文件，指定编码为UTF-8
with open('result.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取数据
topics = list(data.keys())

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 分行绘制热力图
for topic in topics:
    knowledge_points = data[topic]['knowledge_points']
    scores = data[topic]['scores']
    datetime = data[topic]['datetime']  # 获取时间戳数据

    df = pd.DataFrame({
        'Knowledge Points': knowledge_points,
        'Scores': scores
    })

    plt.figure(figsize=(12, 1 + len(knowledge_points) * 0.5))  # 调整高度
    heatmap_data = df.pivot_table(index=pd.Index([topic]*len(knowledge_points)), columns='Knowledge Points', values='Scores')

    sns.heatmap(heatmap_data, annot=True, cmap='Blues', fmt='g')
    plt.title(f'{topic} - Knowledge Points Scores Heatmap\n{datetime}')
    plt.xlabel('Knowledge Points')
    plt.ylabel('Topic')
    plt.xticks(rotation=45)  # 旋转X轴标签，避免重叠
    plt.yticks(rotation=0)   # 保持Y轴标签水平
    plt.tight_layout()       # 自动调整布局
    plt.show()
