<div align="center">
<h1><i>✨ LitePress ✨</i></h1>
<p><b><i>下一代的Litedoc，Python模块文档构建工具</i></b></p>
0.0.1开发中，敬请期待...
</div>

## 特性

- 通过解耦docstring parser支持多种docstring风格
- 支持 Markdown 语法
- 支持动态开发重载
- 支持自定义模板样式
- 支持多语言文档

## 快速开始

### 安装

```shell
pip install git+https://github.com/LiteyukiStudio/litepress
```

### 使用

在`docs/`目录下生成库`litepress_example`（内置示例模块）的文档

```shell
litepress build -i litepress_example -o docs
```

## 详细使用

### 命令行

生成默认配置文件到指定文件
```shell
litepress gencfg [output="litepress.yml"] # 默认输出到litepress.yml
```

生成文档
```shell
litepress build [-c config="litepress.yml"] [-i input="."] [-o output="docs"]
```