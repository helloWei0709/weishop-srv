import grpc
from user_srv.proto import user_pb2, user_pb2_grpc

class UserTest:
    def __init__(self):
        # 连接grpc服务器
        channel = grpc.insecure_channel("127.0.0.1:50051")
        self.stub = user_pb2_grpc.UserStub(channel)

    def user_list(self):
        rsp = self.stub.GetUserList(user_pb2.PageInfo(pn=2, pSize=2))
        print(rsp.total)
        print(rsp.data)
        for user in rsp.data:
            print(user.id)
            print(user.mobile)

    def get_user_by_id(self):
        rsp = self.stub.GetUserById(user_pb2.IdRequest(id=30))
        print(rsp)


if __name__ == '__main__':
    user_test = UserTest()
    # user_test.user_list()
    user_test.get_user_by_id()