import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime as dt
import os
import argparse

def plot_heatmaps_from_json(json_path):
    # 确保路径是正确的格式
    json_path = os.path.normpath(json_path)
    
    # 读取JSON文件，指定编码为UTF-8
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 提取数据
    topics = list(data.keys())

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
    plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

    # 分行绘制热力图
    for topic in topics:
        knowledge_points = data[topic]['knowledge_points']
        scores = data[topic]['scores']
        datetime_str = data[topic]['datetime']  # 获取时间戳数据

        # 处理时间
        if '-' in datetime_str:
            datetime_display = datetime_str  # 如果包含'-'，直接显示
        else:
            timestamp = int(datetime_str)
            datetime_display = dt.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  # 转换为人类可读的时间格式

        df = pd.DataFrame({
            'Knowledge Points': knowledge_points,
            'Scores': scores
        })

        plt.figure(figsize=(12, 1 + len(knowledge_points) * 0.5))  # 调整高度
        heatmap_data = df.pivot_table(index=pd.Index([topic]*len(knowledge_points)), columns='Knowledge Points', values='Scores')

        sns.heatmap(heatmap_data, annot=True, cmap='Blues', fmt='g')
        plt.title(f'{topic} - Knowledge Points Scores Heatmap\n{datetime_display}')
        plt.xlabel('Knowledge Points')
        plt.ylabel('Topic')
        plt.xticks(rotation=45)  # 旋转X轴标签，避免重叠
        plt.yticks(rotation=0)   # 保持Y轴标签水平
        plt.tight_layout()       # 自动调整布局
        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate heatmaps from JSON data.')
    parser.add_argument('json_path', type=str, help='Path to the JSON file.')
    args = parser.parse_args()
    
    plot_heatmaps_from_json(args.json_path)