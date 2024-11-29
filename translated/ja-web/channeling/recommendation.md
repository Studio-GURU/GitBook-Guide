---
description: ユーザーが照会したコンテンツに基づいた推奨リストAPIの使用方法について学びましょう。
icon: thumbs-up
---

# 推奨コンテンツリストの参照

## Version

バージョン情報はURLのパスではなく、ヘッダーの accept-version 属性値で定義します。

| Version | Date       | Description |
| ------- | ---------- | ----------- |
| 1.0.0   | 2024.08.23 | Create      |

## 推奨コンテンツ

<mark style="color:green;">`GET`</mark> `https://api-{env}.treasurecomics.com/external/recommendation?sign={value}`

推奨コンテンツリストを返します。

### Headers

| Name           | Value              |
| -------------- | ------------------ |
| Content-Type   | `application/json` |
| Authorization  | `Basic token`      |
| Accept-Version | `1.0.0`            |

### **Body**

{% hint style="info" %}
**署名の生成 (**<mark style="color:red;">**HmacSHA256作成に必要なKeyは、営業チームを通じて提供されます。**</mark>**)**

***

:heavy\_check\_mark: $timeStamp$nonce$暗号化されたUser識別子

上述の値をHmacSHA256 Hash -> Base64 Url Encodingを通じてSignatureを生成します。

***

* timeStamp -> unix timestamp seconds
* nonce -> 文字列32字(ランダムに生成された文字列32字)
* user識別子 -> 会員区分が可能な識別子
{% endhint %}

<table data-full-width="false"><thead><tr><th width="127">Name</th><th width="141">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>sign</code></td><td>string</td><td><p> <code>timestmap.nonce.encryptedUserId.signature</code></p><hr><p> <mark style="background-color:red;">timestamp, nonce, userid の値は、<strong>署名の生成に使用された値</strong>を渡します。</mark></p></td></tr></tbody></table>



```
// get使用例
https://api-{env}.treasurecomics.com/external/recommendation?sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ
```

### **Response**

<table><thead><tr><th width="239">Fields</th><th width="106">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>recommendationSN</code></td><td>number</td><td>シーケンス</td></tr><tr><td><code>title</code></td><td>string</td><td>タイトル</td></tr><tr><td><code>description</code></td><td>string</td><td>内容</td></tr><tr><td><code>thumbnail</code></td><td>string</td><td>画像パス</td></tr><tr><td><code>contentType</code></td><td>string</td><td>ウェブコミック｜ウェブ小説</td></tr><tr><td><code>contentCName</code></td><td>string</td><td>作品キー</td></tr><tr><td><code>episodeNo</code></td><td>number</td><td>エピソード番号</td></tr><tr><td><code>genre</code></td><td>string</td><td>ジャンル</td></tr><tr><td><code>link</code></td><td>string</td><td><p>提供されるリンクの後にsignを付けて伝達</p><p>例)<code>&#x26;sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ</code></p></td></tr><tr><td><code>returnUrl</code></td><td>string</td><td>最終移動リンク(参考用)</td></tr><tr><td><code>order</code></td><td>number</td><td>表示優先順位(同一値が存在)</td></tr><tr><td><code>recommendationDate</code></td><td>string</td><td>推薦日(yyyy-MM-dd)</td></tr></tbody></table>

**レスポンス コード**

