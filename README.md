## openBlocks
项目已部署
http://www.openblocks.net/
### 说明
统计跟踪开源区块链项目的star/fork/commit记录等信息

前端使用 Vue.js+ElementUI   后端使用 flask+mysql

### 目录结构
├─api　　　　　　　后端根目录  
│　├─app              
│　│　├─api_v1  
│　│　├─static  
│　│　├─templates  
│　├─spider　　　　爬虫端根目录   
│　├─config.py 　　　配置信息    
├─front　　　　　　前端端根目录  
│　└─src  

### 本地运行
```
进入api目录 config.py 填写相应配置信息

## 安装依赖
pip install -r requirements.txt

## 新建数据库表格
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

## 启动爬虫
cd spider         # 进入spider目录
python spider.py

## 启动服务
python manage.py runserver

## 启动前端
cd front          # 进入前端根目录
npm install
npm run dev
```
