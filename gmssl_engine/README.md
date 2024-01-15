# 关于本库

- 基于GmSSL的动态库

- 使用Python封装的接口


> [GmSSL代码源地址](https://github.com/guanzhi/GmSSL)

## 接口说明

1. gmssl_version()
    - 输入
        + 无输入值
    - 输出:
        + 返回GmSSL的版本号
    > 例
    ```python
    version = gmssl_version()
    ```

2. rand_bytes(size)
    - 输入
        + size:int 型，为需要的字符长度
    - 输出
        + bytes类型，返回一个指定（size）长度的bytes串
    > 例
    ```python
    randbytes = rand_bytes(5)
    ```

2. rand_int(size)
    - 输入
        + size:int 型，为需要的字符长度
    - 输出
        + int类型，返回一个指定（size）长度的int串
    > 例
    ```python
    randbytes = rand_int(5)
    ```
