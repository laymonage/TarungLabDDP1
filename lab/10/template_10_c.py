# Template Binary Search Tree

class Node:
    
    '''
    Class untuk node dari Binary Search Tree
    Terdiri dari value dari node
    dan reference ke left child dan right child
    '''
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Benny-ry Search Tree
# *binary
class BST:
    
    '''
    Class untuk Binary Search Tree
    Terdiri dari kumpulan-kumpulan node
    yang sudah tersusun dalam bentuk tree
    '''
    
    def __init__(self):
        self.root = None

    '''
    Method untuk set root dari tree
    '''
    def set_root(self, value):
        self.root = Node(value)

    '''
    Method insert
    Digunakan untuk memasukkan nilai ke dalam tree
    Jika tree masih kosong, nilai yang dimasukkan menjadi root
    Jika tree sudah terisi, nilai yang dimasukkan akan dicek,
    kalau lebih kecil daripada elemen yang akan dibandingkan akan dimasukkan
    sebagai left child, sebaliknya akan ke right child
    -------------------------------------------------------------------------
    @param value
    '''
    def insert(self, value):
        if(self.root is None):
            self.set_root(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, current_node, value):
        if(value < current_node.value):
            if(current_node.left):
                self.insert_node(current_node.left, value)
            else:
                current_node.left = Node(value)
        elif(value > current_node.value):
            if(current_node.right):
                self.insert_node(current_node.right, value)
            else:
                current_node.right = Node(value)

    '''
    Method find
    Digunakan untuk mencari sebuah nilai di dalam tree
    --------------------------------------------------
    @param value
    @return boolean
    '''
    def find(self, value):
        return self.find_node(self.root, value)

    def find_node(self, current_node, value):        
        # TODO implementasikan code ini menggunakan recursion
        # current_node adalah node yang sedang ditunjuk
        # value adalah nilai yang dicari
        # method ini mengembalikan True jika value terdapat di dalam BST,
        # atau False jika value tidak terdapat di dalam BST
        pass


def main():
    # Inisiasi binary search tree
    bst = BST()

    # Memasukkan elemen ke dalam tree
    angka = [50,40,60,30,45,57,75,21,44,47,65,90]
    for i in angka:
        bst.insert(i)

    while(True):
    # Meminta input dari user, angka yang yang akan dicek apakah ada dalam tree
        x = int(input('Masukkan sebuah integer yang ingin dicari di dalam tree: '))
        if(bst.find(x)):
            print("{} terdapat dalam tree".format(x))
        else:
            print("{} tidak ada dalam tree".format(x))

main()
