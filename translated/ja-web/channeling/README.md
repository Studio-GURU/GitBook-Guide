---
description: 宝島チャネリングサービスの統合方法について説明します。
icon: user-group
---

# 宝島チャネリング

{% hint style="info" %}
メイン画面へのアクセス方法

***

:ballot\_box\_with\_check:  <mark style="color:red;">**既存の画面ではなく、新しいウィンドウから宝島を起動してください！**</mark>

:heavy\_check\_mark: メイン画面へのアクセス経路に<mark style="color:red;">**signパラメーター**</mark>を渡して、宝島のメイン画面にアクセスします。
{% endhint %}

## メイン画面へのアクセス経路

`https://{env}.treasurecomics.com/gateway/common?sign={sign-value}&returnUrl=https://{env}.treasurecomics.com/main`

:heavy\_check\_mark: returnUrlはUrlEncodeされた値を渡します。

:white\_check\_mark: `{env}`の値は**営業チームから別途提供されます**。

### **署名の生成**

{% hint style="info" %}
**署名生成（**<mark style="color:red;">**HmacSHA256の生成に必要なKeyは営業チームから提供されます。**</mark>**）**

***

:heavy\_check\_mark: $timeStamp$nonce$暗号化されたUser識別子

上記の値はHmacSHA256 Hash -> Base64 Url EncodeによりSignatureを生成します。

***

* timeStamp -> unixタイムスタンプ秒
* nonce -> 文字列32文字（ランダムに生成された文字列32文字）
* ユーザー識別子 -> 会員の区別が可能な識別子
{% endhint %}

<table data-full-width="false"><thead><tr><th width="127">Name</th><th width="141">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>sign</code></td><td>string</td><td><p><code>timestmap.nonce.encryptedUserId.signature</code></p><hr><p> <mark style="background-color:red;">timestamp, nonce, useridの値は<strong>署名の生成に使用された値</strong>を渡します。</mark></p></td></tr></tbody></table>

### 使用例

```
https://test.treasurecomics.com/gateway/common?sign=1724922215.7b82817d9487471a8a782c2604883924.lymanTest.M21MZORoc4NbVzq1ZaSC8LgcOKYH9SBIljHYjVOfX5o%3D&returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fmain
```

***

<figure><img src="../../.gitbook/assets/Simulator Screenshot - iPhone 16 Pro - 2024-10-25 at 14.08.11.png" alt=""><figcaption><p>メッセージ表示のサンプル画面</p></figcaption></figure>

***

## メイン画面

<div align="left"><figure><img src="../../.gitbook/assets/bms_main.png" alt=""><figcaption></figcaption></figure></div>

