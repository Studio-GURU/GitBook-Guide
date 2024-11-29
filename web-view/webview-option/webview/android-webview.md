---
icon: android
---

# Android WebView

## 신뢰하지 않는 인증서

일부 웹사이트에서 신뢰할 수 없는 인증서를 사용할 경우, 사용자에게 경고창이 표시되며 계속 진행할지 여부를 묻습니다.

{% code lineNumbers="true" %}
```kotlin
class InnerWebViewClient: WebViewClient() {
    override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?) {
        val innerContext = view?.context ?: return
        val alertBuilder: AlertDialog.Builder = AlertDialog.Builder(innerContext)
        alertBuilder.setMessage("이 사이트의 보안 인증서는 신뢰하는 보안 인증서가 아닙니다.\n\n계속하시겠습니까?")
        alertBuilder.setPositiveButton("계속하기") { _, _ -> handler?.proceed() }
        alertBuilder.setNegativeButton("취소") { _, _ -> handler?.cancel() }
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

## Scheme 처리

WebView::shouldOverrideUrlLoading을 통해 전달된 scheme 처리에 대한 방법을 가이드합니다.

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

schem market 처리 방식을 안내합니다.

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









