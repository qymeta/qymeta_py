## 清元链 NFT

### 创建链账户

接口: qy_nft_create_account_address

描述: 创建用户链账户； 

**输入参数**

名称 | 类型 | 必须 | 说明 
---|:---:|:---:|---
appid | str | Y | appid 
secret | str | Y | 秘钥 
name | str | Y | 用户姓名 
idc | str | Y | 用户身份证号 
mobile | str | Y | 用户手机号 

**输出参数**

 名称 | 类型 | 说明 
---|:---:|---
 code | int | 返回码 
 msg | str | 返回说明 
 data |  |
 -- address | str | 链账户地址 

**返回示例**

```
{
	'code': 200, 
	'msg': 'success', 
	'data': {
		'address': '0x75b136cb0ab31bd3b34a194c083ef5a510c285d0'
	}
}
```

**接口示例**

```
import qymeta as qy
result = qy.qy_nft_create_account_address(appid = "……", secret = "……", name = "……", idc = "……", mobile = "……",)
print(result)

>> {'code': 200, 'msg': 'success', 'data': {'address': '0x75b136cb0ab31bd3b34a194c083ef5a510c285d0'}}
```



### 创建NFT资源

接口: qy_nft_create_nft

描述: 创建NFT资源； 

**输入参数**

| 名称        | 类型 | 必须 | 说明            |
| ----------- | :--: | :--: | --------------- |
| appid       | str  |  Y   | appid           |
| secret      | str  |  Y   | 秘钥            |
| title       | str  |  Y   | NFT资源名称     |
| address     | str  |  Y   | NFT拥有者链账户 |
| author      | str  |  Y   | 作者            |
| url         | str  |  Y   | NFT资源地址     |
| series_id   | str  |  N   | 系列ID          |
| series_name | str  |  N   | 系列名称        |

**输出参数**

| 名称             | 类型 | 说明        |
| ---------------- | :--: | ----------- |
| code             | int  | 返回码      |
| msg              | str  | 返回说明    |
| data             |      |             |
| -- Payload       | str  |             |
| -- TokenId       | str  | TOKEN ID    |
| -- SourceUrl     | str  | NFT资源地址 |
| -- TransactionID | str  | 交易ID      |

**返回示例**

```
{
	'code': 200, 
	'msg': 'success', 
	'data': {
		'Payload': '', 
		'TokenId': '5cfe2dfc4ef914985e60ac2c7723e67875c0eeda56232ebd6e8858350e0b4b52', 
		'TransactionID': 'ae86ae491cad24dfbc21fa5cbb2877b24a15b6a2dd3bba9f44f400fe3775e0fe', 
		'SourceUrl': 'http://openqkl.newmin.cn/resouce/hxSFmLMR9zDsFRNIICffDiIOSTPwBK'
	}
}
```

**接口示例**

```
import qymeta as qy
result = qy.qy_nft_create_nft(appid = "……", secret = "……", title = "……", address = "……", author = "……", url = "……")
print(result)

>> {'code': 200, 'msg': 'success', 'data': {'Payload': '', 'TokenId': '5cfe2dfc4ef914985e60ac2c7723e67875c0eeda56232ebd6e8858350e0b4b52', 'TransactionID': 'ae86ae491cad24dfbc21fa5cbb2877b24a15b6a2dd3bba9f44f400fe3775e0fe', 'SourceUrl': 'http://openqkl.newmin.cn/resouce/hxSFmLMR9zDsFRNIICffDiIOSTPwBK'}}
```



### 铸造NFT

接口: qy_nft_casting_nft

描述: 将NFT资源上链进行铸造NFT； 

**输入参数**

| 名称       | 类型 | 必须 | 说明                                 |
| ---------- | :--: | :--: | ------------------------------------ |
| appid      | str  |  Y   | appid                                |
| secret     | str  |  Y   | 秘钥                                 |
| source_url | str  |  Y   | NFT资源地址  通过创建NFT资源接口获取 |
| order_sn   | str  |  Y   | 订单号                               |

**输出参数**

