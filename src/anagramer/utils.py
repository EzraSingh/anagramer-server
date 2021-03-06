#!/usr/bin/python3
import threading

''' Stream each line of a file '''
def parse(dictionary_file):
    with open(dictionary_file, 'r') as dictionary:
        for word in dictionary:
            yield word.rstrip()

# Sorted by frequency to improve performance 
# reference: http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
letters = "etaoinsrhdlucmfywgpbvkxqjz"
# First 26 Primes
primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
# map letter to respective prime based on index (i.e: 'e' -> 2, 't' -> 3, etc)
prime_letters = dict(zip(letters, primes))

''' Return permutation invariant prime hash '''
def normalize(word, sub_hash=1):
    # Check branch hotfix/prime-normalizer for preferred normalization strategy 
    return  "fk:" + "".join(sorted(word))


''' Alphabetize with respect to second letter '''
def alphabetize(collection):
    # NOTE: Since en-us.dict is already alphabetized and the sort algorithm is top down
    # and anagram insertions are head-first (e.g lpush'ed into linked list) items should
    # already be in a completely alphabetized arrangement, however an insert that is
    # an update to the cache may not guarantee this arrangement.
    try:
        return sorted(collection, key=(lambda x: x[1:]))
    except TypeError:
        return None

''' Simple decorator for running a function asynchronously '''
def run_in_background(func):
    def wrapper(*args, **kwargs):
        threading.Thread(target=func, args=args, kwargs=kwargs).start()
    return wrapper