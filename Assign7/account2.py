import pika
import time
import sys

check = False

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='CS361 Message')

friends = []

def callback(ch, method, properties, body):
    global check
    ctr = 1
    print(" [x] received %r" % body)

    if check == False:
        friends.append(body)
        check = True
        for i in friends:
            print(str(ctr) + ". " + i.decode('utf-8'))
            ctr += 1

    else:
        if body in friends:
            print("Already in friends list!")
        else:
            friends.append(body)
            for i in friends:
                print(str(ctr) + ". " + i.decode('utf-8'))
                ctr += 1
    

channel.basic_consume(queue='CS361 Message', auto_ack=True, on_message_callback=callback)

channel.start_consuming()


if __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)