| 名称             | 类型 | 说明     |
| ---------------- | :--: | -------- |
| code             | int  | 返回码   |
| msg              | str  | 返回说明 |
| data             |      |          |
| -- Hash          | str  | 交易哈希 |
| -- TransactionID | str  | 交易ID   |

**返回示例**

```
{
	'code': 200, 
	'msg': 'success', 
	'data': {
		'Hash': '00b5ef79bd5bc9e00dcb152e0e9ebe09d9faf2735bfe8cb60008ec30c059cb90', 
		'TransactionID': 'e2a94bcb9c97492ebaab27135186556cb13ef9458e400570bd166ca35cc8510d'
	}
}
```

**接口示例**

```
import qymeta as qy
result = qy.qy_nft_casting_nft(appid = "……", secret = "……", source_url = "……", order_sn= "……")
print(result)

>> {'code': 200, 'msg': 'success', 'data': {'Hash': '00b5ef79bd5bc9e00dcb152e0e9ebe09d9faf2735bfe8cb60008ec30c059cb90', 'TransactionID': '6be9a7d15cfe4cb42ecb5b075a81509a9c62ae30405bb50a5ab025d1c56720ad'}}


```



### NFT转移

接口: qy_nft_trans_from

描述: 将NFT资源上链进行铸造NFT； 

**输入参数**

| 名称         | 类型 | 必须 | 说明                |
| ------------ | :--: | :--: | ------------------- |
| appid        | str  |  Y   | appid               |
| secret       | str  |  Y   | 秘钥                |
| address_from | str  |  Y   | NFT归属者链账户地址 |
| address_to   | str  |  Y   | NFT接收方链账户地址 |
| token_id     | str  |  Y   | Token ID            |

**输出参数**

| 名称             | 类型 | 说明     |
| ---------------- | :--: | -------- |
| code             | int  | 返回码   |
| msg              | str  | 返回说明 |
| data             |      |          |
| -- TransactionID | str  | 交易ID   |
| -- Payload       | str  |          |

**返回示例**

```
{
	'code': 200, 
	'msg': 'success', 
	'data': {
		'Payload': '', 
		'TransactionID': 'f5a700c184d94ddbbf07d3842c7ae424cd22c6c3697581cdc7fbfbdb34e35839'
	}
}
```

**接口示例**

```
import qymeta as qy
result = qy.qy_nft_trans_from(appid = "……", secret = "……", address_from = "……", address_to = "……", token_id = "……")
print(result)

>> {'code': 200, 'msg': 'success', 'data': {'Payload': '', 'TransactionID': 'f5a700c184d94ddbbf07d3842c7ae424cd22c6c3697581cdc7fbfbdb34e35839'}}
```



### NFT销毁

接口: qy_nft_destruction

描述: 将链上NFT销毁； 

**输入参数**

| 名称         | 类型 | 必须 | 说明                |
| ------------ | :--: | :--: | ------------------- |
| appid        | str  |  Y   | appid               |
| secret       | str  |  Y   | 秘钥                |
| address_from | str  |  Y   | NFT归属者链账户地址 |
| token_id     | str  |  Y   | Token ID            |

**输出参数**

| 名称             | 类型 | 说明     |
| ---------------- | :--: | -------- |
| code             | int  | 返回码   |
| msg              | str  | 返回说明 |
| data             |      |          |
| -- TransactionID | str  | 交易ID   |
| -- Payload       | str  |          |

**返回示例**

```
{
	'code': 200, 
	'msg': 'success', 
	'data': {
		'Payload': '', 
		'TransactionID': 'f5a700c184d94ddbbf07d3842c7ae424cd22c6c3697581cdc7fbfbdb34e35839'
	}
}
```

**接口示例**

```
import qymeta as qy
result = qy.qy_nft_destruction(appid = "……", secret = "……", address_from = "……", token_id = "……")
print(result)

>> {'code': 200, 'msg': 'success', 'data': {'Payload': '', 'TransactionID': 'f5a700c184d94ddbbf07d3842c7ae424cd22c6c3697581cdc7fbfbdb34e35839'}}
```



### 查询某账户拥有的NFT

接口: qy_nft_get_balanceof

