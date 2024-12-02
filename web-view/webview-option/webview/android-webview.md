---
icon: android
---

# Android WebView

## 信頼されていない証明書

一部のウェブサイトで信頼できない証明書を使用している場合、ユーザーに警告ダイアログが表示され、続行するかどうかを確認します。

{% code lineNumbers="true" %}
```kotlin
class InnerWebViewClient: WebViewClient() {
    override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?) {
        val innerContext = view?.context ?: return
        val alertBuilder: AlertDialog.Builder = AlertDialog.Builder(innerContext)
        alertBuilder.setMessage("このサイトのセキュリティ証明書は信頼された証明書ではありません。\n\n続行しますか？")
        alertBuilder.setPositiveButton("続行する") { _, _ -> handler?.proceed() }
        alertBuilder.setNegativeButton("キャンセル") { _, _ -> handler?.cancel() }
        val alertDialog = alertBuilder.create()
        alertDialog.show()
        // width 90%
        runCatching {
            val params: WindowManager.LayoutParams? = alertDialog?.window?.attributes
            params?.width = (innerContext.resources.displayMetrics.widthPixels * 0.9).toInt()
            alertDialog?.window?.attributes = params as WindowManager.LayoutParams
        }
    }
}
```
{% endcode %}

***

## スキーム処理

WebView::shouldOverrideUrlLoadingを通じて渡されたスキーム処理についての方法をガイドします。

### intent

[Previous intent code block remains unchanged]

***

### Market

スキームマーケット処理方式についてご案内します。

[Previous Market code block remains unchanged]

***

### Mailto

[Previous Mailto code block remains unchanged]

***

### Tel

[Previous Tel code block remains unchanged]
