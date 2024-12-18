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

{% code lineNumbers="true" %}
```kotlin
private fun actionIntentTask(viewContext: Context, webView: WebView?, url: String): Boolean {
    val actionWebView = webView ?: return false
    val actionActivity = viewContext as? Activity ?: return false
    val actionIntent = try {
        Intent.parseUri(url, Intent.URI_INTENT_SCHEME)
    } catch (e: Exception) {
        // error
        null        
    }

    // check intent
    if (actionIntent == null) {
        Log.e("TAG", "intent is null")
        return false
    }

    try {
        // Fallback URL -> Loading WebView For Kakao
        val fallbackUrl = actionIntent.getStringExtra("browser_fallback_url")
        if (fallbackUrl != null) {
            actionWebView.loadUrl(fallbackUrl)
            return true
        }
        
        // action
        val actionPackageName = actionIntent.`package` ?: ""
        if (actionPackageName.isNotEmpty()) {
            // launch activity
            val launchIntent = viewContext.packageManager.getLaunchIntentForPackage(actionPackageName)
            if (launchIntent != null) {
                actionActivity.startActivity(launchIntent)
                return true
            }
        }
        
        // market
        if (actionPackageName.isNotEmpty()) {
            try {
                val marketIntent = Intent(Intent.ACTION_VIEW)
                marketIntent.data = Uri.parse("market://details?id=$actionPackageName")
                actionActivity.startActivity(marketIntent)
                return true
            } catch (e: Exception) {
                // error
            }
        }
    } catch (e: Exception) {
            // error
        }
    }
    return false
}
```
{% endcode %}

***

### Market

スキームマーケット処理方式についてご案内します。

{% code lineNumbers="true" %}
```kotlin
private fun actionMarketTask(viewContext: Context, url: String): Boolean {
    val activity = viewContext as? Activity ?: return false
    kotlin.runCatching {
        val id = Uri.parse(url).getQueryParameter("id")
        val marketIntent = Intent(Intent.ACTION_VIEW).apply {
            data = Uri.parse("market://details?id=$id")
        }
        if (marketIntent.resolveActivity(viewContext.packageManager) != null) {
            activity.startActivity(marketIntent)
        } else {
            val viewIntent = Intent(Intent.ACTION_VIEW).apply {
                data = Uri.parse("https://play.google.com/store/apps/details?id=$id")
            }
            activity.startActivity(viewIntent)
        }
    }.onFailure {
        // error
    }
    return true
}
```
{% endcode %}

***

### Mailto

{% code lineNumbers="true" %}
```kotlin
private fun actionMailToTask(viewContext: Context, uri: Uri): Boolean {
    val activity = viewContext as? Activity ?: return false
    kotlin.runCatching {
        activity.startActivity(Intent(Intent.ACTION_VIEW, uri))
    }.onFailure {
        tales.error(moduleName = moduleName, throwable = it, trace = { "actionMailToTask { uri: $uri }" })
        it.message?.produce { message -> ToastView.show(context = viewContext, message = message) }
    }
    return true
}
```
{% endcode %}

***

### Tel

{% code lineNumbers="true" %}
```kotlin
private fun actionTelTask(viewContext: Context, uri: Uri): Boolean {
    val activity = viewContext as? Activity ?: return false
    kotlin.runCatching {
        activity.startActivity(Intent(Intent.ACTION_DIAL, uri))
    }.onFailure {
        // error
    }
    return true
}
```
{% endcode %}