描述: 查询某账户下拥有的NFT信息； 

**输入参数**

| 名称    | 类型 | 必须 | 说明       |
| ------- | :--: | :--: | ---------- |
| appid   | str  |  Y   | appid      |
| secret  | str  |  Y   | 秘钥       |
| address | str  |  Y   | 链账户地址 |

**输出参数**

| 名称     | 类型  | 说明                               |
| -------- | :---: | ---------------------------------- |
| code     |  int  | 返回码                             |
| msg      |  str  | 返回说明                           |
| data     |       |                                    |
| -- Count |  int  | 拥有NFT总数                        |
| -- List  | array | 拥有NFT列表｛TOKENID:NFT资源地址｝ |

**返回示例**

```
{
	'code': 200, 
	'msg': 'success', 
	'data': {
		'Count': 1, 
		'List': {'11a4f81dc2eb44dda24f94f2492c62729b5a2a02f5eebb4e21a150e282ded21e': 'http://openqkl.newmin.cn/resouce/1Ivid5vTCkGwG0RbwYbLITOFQrZXl4?tokenId=11a4f81dc2eb44dda24f94f2492c62729b5a2a02f5eebb4e21a150e282ded21e'
		}, 
		'TransactionID': '09e52b2bd84d121d57964a205a0c1a22d8ac64ebeba6ffd805ff03cd75e8f01a'
	}
}
```

**接口示例**

```
import qymeta as qy
result = qy.qy_nft_get_balanceof(appid = "……", secret = "……", address = "……")
print(result)

>> {'code': 200, 'msg': 'success', 'data': {'Count': 1, 'List': {'11a4f81dc2eb44dda24f94f2492c62729b5a2a02f5eebb4e21a150e282ded21e': 'http://openqkl.newmin.cn/resouce/1Ivid5vTCkGwG0RbwYbLITOFQrZXl4?tokenId=11a4f81dc2eb44dda24f94f2492c62729b5a2a02f5eebb4e21a150e282ded21e'}, 'TransactionID': '09e52b2bd84d121d57964a205a0c1a22d8ac64ebeba6ffd805ff03cd75e8f01a'}}

```



### 查询NFT上链存证信息

接口: qy_nft_query

描述: 查询交易哈希获取上链的存证信息； 

**输入参数**

| 名称   | 类型 | 必须 | 说明     |
| ------ | :--: | :--: | -------- |
| appid  | str  |  Y   | appid    |
| secret | str  |  Y   | 秘钥     |
| hash   | str  |  Y   | 交易哈希 |

**输出参数**

| 名称             | 类型 | 说明        |
| ---------------- | :--: | ----------- |
| code             | int  | 返回码      |
| msg              | str  | 返回说明    |
| data             |      |             |
| -- Info          | dict | NFT存证信息 |
| -- TransactionID | str  | 交易ID      |

**返回示例**

```
{
	'code': 200, 
	'msg': 'success', 
	'data': {
		'Info': {
			'author': '李四', 
			'title': '测试nft', 
			'series_name': None, 
			'series_id': None, 
			'url': 'https://pics6.baidu.com/feed/f31fbe096b63f624f3a2472ac3cecbf31b4ca3b5.jpeg@f_auto?token=59521ff095f3494fc1207eeba354f130'
		}, 
		'TransactionID': 'd3d72e0a36a1c6dadd50af1e8495faacd14bbce55db9f570d711088ddb7f8257'}
	}

```

**接口示例**

```
import qymeta as qy
result = qy.qy_nft_query(appid = "……", secret = "……", hash = "……")
print(result)

>> {'code': 200, 'msg': 'success', 'data': {'Info': {'author': '李四', 'title': '测试nft', 'series_name': None, 'series_id': None, 'url': 'https://pics6.baidu.com/feed/f31fbe096b63f624f3a2472ac3cecbf31b4ca3b5.jpeg@f_auto?token=59521ff095f3494fc1207eeba354f130'}, 'TransactionID': 'd3d72e0a36a1c6dadd50af1e8495faacd14bbce55db9f570d711088ddb7f8257'}}
```

