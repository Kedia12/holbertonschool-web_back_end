#!/usr/bin/env python3
"""Module providing MongoDB queries for a school collection."""


def list_all(mongo_collection):
    """List all documents in a collection.

    Args:
        mongo_collection: The MongoDB collection object.

    Returns:
        A list of all documents in the collection.
    """
    return list(mongo_collection.find())
    