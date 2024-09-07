<div align="center">
<h1><i>✨ LYPress ✨</i></h1>
<p><b><i>下一代的Litedoc，Python模块文档构建工具</i></b></p>
0.0.1开发中，敬请期待...
</div>

## 特性

- 通过解耦docstring parser支持多种风格文档字串
- 生成简洁Markdown
- 动态开发重载
- 自定义模板样式
- 多语言支持
- 对象链接跳转

## 快速开始

### 安装

```shell
pip install git+https://github.com/LiteyukiStudio/lypress
```

### 使用

在`docs/`目录下生成库`lypress_example`（内置示例模块）的文档

```shell
lypress build -i lypress_example -o docs
```

## 详细使用

### 命令行

初始化并生成默认配置文件到指定文件
```shell
lypress init
```

生成文档
```shell
lypress build
```

启动文件变更重载
```shell
lypress dev
```
