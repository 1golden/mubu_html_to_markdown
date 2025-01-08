# -*- coding: utf-8 -*-
# @Author: lveway
# @Date:   2024-12-20
# based on https://github.com/cjlworld/mubu-to-md-converter/blob/main/mubu_converter.py

from bs4 import BeautifulSoup, Tag
from markdownify import MarkdownConverter
import sys
import re

import urllib.parse


class MubuConverter:
    def __init__(self, html_file: str):
        self.html_file = html_file

    def convert(self) -> str:
        # 读取 HTML 文件内容
        with open(self.html_file, 'r', encoding='utf-8') as file:
            html = file.read()

        # 解析 HTML
        soup = BeautifulSoup(html, 'html.parser')
        return self.convert_soup(soup)

    def convert_soup(self, soup: BeautifulSoup) -> str:
        # 转换 LaTeX 块
        for latex_tag in soup.find_all("span", attrs={"class": "formula", "data-raw": True}):
            annotation_tag = latex_tag.find("annotation")
            if annotation_tag and annotation_tag.string:
                latex_content = annotation_tag.string.strip()
                latex_tag.string = f'${latex_content}$'  
            else:
                data_raw = latex_tag.get('data-raw', '').strip()
                if data_raw:
                    decoded_latex = urllib.parse.unquote(data_raw)
                    latex_tag.string = f'${decoded_latex}$'  # 直接转换 data-raw
                else:
                    latex_tag.string = ''  
        
        # 将描述区的内容变成markdown的注释
        for note_tag in soup.find_all("div", class_="note mm-editor"):
            note_tag.insert_before(">")  # 插入引用符号，可以正常显示描述区的公式
    
        # 处理行内代码
        for code_tag in soup.find_all('span', class_='codespan'):
            code_tag.insert_before("`")  
            code_tag.insert_after("`")
        
        # 处理粗体、下划线和高亮样式
        for bold_tag in soup.find_all(class_='bold'):
            bold_tag.insert_before("<strong>") 
            bold_tag.insert_after("</strong>")   
        for highlight_tag in soup.find_all(class_='highlight-yellow'):
            highlight_tag.insert_before("<mark>") 
            highlight_tag.insert_after("</mark>")   
        for underline_tag in soup.find_all(class_='underline'):
            underline_tag.insert_before("<u>")  
            underline_tag.insert_after("</u>")    

        # 将class为“text-color-XX”的<span>标签转为md的颜色标签
        for color_tag in soup.find_all('span', class_=lambda x: x and x.startswith('text-color-')):
            color_class = color_tag['class'][0]  # 获取class名
            color_code = color_class.split('-')[-1]  # 提取颜色码
            # 如果是黄色（这破颜色看不清），则转为高亮标签
            if color_code == "yellow":
                color_tag.insert_before("<mark>")  # 插入高亮标签
                color_tag.insert_after("</mark>")
            else:
                color_tag.insert_before(f"<font color={color_code}>")  # 插入颜色标签
                color_tag.insert_after("</font>")
                
        # 移除class="tag"的文本的#号
        for tag_tag in soup.find_all("span", class_="tag"):
            # 移除#号
            tag_tag.string = tag_tag.string.replace("#", "", 1)

        # 处理图片
        for img_tag in soup.find_all("img"):
            img_src = img_tag.get('src')
            markdown_img_tag = f"![]({img_src})"
            # 插入imgtag的父标签之前
            img_tag.parent.insert_before(markdown_img_tag)
            img_tag.decompose()


        # 处理 h1 标题
        for heading1_tag in soup.find_all("li", class_="node heading1"):
            content_tag = heading1_tag.find("div", class_="content")
            if content_tag:
                heading_text = content_tag.get_text(strip=True)
                print(f"处理 H1 标题: {heading_text}")

            # 将该标签变为 H1 标签，添加前缀 #
            heading1_tag.name = "h1"
            heading1_tag.insert_before(f"# {heading_text}\n")
            content_tag.clear()
        
        # 处理 h2 标题
        for heading1_tag in soup.find_all("li", class_="node heading2"):
            content_tag = heading1_tag.find("div", class_="content")
            if content_tag:
                heading_text = content_tag.get_text(strip=True)
                print(f"处理 H2 标题: {heading_text}")

            # 将该标签变为 H2 标签，添加前缀 ##
            heading1_tag.name = "h2"
            heading1_tag.insert_before(f"## {heading_text}\n")
            content_tag.clear()
            
        # 处理 h3 标题
        for heading1_tag in soup.find_all("li", class_="node heading3"):
            content_tag = heading1_tag.find("div", class_="content")
            if content_tag:
                heading_text = content_tag.get_text(strip=True)
                print(f"处理 H3 标题: {heading_text}")

            # 将该标签变为 H3 标签，添加前缀 ###
            heading1_tag.name = "h3"
            heading1_tag.insert_before(f"### {heading_text}\n")
            content_tag.clear()

        # 移除不必要的标签
        head_tag = soup.find("head")
        if type(head_tag) is Tag:
            head_tag.clear()

        # 移除class="tag"的文本的#号
        for tag_tag in soup.find_all("span", class_="tag"):
            tag_tag.string = tag_tag.string.replace("#", "", 1)

                
        # 删除 "以上内容整理于 幕布文档"
        publish_tag = soup.find("div", attrs={"class": "publish"})
        if type(publish_tag) is Tag:
            publish_tag.clear()
        
    
        # 使用 markdownify 转换解析后的内容到 Markdown
        md_content = MarkdownConverter(
            escape_underscores=False, escape_asterisks=False, bullets='-',).convert_soup(soup)


        # 清除多余的换行符
        md_content = md_content.lstrip()
        # 匹配并移除所有的 = 符号
        md_content = re.sub(r"=+\n", "", md_content)
        # 删除一对**之间的所有其他 *号，原本的内容不变
        md_content = re.sub(r"\*\*(.*?)\*\*", lambda m: re.sub(r"\*", "", m.group(0)), md_content)
        # 使用正则表达式匹配二级标题，并在其前添加分割线
        md_content = re.sub(r"^## (.*?)\n", lambda m: f"---\n## {m.group(1)}\n", md_content, flags=re.MULTILINE)


        return md_content



if __name__ == "__main__":
    # 调用方式：
    # python mubu_converter.py <html_file_path> <output_file_path>
    if len(sys.argv) != 3:
        print("请提供 HTML 文件的路径和输出 Markdown 文件的路径。")
        sys.exit(1)

    html_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    mubu_to_md = MubuConverter(html_file_path)
    md_content = mubu_to_md.convert()

    # 将转换后的内容写入指定的 Markdown 文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(md_content)

    print(f"转换完成，输出文件: {output_file_path}")
