Generate python stubs from proto file in src directory:
```bash
python -m grpc_tools.protoc -I../../jdplus-ws/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../../jdplus-ws/src/main/proto/jdplus/main/ws/v1/toolkit_messages.proto
python -m grpc_tools.protoc -I../../jdplus-ws/src/main/proto --python_out=. --pyi_out=. --grpc_python_out=. ../../jdplus-ws/src/main/proto/jdplus/main/ws/v1/toolkit_basic.proto
```
