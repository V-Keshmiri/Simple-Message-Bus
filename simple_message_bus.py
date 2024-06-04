"""
Author: Vahid Keshmiri
Email: V.Keshmiry@Gmail.com

This module implements a simple message bus architecture with event emitters. The message bus 
facilitates efficient communication between different components of a system by allowing them 
to publish and subscribe to events.
"""

from typing import Callable, Dict, List

class MessageBus:
    """
    A simple message bus for event-driven communication.
    """

    def __init__(self):
        """
        Initializes the message bus with an empty list of subscribers for each event type.
        """
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, handler: Callable):
        """
        Subscribes a handler to an event type.

        Parameters:
        event_type (str): The type of event to subscribe to.
        handler (Callable): The handler function to call when the event is published.
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    def publish(self, event_type: str, data: dict):
        """
        Publishes an event to all subscribed handlers.

        Parameters:
        event_type (str): The type of event to publish.
        data (dict): The data to pass to the event handlers.
        """
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                handler(data)

# Example usage
def handle_chat_message(data: dict):
    """
    Handles chat messages by printing them.

    Parameters:
    data (dict): The data containing the chat message.
    """
    print(f"Handling chat message: {data['message']}")

if __name__ == "__main__":
    bus = MessageBus()
    bus.subscribe("chat_message", handle_chat_message)
    bus.publish("chat_message", {"message": "Hello, World!"})
