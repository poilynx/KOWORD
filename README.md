# KOWORD 使用手册 


### 1 项目简介
这是一个基于Django + JS +Sqlite3 + Python的背单词网站。主要功能包括：
- 用户注册与登录

- 词库（单词书）信息展示

- 用户单词学习与学习记录展示

- 用户单词复习与复习记录展示

- 用户单词考核

  

### 2 运行环境
- 软件客户端
	- 操作系统：Windows、Linux、Mac等均可
	- 浏览器：Chrome、Firefox、Safari等均可

软件服务器端：
- 操作系统：Ubuntu16.04
  - 数据库软件：Sqlite3

  - 系统框架：Django

    

### 3 安装
* 本项目在Ubuntu16.04上进行开发与测试
1. 建议首先安装Anaconda以方便后后续配置环境；
2. 创建虚拟环境：本项目Python版本为3.5.5
```
conda create -n your_env_name python=3.5
```
3. 开启该虚拟环境
```
source activate your_env_name
```
4. 安装依赖
```
pip install -r requirements.txt
```



### 4 运行

1. 运行manage.py
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
2. 打开浏览器，输入 ip：port/login （为登录界面)，e.g. 
```
127.0.0.1:8000/login
```



### 5 测试

- 测试账号(用username和email都可以登录)
	- username: layla3
	- email: layla3@gmail.com
	- password: 123456
- 首次登录的时候注册账号



