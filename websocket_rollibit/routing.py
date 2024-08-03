from django.urls import re_path
from ws_rollibit import consumers

websocket_urlpatterns = [
    # 匹配：?P<group>  ---> 将匹配的结果存储在一个名为 group 的变量中
    # \w+ 匹配一个或多个字母数字字符或下划线
    # (?P<group>\w+)  所以这句的意思是，匹配一个或多个字母数字字符或下划线。并将其放置到group变量中
    # /$  表示匹配到字符串的末尾
    re_path(r'ws/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi())
]