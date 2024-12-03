---
description: ユーザーが閲覧したコンテンツに基づいて推薦リストAPIの使用方法を説明します。
icon: thumbs-up
---

# 推薦コンテンツリスト取得

## バージョン

バージョン情報はURLパスに含めず、ヘッダーの`accept-version`属性値に定義します。

| バージョン   | 日付          | 説明       |
| ------------ | ------------- | ---------- |
| 1.0.0        | 2024.08.23    | 作成       |

## 推薦コンテンツ

<mark style="color:green;">`GET`</mark> `https://api-{env}.treasurecomics.com/external/recommendation?sign={value}`

推薦コンテンツリストを返します。

### ヘッダー

| 名前            | 値                  |
| --------------- | ------------------- |
| Content-Type    | `application/json`  |
| Authorization   | `Basic token`       |
| Accept-Version  | `1.0.0`             |

### **ボディ**

{% hint style="info" %}
**署名の生成 (HmacSHA256生成用のKeyは営業チームから提供されます。)**

***

:heavy\_check\_mark: $timeStamp$nonce$暗号化されたUser識別子

上記値をHmacSHA256 Hash -> Base64 URLエンコードで署名を生成します。

***

* timeStamp -> UNIXタイムスタンプ秒
* nonce -> 32文字のランダム文字列
* User識別子 -> 会員を特定できる識別子
{% endhint %}

<table data-full-width="false"><thead><tr><th width="127">名前</th><th width="141">タイプ</th><th>説明</th></tr></thead><tbody><tr><td><code>sign</code></td><td>string</td><td><p><code>timestamp.nonce.encryptedUserId.signature</code></p><hr><p><mark style="background-color:red;">timestamp、nonce、User識別子は<strong>署名の生成に使用した値</strong>を送信します。</mark></p></td></tr></tbody></table>
// 使用例 https://api-{env}.treasurecomics.com/external/recommendation?sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ

### **レスポンス**

<table><thead><tr><th width="239">フィールド</th><th width="106">タイプ</th><th>説明</th></tr></thead><tbody><tr><td><code>recommendationSN</code></td><td>number</td><td>シーケンス</td></tr><tr><td><code>title</code></td><td>string</td><td>タイトル</td></tr><tr><td><code>description</code></td><td>string</td><td>説明</td></tr><tr><td><code>thumbnail</code></td><td>string</td><td>画像パス</td></tr><tr><td><code>contentType</code></td><td>string</td><td>ウェブトゥーン | ウェブ小説</td></tr><tr><td><code>contentCName</code></td><td>string</td><td>作品キー</td></tr><tr><td><code>episodeNo</code></td><td>number</td><td>エピソード番号</td></tr><tr><td><code>genre</code></td><td>string</td><td>ジャンル</td></tr><tr><td><code>link</code></td><td>string</td><td><p>提供されたリンクに署名を付加して送信</p><p>例)<code>&#x26;sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ</code></p></td></tr><tr><td><code>returnUrl</code></td><td>string</td><td>最終移動リンク(参考用)</td></tr><tr><td><code>order</code></td><td>number</td><td>表示優先順位(同一値あり)</td></tr><tr><td><code>recommendationDate</code></td><td>string</td><td>推薦日(yyyy-MM-dd)</td></tr></tbody></table>

**レスポンスコード**

{% tabs %}
{% tab title="200" %}
{% code lineNumbers="true" %}
```json
[  {    "recommendationSN": 5,    "title": "奉仕感とラブレター",    "description": "奉仕感とラブレターのテスト",    ...  }]
{% endcode %} {% endtab %}

{% tab title="499" %} {% code lineNumbers="true" %}
{
  "code": "err_already_used_signature",
  "message": "既に使用された署名です。",
  ...
}
{% endcode %} {% endtab %} {% endtabs %}

エラーコード
<table><thead><tr><th width="307">コード</th><th>理由</th><th>メッセージ</th></tr></thead><tbody><tr><td><mark style="color:red;"><code>err_invalid_signature</code></mark></td><td>署名検証失敗</td><td>無効な署名です。</td></tr><tr><td><mark style="color:red;"><code>err_already_used_signature</code></mark></td><td>使用済み署名の再利用<br>-> 5分間制限</td><td>既に使用された署名です。</td></tr></tbody></table>
推薦コンテンツリストの画面例
<div align="left"><figure><img src="../../../.gitbook/assets/bms_recommendation_2.png" alt="" width="375"><figcaption></figcaption></figure></div> ```
