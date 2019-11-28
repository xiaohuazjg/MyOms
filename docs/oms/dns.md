# dns和zabbix
oms系统对接binddns和zabbix

---

## dns管理

### 1. 环境说明

因为公司使用了众多域名服务商(godaddy/dnspod/bind)，而且域名数量较大，如果域名有问题的时候，不能立马查到域名是在哪里解析的，说以做了这么模块，用于集中化管理所有域名，且能很快知道域名的归属地。

域名是通过各域名服务商提供的api进行收集和管理，其中bind是自建的dns服务器，它的api是我用django写的，项目地址： [bindapi](https://github.com/itimor/bindapi.git)； godaddy的api最烂，几乎没怎么维护；dnspod的api相当友好，文档非常详细，上手容易。

*api地址*：

> - [bind_api.py](https://github.com/itimor/django-oms/blob/master/omsBackend/dnsmanager/bind_api.py)

> - [dnspod_api.py](https://github.com/itimor/django-oms/blob/master/omsBackend/dnsmanager/dnspod_api.py)

> - [godaddyapi.py](https://github.com/itimor/django-oms/blob/master/omsBackend/dnsmanager/godaddy_api.py)

### 2. 添加dnsapi的key，同步域名

*dns管理 -> api管理*

![dns-api管理](/assets/images/dns/dns1.png)

- 在第一列表格添加新的dns服务商的秘钥信息，其中 `godaddy`用的是 key 和 serert; `dnspod`和`bind`用的是id和token；

- 点击刚添加的dns,会看到第二列表格，这个会显示这个dns下的当前所以域名，点击同步，它会把这里的域名同步到oms系统；

- 点击域名，第三列表格会展示这个域名下所以record;


### 3. 管理record

*dns管理 -> 域名列表*

![域名列表](/assets/images/dns/dns2.png)

在这里可以看到上一步同步过来的域名， 这个列表可以实时的反映每个`域名有效期` 、`ns地址`，以及属于哪个dnsapi, 提供搜索功能，方便快速查找域名。

- 点击同步记录，会把这个域名下的所有记录同步过来；

- 点击添加记录，会在这个域名下添加一条新的记录；

- 点击修改域名，可以给域名添加当前状态和备注信息，dns服务商是没有备注功能的；

![添加域名备注](/assets/images/dns/dns3.png)

- 点击修改记录，可以更换ip，这个会马上同步到dns服务商

## zabbix管理
> [zabbix_api.py](https://github.com/itimor/django-oms/blob/master/omsBackend/zbmanager/zabbix_api.py)

zabbix与oms系统对接都是通过上面的脚本完成的，主要功能是关于zabbix主机的增删改查，可以批量添加或删除主机，再添加监控上可以节省时间。