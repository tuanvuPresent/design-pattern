"""
Pattern này được sử dụng khi code của bạn phải phụ thuộc vào
một thư viện bên ngoài hoặc 1 class khác mà có sự thay đổi một cách thường xuyên.

Pattern này là một loại thuộc structural patterns
bởi vì nó giúp bạn tổ chức code một cách hiệu quả giúp cho việc quản lý và mở rộng dễ dàng hơn.
"""


# third library example
class Paypal:
    def send_payment(self, amount):
        print('send', amount)


class PaypalAdapter:
    def __init__(self, paypal: Paypal):
        self._paypal = paypal

    def pay(self, amount):
        self._paypal.send_payment(amount)


paypal = PaypalAdapter(Paypal())
paypal.pay('1000')
