import os
import re

# 定义原始文件夹路径和输出文件夹路径
folder_path = 'input'
output_folder_path = 'output'

# 检查输出文件夹是否存在，如果不存在则创建它
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# 定义新的文件名列表
# 注意文件名中不能有英文的`:`，会报错，所以我替换为中文的`：`
new_names = [
    "01-What is Machine Learning Model Deployment and Why Deploy a Machine Learning Model.mp4",
    "02-Three Questions to Ask for Machine Learning Model Deployment.mp4",
    "03-Where Is My Model Going to Go？.mp4",
    "04-How Is My Model Going to Function？.mp4",
    "05-Some Tools and Places to Deploy Machine Learning Models.mp4",
    "06-What We Are Going to Cover.mp4",
    "07-Getting Setup to Code.mp4",
    "08-Downloading a Dataset for Food Vision Mini.mp4",
    "09-Outlining Our Food Vision Mini Deployment Goals and Modelling Experiments.mp4",
    "10-Creating an EffNetB2 Feature Extractor Model.mp4",
    "11-Create a Function to Make an EffNetB2 Feature Extractor Model and Transforms.mp4",
    "12-Creating DataLoaders for EffNetB2.mp4",
    "13-Training Our EffNetB2 Feature Extractor and Inspecting the Loss Curves.mp4",
    "14-Saving Our EffNetB2 Model to File.mp4",
    "15-Getting the Size of Our EffNetB2 Model in Megabytes.mp4",
    "16-Collecting Important Statistics and Performance Metrics for Our EffNetB2 Model.mp4",
    "17-Creating a Vision Transformer Feature Extractor Model.mp4",
    "18-Creating DataLoaders for Our ViT Feature Extractor Model.mp4",
    "19-Training Our ViT Feature Extractor Model and Inspecting Its Loss Curves.mp4",
    "20-Saving Our ViT Feature Extractor and Inspecting Its Size.mp4",
    "21-Collecting Stats About Our ViT Feature Extractor.mp4",
    "22-Outlining the Steps for Making and Timing Predictions for Our Models.mp4",
    "23-Creating a Function to Make and Time Predictions with Our Models.mp4",
    "24-Making and Timing Predictions with EffNetB2.mp4",
    "25-Making and Timing Predictions with ViT.mp4",
    "26-Comparing EffNetB2 and ViT Model Statistics.mp4",
    "27-Visualizing the Performance vs Speed Trade-off.mp4",
    "28-Gradio Overview and Installation.mp4",
    "29-Gradio Function Outline.mp4",
    "30-Creating a Predict Function to Map Our Food Vision Mini Inputs to Outputs.mp4",
    "31-Creating a List of Examples to Pass to Our Gradio Demo.mp4",
    "32-Bringing Food Vision Mini to Life in a Live Web Application.mp4",
    "33-Getting Ready to Deploy Our App Hugging Face Spaces Overview.mp4",
    "34-Outlining the File Structure of Our Deployed App.mp4",
    "35-Creating a Food Vision Mini Demo Directory to House Our App Files.mp4",
    "36-Creating an Examples Directory with Example Food Vision Mini Images.mp4",
    "37-Writing Code to Move Our Saved EffNetB2 Model File.mp4",
    "38-Turning Our EffNetB2 Model Creation Function Into a Python Script.mp4",
    "39-Turning Our Food Vision Mini Demo App Into a Python Script.mp4",
    "40-Creating a Requirements File for Our Food Vision Mini App.mp4",
    "41-Downloading Our Food Vision Mini App Files from Google Colab.mp4",
    "42-Uploading Our Food Vision Mini App to Hugging Face Spaces Programmatically.mp4",
    "43-Running Food Vision Mini on Hugging Face Spaces and Trying it Out.mp4",
    "44-Food Vision Big Project Outline.mp4",
    "45-Preparing an EffNetB2 Feature Extractor Model for Food Vision Big.mp4",
    "46-Downloading the Food 101 Dataset.mp4",
    "47-Creating a Function to Split Our Food 101 Dataset into Smaller Portions.mp4",
    "48-Turning Our Food 101 Datasets into DataLoaders.mp4",
    "49-Training Food Vision Big： Our Biggest Model Yet!.mp4",
    "50-Outlining the File Structure for Our Food Vision Big.mp4",
    "51-Downloading an Example Image and Moving Our Food Vision Big Model File.mp4",
    "52-Saving Food 101 Class Names to a Text File and Reading them Back In.mp4",
    "53-Turning Our EffNetB2 Feature Extractor Creation Function into a Python Script.mp4",
    "54-Creating an App Script for Our Food Vision Big Model Gradio Demo.mp4",
    "55-Zipping and Downloading Our Food Vision Big App Files.mp4",
    "56-Deploying Food Vision Big to Hugging Face Spaces.mp4",
    "57-PyTorch Mode Deployment：Main Takeaways, Extra-Curriculum and Exercises.mp4"
]




# 获取文件夹中的所有视频文件
video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

# 提取文件名中的数字部分，并按自然数排序
def extract_and_sort(files):
    def extract_number(s):
        match = re.search(r'\d+', s)
        if match:
            return int(match.group())
        return 0

    return sorted(files, key=lambda x: extract_number(x))

video_files = extract_and_sort(video_files)

# 检查文件数量是否匹配
if len(video_files) != len(new_names):
    print("⚠️ 警告：视频文件数量与新文件名数量不匹配！")
else:
    # 重命名文件并移动到输出文件夹
    for old_name, new_name in zip(video_files, new_names):
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(output_folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"🔄 文件 '{old_name}' 已重命名为 '{new_name}' 并移动到输出文件夹。")

    # 删除原始输入文件夹
    os.rmdir(folder_path)

    # 重命名输出文件夹为原始输入文件夹的名称
    os.rename(output_folder_path, folder_path)

print("✅ 重命名操作完成。")
