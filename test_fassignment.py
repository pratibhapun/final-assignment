import unittest
from tkinter import Tk
import fassignment

class Test_final_assignment(unittest.TestCase):
    def test_mergesort(self):
        list = [('Pratibha', 'Pun', '1002', ' Ethical Hacking', ' Female', 'Dang', '9999999999'),
                ('Amantika', 'Karki', '1001', ' Ethical Hacking', ' Female', 'Sarlahi', '9999999999'),
                ('Rudra', 'Pun', '1000', 'Computing', ' Female', 'Rolpa', '9999999999')]
        ex_result = [('Rudra', 'Pun', '1000', 'Computing', ' Female', 'Rolpa', '9999999999'),
                     ('Amantika', 'Karki', '1001', ' Ethical Hacking', ' Female', 'Sarlahi', '9999999999'),
                     ('Pratibha', 'Pun', '1002', ' Ethical Hacking', ' Female', 'Dang', '9999999999')]
        root1 = Tk()
        a = fassignment.Sort(root1)

        a.sortCombo.set('Student_id')
        ac_result = a.mergesort(list)
        print('Sort Test')
        print(ac_result)
        self.assertEqual(ex_result, ac_result)

    def test_search_item(self):
        list = [('Pratibha', 'Pun', '1002', ' Ethical Hacking', ' Female', 'Dang', '9999999999'),
                ('Amantika', 'Karki', '1001', ' Ethical Hacking', ' Female', 'Sarlahi', '9999999999'),
                ('Rudra', 'Pun', '1000', 'Computing', ' Female', 'Rolpa', '9999999999')]
        ex_result = [('Rudra', 'Pun', '1000', 'Computing', ' Female', 'Rolpa', '9999999999')]
        root1=Tk()
        c = fassignment.Search(root1)
        c.searchentry.delete(0, 'end')
        c.searchentry.insert(0, 'Rudra')
        print('Search test')


        ac_result=c.search_item(list)
        print(ac_result)
        self.assertEqual(ex_result, ac_result)

if __name__ == 'main':
    unittest.main()

