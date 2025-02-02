import re
import os

def remove_markdown_symbols(text):
    # 移除标题符号 #
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    # 移除加粗符号 **
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    # 将 \( 和 \) 替换成 $
    text = text.replace(r'\(', '$').replace(r'\)', '$')
    # 将 \[ 和 \] 替换成 $$
    text = text.replace(r'\[', '$$').replace(r'\]', '$$')
    return text

def main():
    # 读取输入文件路径
    input_file = input("请输入输入文件的路径：")
    
    try:
        # 生成输出文件路径（在同一目录下，文件名加 "_new"）
        file_dir = os.path.dirname(input_file)
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(file_dir, f"{file_name}_new.md")
        
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # 处理文本
        processed_text = remove_markdown_symbols(text)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed_text)
        
        print("文件处理完成！")
        print(f"输入文件：{input_file}")
        print(f"输出文件：{output_file}")
    
    except FileNotFoundError:
        print("输入文件不存在！")
    except Exception as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    main()
