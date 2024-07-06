# 游戏评论网站

> 参考仓库链接：https://github.com/dhdylanhuang/gamefolio

在源仓库 GameFolio 基础上添加：
- CI/CD自动化构建部署，推送镜像到 Docker hub
- 更改本地 Sqlite 数据库，为分离的 MySql 数据库
- 更新 Python 依赖为最新版，解决兼容性问题

<!--
```sh
python3 manage.py makemigrations \
&& python3 manage.py migrate \
&& python3 populate_gamefolio.py
```
-->

**相关技术**
- Python
- Django
- CI/CD
- Docker
- MySQL
