# Do not change the name of this file or the class name.
class Anagram(object):

    def __init__(self, filename):
        self.load_dictionary(filename)

    """
    Helper method to load the dictionary file.
    You may read it in some other way if you want to but do not change the function signature.
    """
    def load_dictionary(self, filename):
        with open(filename) as handle:
            self.dictionary = set(w.strip() for w in handle)

    """
    Here is where I implement QuickSort, Partition, and a wrapper function for QuickSort
    QuickSort is needed to put each word into alphabetical order so it can be efficiently
    inserted into the correct index in the result list.
    """

    def partition(self, arr, p, r):
        pivot = arr[r]  # pivot
        i = (p - 1)     # index of smaller element


        for j in range(p, r): # create the leftmost region of the list

            if (arr[j] <= pivot):

                # increment index of smaller element
                i = i+1
                # exchange the elements at i and j
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return (i + 1)

    def quickSort(self, arr, p, r):
        if (len(arr) == 1): # base case
            return arr
        if (p < r):

            # get partion index q
            q = self.partition(arr, p, r)

            # Recursive calls to the region of list left of q
            # and right of q
            self.quickSort(arr, p, q - 1)
            self.quickSort(arr, q + 1, r)

    def alpha(self, str):
        str = list(str) # convert given string to list for sorting
        self.quickSort(str, 0, len(str) - 1) # sort list, takes O(klogn) time
        result = ''.join(str) #convert list back to string
        return result

    def hash(self, value):
        #Hash function simply returns the word in alphabetical order
        #this function uses quicksort to sort the word
        return self.alpha(value)

    def hashInsert(self, table, value):
        key = self.hash(value) #get the key using hash() function
        #different methods of insertion depending on if the given
        #key has already been inserted
        if key in table:
            table[key].append(value) #append to list stored at key
        else:
            table[key] = [value] #set new key equal to list with value in it

    """
   * Implement the algorithm here. Do not change the function signature.
   *
   * @returns - List of lists, where each element of the outer list is a list containing all the words in that anagram class.
   * example: [['pots', 'stop', 'tops'], ['brake', 'break']]
    """
    def getAnagrams(self):
        hashTable = {}
        result = []
        for word in self.dictionary:
            #iterate through list of words and
            #insert each word into its place
            #in the hashTable
            self.hashInsert(hashTable, word)

        for key in hashTable:
            #iterate through the hashTable
            #and append each list into
            #the result list
            result.append(hashTable[key])

        return result

"""
You can use this for debugging if you wish.
"""
if __name__ == "__main__":
    pf = Anagram("Dictionaries/dict1.txt")
    print(pf.getAnagrams())
