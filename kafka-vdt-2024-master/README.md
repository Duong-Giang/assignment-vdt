# Set up Kafka - Nifi

> Required: Máy cần cài đặt sẵn Docker. Cấu hình máy cần RAM >= 8GB. Môi trường thử nghiệm: Window 11



**B1:** Chạy lệnh docker compose 
```sh
docker compose -f docker-compose.zk-kafka.yml -p vdt-kafka-zk up -d
```
Các cấu hình của Kafka Broker xem tại [đây](https://docs.confluent.io/platform/current/installation/configuration/broker-configs.html)

**B2:** Truy cập vào link [Kafka UI](http://localhost:8080) sẽ thấy kết quả như hình

![Result 1](../master/assets/result-1.png)


**B3:** Cd vao csv2kafka chay lenh 
```sh
python3 producer.py
```
de push du lieu tu folder data len kafka topic
