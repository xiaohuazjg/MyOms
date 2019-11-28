# salt与主机
有关salt和主机，以及发布系统相关的问题

---

## salt模块

> SaltStack经常被描述为Func加强版+Puppet精简版。作为一个强大的配置管理工具，在日常的运维工作中是必不可少的，这里是通过调用 `salt api` 来实现在web界面操作saltstack.

### 1. saltapi
salt模块的核心
> [saltapi.py](https://github.com/itimor/django-oms/blob/master/omsBackend/salts/saltapi.py)

 这个脚本涵盖了saltapi的一些常用操作，比如 minion管理、远程执行命令、state服务等。

### 2. 发布模块
这个模块是依赖 `saltapi` 的远程执行命令功能，salt自带异步功能，首先它把发布任务放入任务队列，然后你通过salt返回的`j_id`查询发布结果，前后交互的数据都是json格式。

*发布任务*：

![发布系统](/assets/images/index/index3.png)

*发布结果展示*：

![发布结果](/assets/images/host/host1.png)

### 3. state模块
> saltstack最强大功能的是state模块，平时我们为了集中化配置管理服务器，会写很多的 `state.sls` 来协助日常运维工作， 比如服务器初始化、批量执行命令、批量更新配置、批量部署zabbix或tomcat等等，现在我们这些 `state.sls` 存到oms系统，然后在页面上通过点击使其工作。

*选择主机和state服务*：

![执行state服务](/assets/images/host/host2.png)

*执行记录查看*：

![查看执行结果](/assets/images/host/host3.png)

---

## 资产模块

### 1. 主机的自动收集和更新
这个是利用salt的grains获取minion节点的系统信息，不用再手动往里录入资产信息，有这个就轻松很多了，不过针对一些交换机路由器等设备，你还是得手动录入。

![主机列表](/assets/images/host/host4.png)

### 2. 资产修改记录

这个是一个修改记录表，在主机列表里面变更数据，都会记录到这里面，无论是手动更改还是自动更改的数据，同时会记录修改时间和修改人。

![资产修改记录](/assets/images/host/host5.png)

---