class ClearMessagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 在每個 request 前執行
        self.process_request(request)
        response = self.get_response(request)
        # 在每個 response 前執行
        response = self.process_response(request, response)
        return response

    def process_request(self, request):
        # 清空現有的訊息
        from django.contrib import messages
        storage = messages.get_messages(request)
        for message in storage:
            pass  # Do nothing, just iterate to clear messages

    def process_response(self, request, response):
        # 在處理 response 前執行的操作
        return response


