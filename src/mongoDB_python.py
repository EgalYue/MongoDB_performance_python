import os
import time
import random
import numpy as np
from pymongo import MongoClient
import pymongo

# Testing performance of MongoDB with Python
# Operation: Insert; Find; Update; Delete.

def compute_performance(count, average):
    """
    Computing the performance of mongoDB with Python.
    Operation: Insert; Find; Update; Delete.
    Args:
        count: number of each operation, e.g. 10 times insert...
        average: number of runs, in order to compute the average time consuming.

    The time consuming would be stored in one .txt file.
    """

    client = MongoClient() # default client
    db = client.test  # default database
    col_python = db.collection_python#

    # Used to store time consuming and compute the average time consuming for
    # each operation respectively.
    timeList_insert = []
    timeList_updateOneByOne = []
    timeList_updateOneRandom = []
    timeList_findOneByOne = []
    timeList_findOneRandom = []
    timeList_delete = []

    for n in range(0,average):
        print n+1," ------------------------------------------"
        #------------Following are the operations! e.g. insert update find delete-----
        insertOne(col_python, count, timeList_insert)
        updateOneByOne(col_python, count, timeList_updateOneByOne)
        updateOne_random(col_python, count, timeList_updateOneRandom)
        # showAll_data(col_python)
        findOneByOne(col_python, count, timeList_findOneByOne)
        findOne_random(col_python, count, timeList_findOneRandom)
        deleteOne(col_python, count, timeList_delete)
        #----------------------------------------------------------------------------

        # After testing, delete the collection from database!!!
        db.collection_python.drop()

    # compute the average time consuming by different operations
    averageTime_insert = np.mean(timeList_insert)
    averageTime_updateOneByOne = np.mean(timeList_updateOneByOne)
    averageTime_updateOneRandom = np.mean(timeList_updateOneRandom)
    averageTime_findOneByOne = np.mean(timeList_findOneByOne)
    averageTime_findRandom = np.mean(timeList_findOneRandom)
    averageTime_delete = np.mean(timeList_delete)

    print "================== " +str(average)+ " times Computation =================="
    print "averageTime_insert: %f[s]" % (averageTime_insert)
    print "averageTime_updateOneByOne: %f[s]" % (averageTime_updateOneByOne)
    print "averageTime_updateOneRandom: %f[s]" % (averageTime_updateOneRandom)
    print "averageTime_findOneByOne: %f[s]" % (averageTime_findOneByOne)
    print "averageTime_findRandom: %f[s]" % (averageTime_findRandom)
    print "averageTime_delete: %f[s]" % (averageTime_delete)

    # write to .txt file
    fileName = str(count)+"_data_timeConsuming.txt"
    out_path = os.path.dirname(os.path.abspath("results"))+"/results/"+fileName
    write_to_txt(out_path,averageTime_insert, averageTime_updateOneByOne,
                 averageTime_updateOneRandom, averageTime_findOneByOne,
                 averageTime_findRandom, averageTime_delete)

def insertOne(col_python, count, timeList_insert):
    """
    Insert data one by one.

    Args:
        col_python: collection name
        count: This is the number of inserts, e.g. if count = 10,
               which means we should insert 10 data
        timeList_insert: one list used to store the time consuming for inserting all data
    """
    start = time.time()

    for num_insert in range(0, count):
        # In PyMongo we use dictionaries to represent documents.
        dict_data = {'timestamp[s]': str(num_insert), 'tx[m]': '-0.00105005',
                     'ty[m]': '-0.00159259', 'tz[m]': '0', 'qx': '0', 'qy': '0',
                     'qz': '0.00128360443', 'qw[Hamilton]': '0.999999176'}
        col_python.insert_one(dict_data)

    end = time.time()
    timeList_insert.append(end - start)
    print "Insert operation time consuming: ", end - start

def createIndex(col_python):
    """
    Not used yet!
    """
    col_python.create_index([("timestamp[s]",pymongo.ASCENDING)], unique=True)

