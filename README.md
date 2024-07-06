# 游戏评论网站

> 参考仓库链接：https://github.com/dhdylanhuang/gamefolio

在源仓库 GameFolio 基础上添加：
- CI/CD自动化构建部署，推送镜像到 Docker hub
- 更改本地 Sqlite 数据库，为分离的 MySql 数据库
- 更新 Python 依赖为最新版，解决兼容性问题


## 使用方法
配置 Github 中的环境变量（Secrets and variables）：
1. Actions 的 Repository secrets：
    - `DOCKERHUB_USERNAME`（Docker Hub 用户名）
    - `DOCKERHUB_TOKEN`（Docker Hub 密码）
2. Codespaces 的 Repository secrets：
    - `CLIENT_ID`（Twitch API Clinet ID）
    - `BEARER`（Twitch API Token）
    - `MYSQL_HOST`（MySQL 服务器地址）
    - `MYSQL_DATABASE`（MySQL 数据库名）
    - `MYSQL_USER`（MySQL 用户名）
    - `MYSQL_PASSWORD`（MySQL 密码）

**相关技术**
- Python
- Django
- CI/CD
- Docker
- MySQL
  
<!--
```sh
python3 manage.py makemigrations \
&& python3 manage.py migrate \
&& python3 populate_gamefolio.py
```
-->