{% tabs %}
{% tab title="200" %}
{% code lineNumbers="true" %}
```json
[
  {
    "recommendationSN": 5,
    "title": "献身感とラブレター",
    "description": "献身感とラブレターテスト",
    "thumbnail": "https://s.treasurecomics.com/images/test/webtoon/cw631ac7ba1f/thumbnailFile_1718001726.jpg",
    "contentType": "ウェブコミック",
    "contentCName": "cw631ac7ba1f",
    "episodeNo": 1,
    "genre": "武侠,ドラマ",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fwebtoon%2Fviewer%2Fcw631ac7ba1f%2F1",
    "returnUrl": "https://test.treasurecomics.com/webtoon/viewer/cw631ac7ba1f/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  },
  {
    "recommendationSN": 8,
    "title": "私は覇王だ",
    "description": "こんな覇王存在でしょうか？",
    "thumbnail": "https://s.treasurecomics.com/images/test/novel/cn718f1595fc/thumbnailFile_1718001368.jpg",
    "contentType": "ウェブ小説",
    "contentCName": "cn718f1595fc",
    "episodeNo": 1,
    "genre": "武侠",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fnovel%2Fviewer%2Fcn718f1595fc%2F1",
    "returnUrl": "https://test.treasurecomics.com/novel/viewer/cn718f1595fc/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  },
  {
    "recommendationSN": 7,
    "title": "全てを打ち倒す天才会計士",
    "description": "こんな会計士がいるでしょうか？",
    "thumbnail": "https://s.treasurecomics.com/images/test/novel/cn0d3b6afccd/thumbnailFile_1718000646.jpg",
    "contentType": "ウェブ小説",
    "contentCName": "cn0d3b6afccd",
    "episodeNo": 1,
    "genre": "対代史",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fnovel%2Fviewer%2Fcn0d3b6afccd%2F1",
    "returnUrl": "https://test.treasurecomics.com/novel/viewer/cn0d3b6afccd/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  },
  {
    "recommendationSN": 9,
    "title": "無情なあなたへ死を",
    "description": "一緒に死ね",
    "thumbnail": "https://s.treasurecomics.com/images/test/novel/cn3a0d0de7e6/thumbnailFile_1718000377.jpg",
    "contentType": "ウェブ小説",
    "contentCName": "cn3a0d0de7e6",
    "episodeNo": 1,
    "genre": "スポーツ",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fnovel%2Fviewer%2Fcn3a0d0de7e6%2F1",
    "returnUrl": "https://test.treasurecomics.com/novel/viewer/cn3a0d0de7e6/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  },
  {
    "recommendationSN": 4,
    "title": "Oh! My メイドさん",
    "description": "Oh! My メイドさん テスト",
    "thumbnail": "https://s.treasurecomics.com/images/test/webtoon/cw3a81e99b70/thumbnailFile_1717999374.jpg",
    "contentType": "ウェブコミック",
    "contentCName": "cw3a81e99b70",
    "episodeNo": 1,
    "genre": "ロマンチックファンタジー",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fwebtoon%2Fviewer%2Fcw3a81e99b70%2F1",
    "returnUrl": "https://test.treasurecomics.com/webtoon/viewer/cw3a81e99b70/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  },
  {
    "recommendationSN": 6,
    "title": "ビートを刻む思春期皇子",
    "description": "ステージ上でビートを刻む",
    "thumbnail": "https://s.treasurecomics.com/images/test/novel/cnb998dc34fc/thumbnailFile_1717999357.jpg",
    "contentType": "ウェブトゥーン",
    "contentCName": "cnb998dc34fc",
    "episodeNo": 1,
    "genre": "現代ファンタジー",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fnovel%2Fviewer%2Fcnb998dc34fc%2F1",
    "returnUrl": "https://test.treasurecomics.com/novel/viewer/cnb998dc34fc/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  }
]
```
{% endcode %}
{% endtab %}

{% tab title="499" %}
{% code lineNumbers="true" %}
```json
{
  "code": "err_already_used_signature",
  "message": "既に使用された署名です。",
  "data": null,
  "appendix": {
    "reason": "既に使用された署名です。",
    "stack": "Error: UNHANDLED\n    at _validateSignature (/var/app/current/build/controllers/external/toss/recentView/get.1.0.0.js:33:15)\n    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)"
  }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### レスポンスエラーコード

<table><thead><tr><th width="307">Code</th><th>Reason</th><th>Message</th></tr></thead><tbody><tr><td><mark style="color:red;"><code>err_invalid_signature</code></mark></td><td>Signatureの確認に失敗</td><td>無効なSignatureです。</td></tr><tr><td><mark style="color:red;"><code>err_already_used_signature</code></mark></td><td>使用されたSignatureの再利用<br>-> 5分間制限</td><td>既に使用されたSignatureです。</td></tr></tbody></table>

***

## 推奨コンテンツリスト実装画面例

### 例1

<div align="left"><figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption><p>例1</p></figcaption></figure></div>

***

### 例2

<div align="left"><figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure></div>

