#!/usr/bin/env python3
"""Module providing MongoDB queries for a school collection."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools that offer a specific topic.

    Args:
        mongo_collection: The MongoDB collection object.
        topic: The topic to search for in the schools' topics.

    Returns:
        A list of schools that have the specified topic in their topics field.
    """
    return list(mongo_collection.find({"topics": topic}))
    