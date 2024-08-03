from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, event):
        # 客户端尝试连接时调用
        print("连接成功")
        group=self.scope['url_route']['kwargs'].get("group")
        self.accept()
        # 将客户端的链接对象加入到（内存 or redis）
        async_to_sync(self.channel_layer.group_add)(group, self.channel_name)


    def websocket_receive(self, event):
        #event包含了 WebSocket 事件的相关信息,如消息内容、消息类型等
        # event['text'] 是客户端发送的消息内容
        # event['type'] 是 WebSocket 事件类型，例如 'websocket.receive'
        # event['websocket'] 是 WebSocket 连接对象
        # event['reply_channel'] 是一个唯一的 reply_channel，用于向客户端发送消息
        # event['path'] 是请求的路径，例如 '/ws/chat/'
        # event['headers'] 是请求头信息
        # event['client'] 是客户端的 IP 地址和端口号
        # event['server'] 是服务器的 IP 地址和端口号
        # event['scheme'] 是请求的协议，例如 'ws' 或 'wss'
        # event['subprotocols'] 是客户端支持的子协议列表
        # event['extensions'] 是客户端支持的 WebSocket 扩展列表
        # event['params'] 是请求的参数，例如 '/ws/chat/?room_name=room1'
        # event['cookies'] 是请求的 cookies
        # event['query_string'] 是请求的查询字符串
        # event['method'] 是请求的方法，例如 'GET' 或 'POST'
        # event['path_info'] 是请求的路径信息
        print(event['text'])
        # 将消息回发给客户端
        # self.send(text_data=json.dumps({
        #     "text": "您的消息已收到"
        # }))

        async_to_sync(self.channel_layer.group_send)("123",{"type":"xx.oo","message":event['text']})
    def xx_oo(self,event):
        # text = json.loads(event['message'])
        # text = text_data_json['text']
        # 发送数据回 WebSocket 客户端
        self.send(text_data=json.dumps({
            'message': event['message']
        }))

    def websocket_disconnect(self, event):
        # 连接断开时调用
        # 处理断开连接的逻辑（如果有的话）
        # self.close()   服务端主动断开连接
        group=self.scope['url_route']['kwargs'].get("group")
        async_to_sync(self.channel_layer.group_discard)(group,self.channel_name)
        raise StopConsumer()