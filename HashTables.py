class HashTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size

    def __hash(self, key) -> int:
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key) -> int:
        index = self.__hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f"{i}: {val}")

if __name__ == "__main__":
    my_hash_table = HashTable()
    my_hash_table.set_item('bolts', 1400)
    my_hash_table.set_item('washers', 50)
    my_hash_table.set_item('lumber', 70)

    print(my_hash_table.keys())
    my_hash_table.print_table()
    