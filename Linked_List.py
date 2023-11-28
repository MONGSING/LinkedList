class Node:
    def __init__(self, Data=None, Next=None):
        self.Data = Data
        self.Next = Next


class LinkedList:
    def __init__(self):
        self.Head = None

    def Insert_At_Beginning(self, Value):
        New_Node = Node(Value, self.Head)
        self.Head = New_Node

    def Insert_At_End(self, Value):
        New_Node = Node(Value)
        if self.Head is None:
            self.Head = New_Node
        else:
            itr = self.Head
            while itr.Next is not None:
                itr = itr.Next
            itr.Next = New_Node

    def Pop_From_Beginning(self):
        if self.Head is None:
            print("Linked List is Empty. Cannot pop from an empty list.")
        Pop_Value = self.Head.Data
        self.Head = self.Head.Next
        return Pop_Value

    def Pop_From_End(self):
        if self.Head is None:
            print("Linked List is Empty. Cannot pop from an empty list.")
        elif self.Head.Next is None:
            Pop_Value = self.Head.Data
            self.Head = None
            return Pop_Value
        else:
            itr = self.Head
            while itr.Next.Next is not None:
                itr = itr.Next
            Pop_Value = itr.Next.Next
            itr.Next = None
            return Pop_Value

    def Insert_At_index(self, index, Value):
        if index < 0:
            print("Invalid index. Index should be non-negative.")
            return

        New_Node = Node(Value)
        if index == 0:
            self.Insert_At_Beginning(Value)
        else:
            Count = 0
            itr = self.Head
            while itr:
                if Count == index - 1:
                    itr.Next = New_Node
                itr = itr.Next
                Count = Count + 1

    def Count_LinkedList(self):
        Counter = 0
        itr = self.Head
        while itr:
            Counter = Counter + 1
            itr = itr.Next
        return Counter

    def Print_Linked_List(self):
        if self.Head is None:
            print("Linked List Is None")
        else:
            Linked_List = ""
            itr = self.Head

            while itr:
                # Ethane 0 + Str(10) + ===>
                Linked_List = Linked_List + str(itr.Data) + " ===> "
                # And Last e Str(10) = Str(10).Next (mean 10 er por jodi 12 dei tah-ole 10 ==> 12)
                itr = itr.Next
            print(Linked_List[:-5])


LL1 = LinkedList()

print("Insert At Beginning")
LL1.Insert_At_Beginning(10)
LL1.Insert_At_Beginning(12)
LL1.Insert_At_Beginning(13)
LL1.Insert_At_Beginning(15)
LL1.Print_Linked_List()

print("Insert At End")
LL1.Insert_At_End(30)
LL1.Insert_At_End(40)
LL1.Insert_At_End(50)
LL1.Print_Linked_List()

# print("Insert At Index")
# LL1.Insert_At_index(2, 90)
# LL1.Print_Linked_List()

print(f"Current All Nodes Are : {LL1.Count_LinkedList()}")
#
# print("Pop From Beginning")
# LL1.Pop_From_Beginning()
# LL1.Print_Linked_List()
# print(f"Current All Nodes Are : {LL1.Count_LinkedList()}")

print("--------Pop From End--------")
LL1.Pop_From_End()
LL1.Pop_From_End()
LL1.Print_Linked_List()
print(f"Current All Nodes Are : {LL1.Count_LinkedList()}")
