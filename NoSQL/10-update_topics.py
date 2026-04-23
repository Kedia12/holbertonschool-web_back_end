#!/usr/bin/env python3
"""Module providing MongoDB queries for a school collection."""


def update_topics(mongo_collection, name, topics):
    """Update the topics of a document in a collection.

    Args:
        mongo_collection: The MongoDB collection object.
        name: The name of the document to update.
        topics: A list of topics to set for the document.

    Returns:
        The number of documents updated.
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
    