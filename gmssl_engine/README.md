# 关于本库

- 基于GmSSL的动态库

- 使用Python封装的接口


> [GmSSL代码源地址](https://github.com/guanzhi/GmSSL)

## 接口说明

## 1.<span style="color:#66ccff;">(function)</span> <span style="color:orange;">gmssl_version()</span>   

- 输入
    + 无输入值
- 输出:
    + 返回GmSSL的版本号
- 例
```python
version = gmssl_version()
```

## 2. <span style="color:#66ccff;">(function)</span> <span style="color:orange;">rand_bytes(size:int)</span>

- 输入
    + size:int 型，为需要的字符长度
- 输出
    + bytes类型，返回一个指定（size）长度的bytes串
- 例
```python
randbytes = rand_bytes(5)
```

## 3. <span style="color:#66ccff;">(function)</span><span style="color:orange;">rand_int(size:int)</span> 

- 输入
    + size:int 型，为需要的字符长度
- 输出
    + int类型，返回一个指定（size）长度的int串
- 例
```python
randbytes = rand_int(5)
```

## 4. <span style="color:#66ccff;">(class)</span><span style="color:green;">Sm4(key:bytes)</span>
- sm4的类，提供sm4的加密和解密
- key:bytes类型，为sm4的key，长度需为16字节


    ### 4.1 <span style="color:#66ccff;">(function)</span><span style="color:orange;">encrypt(block:bytes)</span> 
    - 输入：
        + block:bytes型，为需要加密的文本
    - 输出：
        + bytes型，为加密后的密文
    >
    ### 4.2 <span style="color:#66ccff;">(function)</span><span style="color:orange;">decrypt(block:bytes)</span> 
    - 输入：
        + block:bytes型，为需要解密的文本
    - 输出：
        + bytes型，为解密后的明文
- 例
```python
key = b'1234567812345678' #sm4key
plaintext = '0123456' #待加密的文本

sm4 = Sm4(key) #实例化
ciphtertext = sm4.encrypt(plaintext) #加密
plaintext = sm4.decrypt(ciphtertext) #解密

```