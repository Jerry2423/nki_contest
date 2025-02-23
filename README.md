## Performance Log

- Incoporated `fused_attention` into `llama.py`.
- There is a substantial difference in the program's performance when run twice with `python main.py --mode  evaluate  --fused-qkv`
- First run:
```json
{
    "e2e_model": {
        "latency_ms_p50": 279.6248197555542,
        "latency_ms_p90": 303.92990112304705,
        "latency_ms_p95": 380.8887243270874,
        "latency_ms_p99": 391.26086711883545,
        "latency_ms_p100": 393.85390281677246,
        "latency_ms_avg": 292.65953302383423,
        "throughput": 218.68414583572726
    },
    "context_encoding_model": {
        "latency_ms_p50": 29.15823459625244,
        "latency_ms_p90": 29.37626838684082,
        "latency_ms_p95": 29.427039623260498,
        "latency_ms_p99": 29.77475881576538,
        "latency_ms_p100": 29.8616886138916,
        "latency_ms_avg": 29.22142744064331,
        "throughput": 1095.0868182261365
    },
    "token_generation_model": {
        "latency_ms_p50": 6.929159164428711,
        "latency_ms_p90": 7.124996185302734,
        "latency_ms_p95": 7.4158430099487305,
        "latency_ms_p99": 7.717504501342768,
        "latency_ms_p100": 7.825374603271484,
        "latency_ms_avg": 6.997509925596176,
        "throughput": 147.51791358526475
    }
}
Completed saving result to benchmark_report.json
Final Score: 1.093050539312594
        Accuracy: True
        Latency: 391.26086711883545
        Throughput: 218.68414583572726
        NKI FLOPs Ratio: 0.9925336919440101
```

- Second run:
```json
Benchmark completed and its result is as following
{
    "e2e_model": {
        "latency_ms_p50": 280.55477142333984,
        "latency_ms_p90": 286.90123558044434,
        "latency_ms_p95": 288.60626220703125,
        "latency_ms_p99": 290.02830505371094,
        "latency_ms_p100": 290.38381576538086,
        "latency_ms_avg": 281.625759601593,
        "throughput": 227.25193920662215
    },
    "context_encoding_model": {
        "latency_ms_p50": 29.159903526306152,
        "latency_ms_p90": 29.388952255249023,
        "latency_ms_p95": 29.401862621307373,
        "latency_ms_p99": 29.4284987449646,
        "latency_ms_p100": 29.435157775878906,
        "latency_ms_avg": 29.21386957168579,
        "throughput": 1095.3701262161635
    },
    "token_generation_model": {
        "latency_ms_p50": 6.915450096130371,
        "latency_ms_p90": 7.072234153747559,
        "latency_ms_p95": 7.115137577056885,
        "latency_ms_p99": 7.474346160888672,
        "latency_ms_p100": 7.621288299560547,
        "latency_ms_avg": 6.961395279053719,
        "throughput": 148.28321380084694
    }
}
Completed saving result to benchmark_report.json
Final Score: 1.5323450528578704
        Accuracy: True
        Latency: 290.02830505371094
        Throughput: 227.25193920662215
        NKI FLOPs Ratio: 0.9925336919440101
```