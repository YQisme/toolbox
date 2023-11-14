from moviepy.editor import VideoFileClip
import os

# 视频路径
video_path = "Learn React With This One Project.mp4"

# 时间节点和标题
segments = [
    ("01-Introduction", "00:00", "01:10"),
    ("02-What Is React", "01:10", "02:45"),
    ("03-Thinking In React", "02:45", "06:07"),
    ("04-Todo List Project Setup", "06:07", "10:45"),
    ("05-JSX", "10:45", "15:30"),
    ("06-React State", "15:30", "20:15"),
    ("07-Todos Logic", "20:15", "30:45"),
    ("08-Break App Into Components", "30:45", "38:15"),
    ("09-useEffect Hook", "38:15", "42.37")  # 自己设置一下视频的结束时间
]

# # 适用于时间格式为HH:MM:SS的情况
# def time_to_seconds(time_str):
#     """将时间字符串转换为秒"""
#     h, m, s = map(int, time_str.split(':'))
#     return h * 3600 + m * 60 + s
# 适用于时间格式为MM:SS的情况
def time_to_seconds(time_str):
    """将时间字符串转换为秒"""
    parts = list(map(int, time_str.split(':')))
    if len(parts) == 3:  # 如果时间包含小时
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    elif len(parts) == 2:  # 如果时间只包含分钟和秒
        return parts[0] * 60 + parts[1]
    else:
        return 0  # 返回0秒作为默认值

def split_video(segment, video_path, output_folder):
    """根据时间段剪辑视频"""
    title, start, end = segment
    start_sec = time_to_seconds(start)
    end_sec = time_to_seconds(end)
    with VideoFileClip(video_path) as video:
        new_video = video.subclip(start_sec, end_sec)
        new_video_path = os.path.join(output_folder, f"{title}.mp4")
        new_video.write_videofile(new_video_path, codec="libx264", audio_codec="aac")

# 输出文件夹
output_folder = "./output"
os.makedirs(output_folder, exist_ok=True)

# 对每个段落进行分割
for segment in segments:
    split_video(segment, video_path, output_folder)

print("视频分割完成！")
