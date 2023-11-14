import re
import os

def parse_time(time_str):
    """将时间字符串转换为秒数"""
    parts = re.split('[:]', time_str)
    h, m = map(int, parts[0:2])
    s_ms_parts = parts[2].split(',')
    s = int(s_ms_parts[0])
    ms = int(s_ms_parts[1]) if len(s_ms_parts) > 1 else 0
    return h * 3600 + m * 60 + s + ms / 1000.0

def format_time(seconds):
    """将秒数转换回时间字符串格式"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def time_in_range(start, end, check_time):
    """检查时间是否在给定范围内"""
    return start <= check_time <= end

def adjust_time(line, offset):
    """调整时间戳，减去开始时间的偏移量"""
    times = re.split(' --> ', line)
    start_time = format_time(parse_time(times[0]) - offset)
    end_time = format_time(parse_time(times[1]) - offset)
    return f"{start_time} --> {end_time}\n"

def split_srt(filename, segments, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for segment in segments:
        title, start, end = segment
        start_sec = parse_time(start)
        end_sec = parse_time(end)
        output_file = os.path.join(output_folder, f'{title}.srt')

        with open(output_file, 'w', encoding='utf-8') as new_file:
            inside_segment = False
            for line in lines:
                if re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line):
                    times = re.split(' --> ', line.strip())
                    start_time = parse_time(times[0].split(',')[0])
                    end_time = parse_time(times[1].split(',')[0])
                    inside_segment = time_in_range(start_sec, end_sec, start_time) and time_in_range(start_sec, end_sec, end_time)

                    if inside_segment:
                        line = adjust_time(line, start_sec)

                if inside_segment:
                    new_file.write(line)

# 时间节点和标题
segments = [
    ("01-Intro", "00:00:00", "00:01:13"),
    ("02-Python in Context", "00:01:13", "00:06:20"),
    ("03-Installing Python", "00:06:20", "00:14:20"),
    ("04-Installing a code editor", "00:14:20", "00:27:57"),
    ("05-How code is executed", "00:27:57", "00:33:21"),
    ("06-Math operations", "00:33:21", "00:41:52"),
    ("07-Variables", "00:41:52", "00:56:37"),
    ("08-Functions", "00:56:37", "01:03:22"),
    ("09-Methods", "01:03:22", "01:18:11"),
    ("10-Returning values", "01:18:11", "01:24:23"),
    ("11-Comments", "01:24:23", "01:29:38"),
    ("12-More on the order of execution", "01:29:38", "01:37:53"),
    ("13-Datatypes intro", "01:37:53", "01:42:15"),
    ("14-Numbers (integers + floating point numbers)", "01:42:15", "01:48:09"),
    ("15-Strings", "01:48:09", "02:08:45"),
    ("16-Lists and tuples", "02:08:45", "02:26:45"),
    ("17-Slicing", "02:26:45", "02:39:26"),
    ("18-Unpacking", "02:39:26", "02:44:03"),
    ("19-Strings, tuples and lists", "02:44:03", "02:52:54"),
    ("20-Dictionaries", "02:52:54", "03:04:35"),
    ("21-Sets", "03:04:35", "03:18:26"),
    ("22-Booleans", "03:18:26", "03:31:39"),
    ("23-Other datatypes", "03:31:39", "03:33:32"),
    ("24-Flow intro", "03:33:32", "03:37:26"),
    ("25-Simple if statements", "03:37:26", "03:50:34"),
    ("26-Complex if statements", "03:50:34", "04:06:10"),
    ("27-Match case", "04:06:10", "04:14:49"),
    ("28-While loops", "04:14:49", "04:27:29"),
    ("29-For loops", "04:27:29", "04:42:42"),
    ("30-Flow + linebreaks", "04:42:42", "04:50:22"),
    ("31-Function intro", "04:50:22", "05:04:18"),
    ("32-Parameters", "05:04:18", "05:16:37"),
    ("33-More on parameters", "05:16:37", "05:27:30"),
    ("34-Scope", "05:27:30", "05:44:47"),
    ("35-Lambda functions", "05:44:47", "05:50:38"),
    ("36-Documenting functions", "05:50:38", "05:57:03"),
    ("37-Data intro", "05:57:03", "05:57:51"),
    ("38-Better for loops", "05:57:51", "06:12:46"),
    ("39-List comprehension", "06:12:46", "06:30:56"),
    ("40-Other comprehensions", "06:30:56", "06:37:49"),
    ("41-Sorting data", "06:37:49", "06:49:11"),
    ("42-Map + Filter", "06:49:11", "06:58:04"),
    ("43-File handling", "06:58:04", "07:09:35"),
    ("44-Deleting", "07:09:35", "07:13:59"),
    ("45-Classes intro", "07:13:59", "07:30:21"),
    ("46-Classes in practice", "07:30:21", "07:43:48"),
    ("47-Dunder methods", "07:43:48", "08:00:01"),
    ("48-Class and methods", "08:00:01", "08:13:25"),
    ("49-Scope and classes", "08:13:25", "08:28:00"),
    ("50-Simple inheritance", "08:28:00", "08:50:34"),
    ("51-Complex inheritance", "08:50:34", "09:10:30"),
    ("52-Class extra parts", "09:10:30", "09:21:26"),
    ("53-Module intro", "09:21:26", "09:34:51"),
    ("54-External modules", "09:34:51", "09:48:41"),
    ("55-Creating modules", "09:48:41", "09:56:09"),
    ("56-Dunder main", "09:56:09", "09:59:31"),
    ("57-Intro + input + pass", "09:59:31", "10:04:22"),
    ("58-Exceptions & Error handling", "10:04:22", "10:18:56"),
    ("59-Decorators", "10:18:56", "11:01:27"),
    ("60-Eval + Exec", "11:01:27", "11:59:59") 
]

output_folder = './output'  # 请将此处替换为您希望保存文件的文件夹路径
split_srt('subtitles.srt', segments, output_folder)
