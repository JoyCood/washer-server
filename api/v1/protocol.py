import common_1_pb2 as common_pb2

route = {
    common_pb2.REGISTER: "register",
    common_pb2.LOGIN: "login",
    common_pb2.REQUEST_AUTHCODE: "request_authcode",
    common_pb2.VERIFY_AUTHCODE: "verify_authcode",
    common_pb2.FRESH_LOCATION: "fresh_location",
    common_pb2.START_WORK: "start_work",
    common_pb2.STOP_WORK: "stop_work",
    common_pb2.FINISH_ORDER: "finish_order",
    common_pb2.PROCESSING_ORDER: "processing_order",
    common_pb2.ORDER_FEEDBACK: "order_feedback",
    common_pb2.CANCEL_ORDER: "cancel_order",
    common_pb2.HISTORY_ORDER: "history_order",
    common_pb2.ORDER_DETAIL: "order_detail",
    common_pb2.LOGOUT: "logout"
}
