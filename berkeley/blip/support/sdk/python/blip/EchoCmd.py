#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'EchoCmd'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 0

# The Active Message type associated with this message.
AM_TYPE = -1

class EchoCmd(tinyos.message.Message.Message):
    # Create a new EchoCmd of size 0.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=0):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <EchoCmd> \n"
        try:
            pass
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: data
    #   Field type: short[]
    #   Offset (bits): 0
    #   Size of each element (bits): 8
    #

    #
    # Return whether the field 'data' is signed (False).
    #
    def isSigned_data(self):
        return False
    
    #
    # Return whether the field 'data' is an array (True).
    #
    def isArray_data(self):
        return True
    
    #
    # Return the offset (in bytes) of the field 'data'
    #
    def offset_data(self, index1):
        offset = 0
        if index1 < 0:
            raise IndexError
        offset += 0 + index1 * 8
        return (offset / 8)
    
    #
    # Return the offset (in bits) of the field 'data'
    #
    def offsetBits_data(self, index1):
        offset = 0
        if index1 < 0:
            raise IndexError
        offset += 0 + index1 * 8
        return offset
    
    #
    # Return the entire array 'data' as a short[]
    #
    def get_data(self):
        raise IndexError
    
    #
    # Set the contents of the array 'data' from the given short[]
    #
    def set_data(self, value):
        for index0 in range(0, len(value)):
            self.setElement_data(index0, value[index0])

    #
    # Return an element (as a short) of the array 'data'
    #
    def getElement_data(self, index1):
        return self.getUIntElement(self.offsetBits_data(index1), 8, 1)
    
    #
    # Set an element of the array 'data'
    #
    def setElement_data(self, index1, value):
        self.setUIntElement(self.offsetBits_data(index1), 8, value, 1)
    
    #
    # Return the size, in bytes, of each element of the array 'data'
    #
    def elementSize_data(self):
        return (8 / 8)
    
    #
    # Return the size, in bits, of each element of the array 'data'
    #
    def elementSizeBits_data(self):
        return 8
    
    #
    # Return the number of dimensions in the array 'data'
    #
    def numDimensions_data(self):
        return 1
    
    #
    # Return the number of elements in the array 'data'
    # for the given dimension.
    #
    def numElements_data(self, dimension):
        array_dims = [ 0,  ]
        if dimension < 0 or dimension >= 1:
            raise IndexException
        if array_dims[dimension] == 0:
            raise IndexError
        return array_dims[dimension]
    
    #
    # Fill in the array 'data' with a String
    #
    def setString_data(self, s):
         l = len(s)
         for i in range(0, l):
             self.setElement_data(i, ord(s[i]));
         self.setElement_data(l, 0) #null terminate
    
    #
    # Read the array 'data' as a String
    #
    def getString_data(self):
        carr = "";
        for i in range(0, 4000):
            if self.getElement_data(i) == chr(0):
                break
            carr += self.getElement_data(i)
        return carr
    