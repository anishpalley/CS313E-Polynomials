"""
Student information for this assignment:

Replace Anish Palley with your name.
On my/our honor, Anish Palley and <FULL NAME>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: ap65675
UT EID 2:
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    """
    linkedList
    """
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        """
        insert term
        """
        if coeff == 0:
            return
        node = Node(coeff, exp)
        current = self.head

        if self.head is None or exp > current.exp:
            node.next = current
            self.head = node
            return
        if current.exp == exp:
            current.coeff += coeff
            if current.coeff == 0:
                self.head = current.next
            return

        while current.next is not None and current.next.exp > exp:
            current = current.next
        if current.next is not None and current.next.exp == exp:
            current.next.coeff += coeff
            if current.next.coeff == 0:
                current.next = current.next.next
            return
        node.next= current.next
        current.next = node

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        """
        add
        """
        poly = LinkedList()
        self_current = self.head
        p_current = p.head
        while self_current is not None:
            poly.insert_term(self_current.coeff, self_current.exp)
            self_current = self_current.next
        while p_current is not None:
            poly.insert_term(p_current.coeff, p_current.exp)
            p_current = p_current.next
        return poly
    def mult(self, p):
        """
        mult
        """
        poly = LinkedList()
        self_current = self.head
        while self_current is not None:
            poly_current = p.head
            while poly_current is not None:
                coeff = self_current.coeff * poly_current.coeff
                exp = self_current.exp + poly_current.exp
                poly.insert_term(coeff,exp)
                poly_current = poly_current.next
            self_current = self_current.next
        return poly
    # Return a string representation of the polynomial.
    def __str__(self):
        current = self.head
        lst = []
        while current is not None:
            coeff = current.coeff
            exp = current.exp
            returned = "("+str(coeff)+", "+str(exp)+")"
            lst.append(returned)
            current = current.next
        string = ""
        for i,element in enumerate((lst)):
            string+=element
            if i!=(len(lst)-1):
                string+=" + "
        return string
def main():
    """
    main
    """
    # read data from stdin (terminal/file) using input() and create polynomial p
    p_n = int(input())
    p = LinkedList()
    for _ in range(p_n):
        nums = input().split()
        p_coeff = int(nums[0])
        p_exp = int(nums[1])
        p.insert_term(p_coeff,p_exp)
    input()

    # read data from stdin (terminal/file) using input() and create polynomial q
    q_n = int(input())
    q = LinkedList()
    for _ in range(q_n):
        nums = input().split()
        q_coeff = int(nums[0])
        q_exp = int(nums[1])
        q.insert_term(q_coeff,q_exp)

    # get sum of p and q as a new linked list and print sum
    sum_pq = p.add(q)
    print(sum_pq)

    # get product of p and q as a new linked list and print product
    prod_pq = p.mult(q)
    print(prod_pq)


if __name__ == "__main__":
    main()
