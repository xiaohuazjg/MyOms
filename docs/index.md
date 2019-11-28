# 概述
随便写写

---

## 项目组成

> 本项目基于python3.6和vue2.0开发，采用的前后端分离模式

后端：基于python3和django构建api,提供数据支持

前端： 基于 [Vue.js](https://github.com/vuejs/vue) 和 [element](http://element.eleme.io/#/zh-CN/component/installation)，页面展示大部分参考[vue-element-admin](https://github.com/PanJiaChen/vue-element-admin), 在这里十分感谢PanJiaChen的开源。

## 效果图

> 先来几张样图

### 1. 登录
![登录](/assets/images/index/login.png)

### 2. 首页
![首页](/assets/images/index/index1.png)

### 3. 工单系统
![工单系统](/assets/images/index/index2.png)

### 4. 发布系统
![发布系统](/assets/images/index/index3.png)

### 5. 执行命令
![执行命令](/assets/images/index/index4.png)


## 目录介绍

### 1. 后端

``` bash
.
├── celery.service             # celery在centos7的启动文件
├── dnsmanager                 # dns模块
├── hosts                      # 主机模块
├── __init__.py                
├── init.sh                    # 初始化脚本
├── jobs                       # 发布系统
├── manage.py           
├── menus                      # 菜单模块
├── omsBackend                 # django主配目录
├── omsBackend.sock            
├── oms.ini                    # uwsgi 启动配置
├── oms.service                # oms在centos7的启动文件
├── perms                      # 权限模块
├── projects                   # 项目模块
├── records                    # 日志审计
├── requirements.txt           # 安装包依赖文件
├── salts                      # saltapi模块
├── tasks                      # celery任务
├── tools                      # 工具管理
├── upload                     # 上传文件
├── users                      # 用户模块
├── utils                      # 小脚本管理
├── wikis                      # 文档系统
├── worktickets                # 工单系统
├── zbmanager                  # zabbix模块
└── zkmanager                  # 中控考勤机
```

### 2. 前端

```
.
├── build                      // 构建相关  
├── config                     // 配置相关
├── src                        // 源代码
│   ├── api                    // 所有请求
│   ├── assets                 // 主题 字体等静态资源
│   ├── components             // 全局公用组件
|   ├── directive              // 自定义指令
│   ├── filtres                // 全局filter
│   ├── router                 // 路由
│   ├── store                  // 全局store管理
│   ├── styles                 // 全局样式
│   ├── utils                  // 全局公用方法
│   ├── views                  // 页面
│   ├── App.vue                // 入口页面
│   ├── main.js                // 入口 加载组件 初始化等
│   ├── config.js              // 配置文件
│   └── permission.js          // 权限检查
├── static                     // 第三方资源
│   ├── js                     //  第三方js
│   └── rest_framework         // rest_framework的js和css
├── .babelrc                   // babel-loader 配置
├── eslintrc.js                // eslint 配置项
├── .gitignore                 // git 忽略项
├── favicon.ico                // favicon图标
├── index.html                 // html模板
└── package.json               // package.json
```

## 项目初始化

### 1. 克隆项目
``` bash
git clone https://github.com/itimor/django-oms.git
```

### 2. 后端
```
# 安装python依赖
cd omsBackend
pip install -r requirements.txt

# 生成数据库文件
# 把每个模块 makemigrations
python manage.py makemigrations 模块名

#初始化数据库
python manage.py migrate

#创建admin用户
python manage.py createsuperuser 

#启动
python manage.py runserver 0.0.0.0:8000

```

### 3. 前端
```
# 安装依赖
npm install
#或者
npm install --registry=https://registry.npm.taobao.org

# 本地开发 开启服务
npm run dev

# 打包
npm run build
```

## 后续
> - 完成以上步骤后，大概也许可能项目可以用了吧， 项目本身是按照公司基本需要开发的，所以想使用此项目你还得根据自己公司的规则来进行修改使用，如有其它问题，可以及时拍砖(issue)
> - 后续可能要弄个周报系统， 每周结束之前在oms系统上发布周报，方便领导统计、查看。

