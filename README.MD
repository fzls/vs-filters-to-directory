本工具用于将vc项目过滤器转换为实际目录层级

## 主要用途
当项目主要使用vs进行管理，但又想通过clion等ide来打开，想继续使用filter中定义的导航信息，这时候可以通过本工具来生成本地目录，以实现在clion中也能使用导航信息

## 用法
```shell
main.py -r ~/codes/projects_common_root -l _filter_links

usage: main.py [-h] [-r ROOT_DIR] [-l LINK_DIR_NAME]

optional arguments:
  -h, --help            show this help message and exit
  -r ROOT_DIR, --root_dir ROOT_DIR
                        要处理的根目录，将递归处理下方各个项目子目录
  -l LINK_DIR_NAME, --link_dir_name LINK_DIR_NAME
                        各个项目中生成的链接文件夹名称
```

## 示例
假如现在有 a.vcxproj.filters，其中定义了如下的层级关系
```
模块一/
    子模块一/
        文件一.cpp
        文件二.cpp
模块二
    文件三.cpp
```

那么通过本工具可以在项目目录生成一个新的链接目录 `_filter_links`，其层级如下
```
模块一/
    子模块一/
        文件一.cpp(链接文件，指向实际路径)
        文件二.cpp(链接文件，指向实际路径)
模块二
    文件三.cpp(链接文件，指向实际路径)
```

## 使用生成的链接
### 直接编辑
由于是链接文件，可以直接编辑，作用与编辑源文件等效

### 仅用于导航
但是由于链接文件在不同的文件目录中，代码解析可能会有问题

所以推荐仅用于导航。在clion中想要通过filters快速定位某个模块相关文件，可以打开该链接目录来快速定位

同时，为避免查询符号时出现两个相同的，建议在clion中将链接目录忽略，确保不解析其中的链接文件

### jetbrains ide
可使用 IDEA Resolve Symlinks 插件来实现在rider、clion中点击软链接时，跳转到实际的文件，方便修改和查看代码
