## Performance Log

```json
{
    "e2e_model": {
        "latency_ms_p50": 297.88315296173096,
        "latency_ms_p90": 315.1472568511963,
        "latency_ms_p95": 316.3021683692932,
        "latency_ms_p99": 317.144558429718,
        "latency_ms_p100": 317.3551559448242,
        "latency_ms_avg": 303.3171057701111,
        "throughput": 211.00029896931244
    },
    "context_encoding_model": {
        "latency_ms_p50": 24.80900287628174,
        "latency_ms_p90": 25.102543830871582,
        "latency_ms_p95": 25.124680995941162,
        "latency_ms_p99": 25.14479398727417,
        "latency_ms_p100": 25.149822235107422,
        "latency_ms_avg": 24.89844560623169,
        "throughput": 1285.2207927385998
    },
    "token_generation_model": {
        "latency_ms_p50": 7.369399070739746,
        "latency_ms_p90": 7.651567459106445,
        "latency_ms_p95": 7.675564289093017,
        "latency_ms_p99": 8.088569641113281,
        "latency_ms_p100": 8.357524871826172,
        "latency_ms_avg": 7.454710237441525,
        "throughput": 138.47058190559565
    }
}
Completed saving result to benchmark_report.json
Final Score: 1.3007382924260704
        Accuracy: True
        Latency: 317.144558429718
        Throughput: 211.00029896931244
        NKI FLOPs Ratio: 0.9919591850284661
```