
## QYmeta Python SDK

清元多链QYmeta Python是针对国内多家联盟链提供的一套完整的web3、数字藏品等解决方案的python sdk版。开发者无需深入了解各联盟链的相关技术知识，可通过QYmeta python SDK 快速搭建自己的web3、数字藏品应用。

* 清元多链 [官网](http://openqkl.newmin.cn/)

* 清元链 NFT SDK [文档](https://github.com/qymeta/qymeta_py/blob/main/doc/qyb_nft.md)

  
### Installation
```python
pip install qymeta
```

### Upgrade
```python
pip install qymeta --upgrade
```

### Quick Start

```
import qymeta as qy
result = qy.qy_nft_create_nft_info(appid = "……", secret = "……", title = "……", author = "……", url = "……")
print(result)
```

### Change Logs

#### 0.0.4 2022/11/01

* 清元链 NFT 相关接口发布
