from confluent_kafka import Consumer

conf = {'bootstrap.servers': "81.177.140.38:9092,host2:9092",
        'group.id': "foo",
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)
