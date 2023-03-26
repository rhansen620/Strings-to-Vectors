"""
The main code for the Strings-to-Vectors assignment. See README.md for details.
"""
from typing import Sequence, Any

import numpy as np


class Index:
    """
    Represents a mapping from a vocabulary (e.g., strings) to integers.
    """

    def __init__(self, vocab: Sequence[Any], start=0):
        """
        Assigns an index to each unique item in the `vocab` iterable,
        with indexes starting from `start`.

        Indexes should be assigned in order, so that the first unique item in
        `vocab` has the index `start`, the second unique item has the index
        `start + 1`, etc.
        """
        self.dict1 ={}
        self.start = start
        self.vocabulab = vocab
        for item in vocab:
            if item in self.dict1:
                continue
            self.dict1[item] = start
            start += 1


    def objects_to_indexes(self, object_seq: Sequence[Any]) -> np.ndarray:
        """
        Returns a vector of the indexes associated with the input objects.

        For objects not in the vocabulary, `start-1` is used as the index.

        :param object_seq: A sequence of objects.
        :return: A 1-dimensional array of the object indexes.
        """
        new_list =[]
        for item in object_seq:
            value = self.dict1.get(item, (self.start-1))
            new_list.append(value)
        new_list = np.array(new_list)
        return new_list


    def objects_to_index_matrix(
            self, object_seq_seq: Sequence[Sequence[Any]]) -> np.ndarray:
        """
        Returns a matrix of the indexes associated with the input objects.

        For objects not in the vocabulary, `start-1` is used as the index.

        If the sequences are not all of the same length, shorter sequences will
        have padding added at the end, with `start-1` used as the pad value.

        :param object_seq_seq: A sequence of sequences of objects.
        :return: A 2-dimensional array of the object indexes.
        """
        max_len = max([len(x) for x in object_seq_seq])
        output = [np.pad(x, (0, max_len - len(x)), 'constant') for x in object_seq_seq]
        new_list =[]
        for rows in output:
            m_list = []
            for columns in rows:
                value = self.dict1.get(columns, (self.start-1))
                m_list.append(value)
            new_list.append(m_list)
        new_list = np.array(new_list)
        return new_list


    def objects_to_binary_vector(self, object_seq: Sequence[Any]) -> np.ndarray:
        """
        Returns a binary vector, with a 1 at each index corresponding to one of
        the input objects.

        :param object_seq: A sequence of objects.
        :return: A 1-dimensional array, with 1s at the indexes of each object,
                 and 0s at all other indexes.
        """
        #vocab = "she sells seashells by the seashore".split()
        #objects = "the seashells she sells".split()
        #sorted_objects = "she sells seashells the".split()
        #vector = np.array([1, 1, 1, 0, 1, 0])
        new_list=[]
        if self.start != 0:
            r_count=0
            while r_count != self.start:
                new_list.append(0)
                r_count += 1
        for key in self.dict1:
            if key in  object_seq:
                new_list.append(1)
            else:
                new_list.append(0)
        new_list = np.array(new_list)
        print (new_list)
        return new_list


    def objects_to_binary_matrix(self, object_seq_seq: Sequence[Sequence[Any]]) -> np.ndarray:
        """
        Returns a binary matrix, with a 1 at each index corresponding to one of
        the input objects.

        :param object_seq_seq: A sequence of sequences of objects.
        :return: A 2-dimensional array, where each row in the array corresponds
                 to a row in the input, with 1s at the indexes of each object,
                 and 0s at all other indexes.
        """
        new_list=[]
        for rows in object_seq_seq:
            m_list= []
            if self.start != 0:
                r_count=0
                while r_count != self.start:
                    m_list.append(0)
                    r_count += 1
                    print (r_count)
            for key in self.dict1:
                if key in rows:
                    m_list.append(1)
                else:
                    m_list.append(0)
            new_list.append(m_list)
        new_list =np.array(new_list)
        return new_list


    def indexes_to_objects(self, index_vector: np.ndarray) -> Sequence[Any]:
        """
        Returns a sequence of objects associated with the indexes in the input
        vector.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param index_vector: A 1-dimensional array of indexes
        :return: A sequence of objects, one for each index.
        """
        vocab =[]
        for item in index_vector:
            for key, value in self.dict1.items():
                if item == value:
                    vocab.append(key)
    #    print (vocab)
        return vocab

    def index_matrix_to_objects(
            self, index_matrix: np.ndarray) -> Sequence[Sequence[Any]]:
        """
        Returns a sequence of sequences of objects associated with the indexes
        in the input matrix.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param index_matrix: A 2-dimensional array of indexes
        :return: A sequence of sequences of objects, one for each index.
        """
        vocab = []
        for rows in index_matrix:
            d_list =[]
            for i in rows:
                for key, value in self.dict1.items():
                    if i == value:
                        d_list.append(key)
            vocab.append(d_list)
        return vocab

    def binary_vector_to_objects(self, vector: np.ndarray) -> Sequence[Any]:
        """
        Returns a sequence of the objects identified by the nonzero indexes in
        the input vector.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param vector: A 1-dimensional binary array
        :return: A sequence of objects, one for each nonzero index.
        """
        new_list=[]
        vex = vector.tolist()
      #  print (self.vocabulab)
        if self.start != 0:
            r_count =0
            while r_count != self.start:
                vex.pop(0)
                r_count += 1
        for item in range(len(vex)):
            if vex[item] == 1:
                v_list = self.vocabulab[int(item)]
                print (v_list)
                new_list.append(v_list)
            else:
                continue
        return new_list

    def binary_matrix_to_objects(self, binary_matrix: np.ndarray) -> Sequence[Sequence[Any]]:
        """
        Returns a sequence of sequences of objects identified by the nonzero
        indices in the input matrix.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param binary_matrix: A 2-dimensional binary array
        :return: A sequence of sequences of objects, one for each nonzero index.
        """
        new_list =[]
        vex = binary_matrix.tolist()
        print (vex)
        for rows in vex:
            d_list=[]
            if self.start != 0:
                r_count =0
                while r_count != self.start:
                    rows.pop(0)
                    r_count += 1
            for item in range(len(rows)):
                if rows[item] == 1:
                    v_list = (self.vocabulab[item])
                    print (v_list)
                    d_list.append(v_list)
                else:
                    continue
            new_list.append(d_list)
        return new_list
        