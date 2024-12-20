# mubu_html_to_markdown

一个简单的幕布导出的html转markdown的小工具

基于 <https://github.com/cjlworld/mubu-to-md-converter/blob/main/mubu_converter.py> 进行改进而来

## 调用方式

```sh
python mubu_converter.py <html_file_path> <output_file_path>
```

## 注意事项

- 目前只支持导出单个文件，不支持批量导出
- 支持正常化标题级别（需提前将笔记的标题级别设置好）、文本、图片、代码块、公式等常用元素
  
## 更新

- 2024/12/10 增加文本的颜色格式追加
