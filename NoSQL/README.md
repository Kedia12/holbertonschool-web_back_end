# NoSQL

## What is NoSQL?
NoSQL means **Not Only SQL**.  
It refers to non-relational databases designed for flexible, scalable, and fast data storage.

## SQL vs NoSQL
- **SQL**: tables, rows, fixed schema
- **NoSQL**: documents, key-value, flexible schema

## ACID
ACID means:
- **Atomicity**
- **Consistency**
- **Isolation**
- **Durability**

It describes reliable transaction rules, mainly in SQL databases.

## Document Store
A document store saves data as **documents**, often like JSON.

Example:
```json
{
  "name": "Alice",
  "age": 22
}

## Types of NoSQL

Document databases
Key-value databases
Column-family databases
Graph databases

##Benefits of NoSQL

Flexible schema
Easy scaling
Good for large data
Fast for modern apps

##MongoDB

MongoDB is a document-oriented NoSQL database.

## Main terms
Database → contains collections
Collection → contains documents
Document → one record
Field → one key-value pair

## Common MongoDB Commands

Show databases
show dbs

Use a database
use my_db

Show collections
show collections

Insert
db.users.insertOne({ name: "Alice", age: 22 })

Find
db.users.find()

Update
db.users.updateOne(
  { name: "Alice" },
  { $set: { age: 23 } }
)

Delete
db.users.deleteOne({ name: "Alice" })

Query Operators
$gt → greater than
$lt → less than
$gte → greater than or equal
$lte → less than or equal
$in → value in a list
$or → logical OR

Aggregation

Aggregation is used to group and summarize data.

Example:

db.users.aggregate([
  { $group: { _id: "$city", total: { $sum: 1 } } }
])
PyMongo

PyMongo lets Python work with MongoDB.

Example:

from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.my_db
collection = db.users

Quick Summary

NoSQL = non-relational database
MongoDB = document database
Data is stored as JSON-like documents
Good for flexible and scalable applications
