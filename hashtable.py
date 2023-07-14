class HashTable:
    def __init__(self, size):
        self.table = []
        for i in range(size):
            self.table.append([])

    # insert key value pair into hash table
    # Space-Time Complexity O(N)
    def insert(self, key, item):
        # calculate bucket index
        bucket = hash(key) % len(self.table)
        # create key, value pair
        kv_item = [key, item]
        # bucket list for insertion
        bucket_list = self.table[bucket]

        # check if key already exists in bucket
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if key does not exist, append to end of bucket list
        bucket_list.append(kv_item)
        return True

    # delete item with key, return true if key is found and item is deleted, else return false
    # Space-Time Complexity O(N)
    def delete(self, key):
        # calculate bucket index
        bucket = hash(key) % len(self.table)
        # bucket list to delete from
        bucket_list = self.table[bucket]
        # if key exists within bucket list, remove key value pair and return true
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove(kv)
                return True

        # else if key does not exist, return false
        return False

    # return item found with stored key in hash table, else return None
    # Space-Time Complexity O(N)
    def search(self, key):
        # calculate bucket index
        bucket = hash(key) % len(self.table)
        # bucket list to search
        bucket_list = self.table[bucket]

        # iterate over bucket_list
        for kv in bucket_list:
            # check every key in bucket list
            if key == kv[0]:
                # if key is found, return its value
                return kv[1]

        # if no key is found, return None
        return None

    def print(self):
        print(self.table)