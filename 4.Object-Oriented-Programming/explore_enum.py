from enum import Enum


class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    COMPLETED = 3
    CANCELLED = 4
    PRE_PROCESSING = 5
    SHIPPING = 6


# print(OrderStatus.PENDING.value)
# print(OrderStatus.PROCESSING.value)
# print(OrderStatus.COMPLETED.value)
# print(OrderStatus.CANCELLED.value)

order_status = 1

if order_status == OrderStatus.PENDING.value:
    print("Pending")
elif order_status == OrderStatus.PROCESSING.value:
    print("Processing")
elif order_status == OrderStatus.COMPLETED.value:
    print("Completed")
elif order_status == OrderStatus.CANCELLED.value:
    print("Cancelled")
else:
    print("No Order")


