from collections import OrderedDict

# 예시 딕셔너리 (간략화)
network = {
    "agent": {
        "step1.5": {
            "nn1": {"type": "rnn"}
        },
        "step2": {
            "nn1": {"type": "cnn"}
        },
        "step1": {
            "nn1": {"type": "mlp"}
        }
    }
}

# 정렬 적용
network["agent"] = dict(sorted(network["agent"].items()))

# 결과 확인
print(network)
