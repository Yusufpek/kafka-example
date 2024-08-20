from kafka import KafkaConsumer

while True:
    try:
        print('Welcome to parse engine')
        consumer = KafkaConsumer(
            'test',
            bootstrap_servers='172.19.0.3:9092')

        for message in consumer:
            print(f"""
                topic: {message.topic}
                parttion: {message.partition}
                offset: {message.offset}
                =========================
                key:{message.key}
                value: {message.value}""")
    except Exception as e:
        print(e)
        # Logs the error appropriately.
        pass
