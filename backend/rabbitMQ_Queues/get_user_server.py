import asyncio
import logging

from aio_pika import Message, connect
from aio_pika.abc import AbstractIncomingMessage

from db_connection.db_service import get_user


async def main() -> None:
    # Perform connection
    connection = await connect("amqp://guest:guest@rabbitmq/")

    # Creating a channel
    channel = await connection.channel()
    exchange = channel.default_exchange

    # Declaring queue
    queue = await channel.declare_queue("get_user_queue")

    print(" [x] Awaiting RPC requests")

    # Start listening the queue with name 'hello'
    async with queue.iterator() as qiterator:
        message: AbstractIncomingMessage
        async for message in qiterator:
            try:
                async with message.process(requeue=False):
                    assert message.reply_to is not None

                    user_id = int(message.body.decode())

                    response = get_user(conn, user_id)

                    await exchange.publish(
                        Message(
                            body=response,
                            correlation_id=message.correlation_id,
                        ),
                        routing_key=message.reply_to,
                    )
                    print("Request complete")
            except Exception:
                logging.exception("Processing error for message %r", message)
#
# if __name__ == "__main__":
#     asyncio.run(main())