def updateOneByOne(col_python, count, timeList_updateOneByOne):
    """
    Update date one by one.
    Args:
        col_python: collection name
        count: This is the number of inserts, e.g. if count = 10,
               which means we should update 10 data randomly
        timeList_updateOneByOne: list used to store the time consuming for updating data
    """
    start = time.time()

    for num_update in range(0, count):
        col_python.update_one({"timestamp[s]": str(num_update)},
                              {'$set': {"qx": "1"}})

    end = time.time()
    timeList_updateOneByOne.append(end - start)
    print "Update operation(one by one) time consuming: ", end - start

def updateOne_random(col_python, count, timeList_updateOneRandom):
    """
    Update data without indexing.

    Args:
        col_python: collection name
        count: This is the number of inserts, e.g. if count = 10,
               which means we should update 10 data randomly
        timeList_updateOneRandom: one list used to store the time consuming for updating random data
    """
    start = time.time()

    for num_update in range(0, count):
        rand = random.randint(0, count - 1)  # [0, count-1]
        col_python.update_one({"timestamp[s]": str(rand)},
                              {'$set': {"qx": "2"}})

    end = time.time()
    timeList_updateOneRandom.append(end - start)
    print "Update operation(randomly) time consuming: ", end - start

def findOneByOne(col_python, count, timeList_findOneByOne):
    """
    Find one data.

    Args:
        col_python: collection name
        count: This is the number of inserts, e.g. if count = 10,
               which means we should find 10 data randomly
        timeList_findOneByOne: list used to store the time consuming for finding data
    """
    start = time.time()

    for num_find in range(count):
        col_python.find_one({"timestamp[s]": str(num_find)})

    end = time.time()
    timeList_findOneByOne.append(end - start)
    print "Find operation(one by one) time consuming: ", end - start

def findOne_random(col_python, count, timeList_findOneRandom):
    """
    Find one data.

    Args:
        col_python: collection name
        count: This is the number of inserts, e.g. if count = 10,
               which means we should find 10 data randomly
        timeList_findOneRandom: one list used to store the time consuming for finding random data
    """
    start = time.time()

    for num_find in range(count):
        rand = random.randint(0, count - 1)  # [0, count-1]
        col_python.find_one({"timestamp[s]": str(rand)})

    end = time.time()
    timeList_findOneRandom.append(end - start)
    print "Find operation(randomly) time consuming: ", end - start

def deleteOne(col_python, count, timeList_delete):
    """
    Delete data one by one.

    Args:
        col_python: collection name
        count: This is the number of inserts, e.g. if count = 10,
               which means we should delete  data randomly
        timeList_delete: one list used to store the time consuming for deleting all data
    """
    start = time.time()

    for num_delete in range(0, count):
        s = str(num_delete)
        col_python.delete_one({"timestamp[s]": s})

    end = time.time()
    timeList_delete.append(end - start)
    print "Delete operation time consuming: ", end - start

def showAll_data(col_python):
    for data in col_python.find():
        print data

def write_to_txt(out_path,averageTime_insert, averageTime_updateOneByOne,
                 averageTime_updateOneRandom, averageTime_findOneByOne,
                 averageTime_findRandom, averageTime_delete):
    """
    Write the time consuming into one txt file.
    """
    with open(out_path,"w") as f:
        f.write("averageTime_insert: ")
        f.write(str(averageTime_insert))
        f.write("\n")

        f.write("averageTime_updateOneByOne: ")
        f.write(str(averageTime_updateOneByOne))
        f.write("\n")

        f.write("averageTime_updateOneRandom: ")
        f.write(str(averageTime_updateOneRandom))
        f.write("\n")

        f.write("averageTime_findOneByOne: ")
        f.write(str(averageTime_findOneByOne))
        f.write("\n")

        f.write("averageTime_findRandom: ")
        f.write(str(averageTime_findRandom))
        f.write("\n")

        f.write("averageTime_delete: ")
        f.write(str(averageTime_delete))
        f.write("\n")





