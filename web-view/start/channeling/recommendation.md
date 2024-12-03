---
description: ユーザーが閲覧したコンテンツに基づくレコメンデーションリストAPIの使用方法について説明します。
icon: thumbs-up
---

# レコメンデーションコンテンツ一覧の照会

## バージョン

バージョン情報はURL経路に表現せず、ヘッダーのaccept-version属性値に定義します。

| Version | Date       | Description |
| ------- | ---------- | ----------- |
| 1.0.0   | 2024.08.23 | Create      |

## レコメンデーションコンテンツ

<mark style="color:green;">`GET`</mark> `https://api-{env}.treasurecomics.com/external/recommendation?sign={value}`

レコメンデーションコンテンツ一覧を返します。

### ヘッダー

| Name           | Value              |
| -------------- | ------------------ |
| Content-Type   | `application/json` |
| Authorization  | `Basic token`      |
| Accept-Version | `1.0.0`            |

### **ボディ**

{% hint style="info" %}
**シグネチャの生成（**<mark style="color:red;">**HmacSHA256生成に必要なKeyは営業チームより提供されます**</mark>**）**

***

:heavy_check_mark: $timeStamp$nonce$暗号化されたユーザー識別子

上記の値をHmacSHA256 Hash -> Base64 Url Encodingを通じてシグネチャを生成します。

***

* timeStamp -> unixタイムスタンプ（秒）
* nonce -> 32文字の文字列（ランダムに生成された32文字）
* ユーザー識別子 -> 会員を区別できる識別子
{% endhint %}

<table data-full-width="false"><thead><tr><th width="127">Name</th><th width="141">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>sign</code></td><td>string</td><td><p> <code>timestmap.nonce.encryptedUserId.signature</code></p><hr><p> <mark style="background-color:red;">timestamp、nonce、useridの値は<strong>シグネチャ生成に使用された値</strong>を渡します。</mark></p></td></tr></tbody></table>
// get usage example
https://api-{env}.treasurecomics.com/external/recommendation?sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ
### **レスポンス**

<table><thead><tr><th width="239">Fields</th><th width="106">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>recommendationSN</code></td><td>number</td><td>シーケンス</td></tr><tr><td><code>title</code></td><td>string</td><td>タイトル</td></tr><tr><td><code>description</code></td><td>string</td><td>内容</td></tr><tr><td><code>thumbnail</code></td><td>string</td><td>画像パス</td></tr><tr><td><code>contentType</code></td><td>string</td><td>ウェブトゥーン | ウェブ小説</td></tr><tr><td><code>contentCName</code></td><td>string</td><td>作品キー</td></tr><tr><td><code>episodeNo</code></td><td>number</td><td>エピソード番号</td></tr><tr><td><code>genre</code></td><td>string</td><td>ジャンル</td></tr><tr><td><code>link</code></td><td>string</td><td><p>提供されるリンクの後ろにsignを付けて渡す</p><p>例：<code>&sign=1724328195.3da08653e6c1420aac89eecdf5c20063.OGMzYjUzYTUyYjE1YTJiNDAyZGM3MGJiZmMzMDI2YWE1NDg0YWY2ZTdjNjMyZTJlMTdjMjQyOGU1NjZhYjdhYQ</code></p></td></tr><tr><td><code>returnUrl</code></td><td>string</td><td>最終遷移リンク（参考用）</td></tr><tr><td><code>order</code></td><td>number</td><td>表示優先順位（同じ値が存在可能）</td></tr><tr><td><code>recommendationDate</code></td><td>string</td><td>レコメンデーション日付（yyyy-MM-dd）</td></tr></tbody></table>

**レスポンスコード**

{% tabs %}
{% tab title="200" %}
{% code lineNumbers="true" %}
```json
[
  {
    "recommendationSN": 5,
    "title": "風紀委員と恋文",
    "description": "風紀委員と恋文 test",
    "thumbnail": "https://s.treasurecomics.com/images/test/webtoon/cw631ac7ba1f/thumbnailFile_1718001726.jpg",
    "contentType": "ウェブトゥーン",
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
    "title": "我は覇王なり",
    "description": "こんな覇王が存在する？",
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
    "title": "全てを叩き潰す天才会計士",
    "description": "こんな会計士がいるのか？",
    "thumbnail": "https://s.treasurecomics.com/images/test/novel/cn0d3b6afccd/thumbnailFile_1718000646.jpg",
    "contentType": "ウェブ小説",
    "contentCName": "cn0d3b6afccd",
    "episodeNo": 1,
    "genre": "歴史改変",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fnovel%2Fviewer%2Fcn0d3b6afccd%2F1",
    "returnUrl": "https://test.treasurecomics.com/novel/viewer/cn0d3b6afccd/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  },
  {
    "recommendationSN": 9,
    "title": "無情なあなたに死を",
    "description": "共に死のう",
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
    "title": "ああ！我がメイド様",
    "description": "ああ！我がメイド様 test",
    "thumbnail": "https://s.treasurecomics.com/images/test/webtoon/cw3a81e99b70/thumbnailFile_1717999374.jpg",
    "contentType": "ウェブトゥーン",
    "contentCName": "cw3a81e99b70",
    "episodeNo": 1,
    "genre": "ロマンティックファンタジー",
    "link": "https://test.treasurecomics.com/gateway/common?returnUrl=https%3A%2F%2Ftest.treasurecomics.com%2Fwebtoon%2Fviewer%2Fcw3a81e99b70%2F1",
    "returnUrl": "https://test.treasurecomics.com/webtoon/viewer/cw3a81e99b70/1",
    "order": 1,
    "recommendationDate": "2024-08-22"
  },
  {
    "recommendationSN": 6,
    "title": "ビートを刻む世子",
    "description": "ステージの上でビートを刻もう",
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
{% endcode %}
{% endtab %}
{% tab title="499" %}
{% code lineNumbers="true" %}
{
  "code": "err_already_used_signature",
  "message": "既に使用されたシグネチャです。",
  "data": null,
  "appendix": {
    "reason": "既に使用されたシグネチャです。",
    "stack": "Error: UNHANDLED\n    at _validateSignature (/var/app/current/build/controllers/external/toss/recentView/get.1.0.0.js:33:15)\n    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)"
  }
}
{% endcode %}
{% endtab %}
{% endtabs %}
レスポンスエラーコード
<table><thead><tr><th width="307">Code</th><th>Reason</th><th>Message</th></tr></thead><tbody><tr><td><mark style="color:red;"><code>err_invalid_signature</code></mark></td><td>シグネチャ検証失敗</td><td>無効なシグネチャです。</td></tr><tr><td><mark style="color:red;"><code>err_already_used_signature</code></mark></td><td>使用済みシグネチャの再使用<br>-> 5分間制限</td><td>既に使用されたシグネチャです。</td></tr></tbody></table>

レコメンデーションコンテンツ一覧実装画面例
<div align="left"><figure><img src="../../../.gitbook/assets/bms_recommendation_2.png" alt="" width="375"><figcaption></figcaption></figure></div>
```
