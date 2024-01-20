# 关于本库

- 基于GmSSL的动态库

- 使用Python封装的接口


> [GmSSL代码源地址](https://github.com/guanzhi/GmSSL)

## 接口说明

## 1.<span style="color:#66ccff;">(function)</span> : <span style="color:orange;">gmssl_version()</span>   

- 输入
    + 无输入值
- 输出:
    + 返回GmSSL的版本号
- 例
```python
version = gmssl_version()
```

## 2. <span style="color:#66ccff;">(function)</span> : <span style="color:orange;">rand_bytes(size:int)</span>

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

## 5. <span style="color:#66ccff;">(class)</span><span style="color:green;">Sm4Cbc(key:bytes, iv：bytes)</span>
- sm4的cbc模式，提供cbc模式的加密和解密
- key:bytes类型，需要长度为16字节，iv:bytes类型，需要长度为16字节

    ### 5.1 <span style="color:#66ccff;">(function)</span><span style="color:orange;">encrypt(data:bytes)</span> 
    - 输入：
        + data:bytes类型，为需要加密的文本
    - 输出：
        + bytes类型，为加密后的密文
    
    ### 5.2 <span style="color:#66ccff;">(function)</span><span style="color:orange;">decrypt(data:bytes)</span> 
    - 输入：
        + data:bytes类型，为需要解密的密文
    - 输出：
        + bytes类型，为解密后的明文
- 例
```python
key = b'1234567812345678' # sm4的key
iv = b'1234567812345678' # 初始向量
plaintext = b'1234567812345678' # 待加密的文本

sm4cbc = Sm4Cbc(key, iv) # 实例化Sm4Cbc的类

encrypted = sm4cbc.encrypt(plaintext) #对bytes类型的文本 plaintext 加密，得到bytes类型的密文 encrypted
decrypted = sm4cbc.decrypted(encrypted) #对bytes类型的密文 encrypted 解密，得到bytes类型的铭文 decrypted
```