#!/usr/bin/python3
"""unit tests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRect(unittest.TestCase):
    """da UWUnit tests"""

    def test_rekt_base(self):
        self.assertIsInstance(Rectangle(2, 2), Base)

    def test_min_args(self):
        rekt1 = Rectangle(2, 2)
        self.assertEqual(rekt1.area(), 4)

    def test_arg_limit(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 2, 2, 2)

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__width)

    def test_privacy_2(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__height)

    def test_privacy_3(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__x)

    def test_privacy_4(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__y)

    def test_privacy_5(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1, 1).__id)

    def test_richard(self):
        rekt1 = Rectangle(1, 1, 1, 1 ,1)
        richard = {"id": 1, "width": 1, "height": 1, "x": 1, "y": 1}
        dick = rekt1.to_dictionary()
        self.assertEqual(richard, dick)

    def test_update_1(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2)
        self.assertEqual(rekt1.id, 2)

    def test_update_2(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2)
        self.assertEqual(rekt1.width, 2)

    def test_update_3(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2, 2)
        self.assertEqual(rekt1.height, 2)

    def test_update_4(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2, 2, 2)
        self.assertEqual(rekt1.x, 2)

    def test_update_5(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(2, 2, 2, 2, 2)
        self.assertEqual(rekt1.y, 2)

    def test_upd_kwa_1(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(id=2)
        self.assertEqual(rekt1.id, 2)

    def test_upd_kwa_2(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(width=2)
        self.assertEqual(rekt1.width, 2)

    def test_upd_kwa_3(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(height=2)
        self.assertEqual(rekt1.height, 2)

    def test_upd_kwa_4(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(x=2)
        self.assertEqual(rekt1.x, 2)

    def test_upd_kwa_5(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(y=2)
        self.assertEqual(rekt1.y, 2)

    def test_upd_kwa_6(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.update(x=2, y=3)
        self.assertEqual(rekt1.y, 3)

    def test_str_rekt(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rektstr1 = rekt1.__str__()
        rektstr2 = '[Rectangle] (1) 1/1 - 1/1'
        self.assertEqual(rektstr1, rektstr2)

    def test_get_w(self):
        rekt1 = Rectangle(8, 6, 7, 5, 1)
        self.assertEqual(8, rekt1.width)

    def test_get_h(self):
        rekt1 = Rectangle(8, 6, 7, 5, 1)
        self.assertEqual(6, rekt1.height)

    def test_get_x(self):
        rekt1 = Rectangle(8, 6, 7)
        self.assertEqual(7, rekt1.x)

    def test_get_y(self):
        rekt1 = Rectangle(8, 6, 7, 5)
        self.assertEqual(5, rekt1.y)

    def test_get_id(self):
        rekt1 = Rectangle(8, 6, 7, 5, 1)
        self.assertEqual(1, rekt1.id)

    def test_set_w(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.width = 7
        self.assertEqual(7, rekt1.width)

    def test_set_h(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.height = 7
        self.assertEqual(7, rekt1.height)

    def test_set_x(self):
        rekt1 = Rectangle(1, 1, 1)
        rekt1.x = 7
        self.assertEqual(7, rekt1.x)

    def test_set_y(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        rekt1.y = 7
        self.assertEqual(7, rekt1.y)

    def test_set_id(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt1.id = 7
        self.assertEqual(7, rekt1.id)

    def test_flt_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.2, 2)

    def test_non_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_chr_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('a', 2)

    def test_str_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("UWU", 2)

    def test_boo_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_lst_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 2], 2)

    def test_dic_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"size": 1}, 2)

    def test_set_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 1}, 2)

    def test_tup_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 1), 2)

    def test_ngv_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)

    def test_zed_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_flt_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 2.2)

    def test_non_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_chr_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 'a')

    def test_str_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "UWU")

    def test_boo_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_lst_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [2, 2])

    def test_dic_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"size": 1})

    def test_set_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 1})

    def test_tup_reg_h(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 1))

    def test_ngv_reg_h(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3)

    def test_zed_reg_h(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_flt_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, 2.2)

    def test_non_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, None)

    def test_chr_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, 'a')

    def test_str_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, "UWU")

    def test_boo_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, True)

    def test_lst_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, [2, 2])

    def test_dic_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, {"size": 1})

    def test_set_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, {1, 1})

    def test_tup_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, (1, 1))

    def test_ngv_reg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 2, -3)

    def test_flt_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, 2.2)

    def test_non_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, None)

    def test_chr_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, 'a')

    def test_str_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2,"UWU")

    def test_boo_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, True)

    def test_lst_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, [2, 2])

    def test_dic_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, {"size": 1})

    def test_set_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, {1, 1})

    def test_tup_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 2, (1, 1))

    def test_ngv_reg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 2, 2, -3)

    def test_bad_upd_wid(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rekt1.update(width="YOLO")

    def test_bad_upd_hei(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rekt1.update(height="YOLO")

    def test_bad_upd_x(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rekt1.update(x="YOLO")

    def test_bad_upd_y(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rekt1.update(y="YOLO")

    def test_bad_upd_wid_val(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rekt1.update(width=-1)

    def test_bad_upd_hei_val(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rekt1.update(height=-1)

    def test_bad_upd_x_val(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rekt1.update(x=-1)

    def test_bad_upd_y_val(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rekt1.update(y=-1)

    @staticmethod
    def disp_yoink(shape):
        yoink = StringIO()
        sys.stdout = yoink
        shape.display()
        sys.stdout = sys.__stdout__
        return yoink

    def test_rkt_dis(self):
        rekt1 = Rectangle(2, 2, 1, 1, 1)
        yoink = TestRect.disp_yoink(rekt1)
        rektstr = "\n ##\n ##\n"
        self.assertEqual(yoink.getvalue(), rektstr)

    def test_rkt_dis_nof(self):
        rekt1 = Rectangle(2, 2, 0, 0, 0)
        yoink = TestRect.disp_yoink(rekt1)
        rektstr = "##\n##\n"
        self.assertEqual(yoink.getvalue(), rektstr)

    def test_str_rkt_nof(self):
        rekt1 = Rectangle(1, 1, 0, 0, 1)
        rektstr1 = rekt1.__str__()
        rektstr2 = '[Rectangle] (1) 0/0 - 1/1'
        self.assertEqual(rektstr1, rektstr2)

    def test_str_rkt_nid(self):
        rekt1 = Rectangle(1, 1)
        rekt1.update(id='')
        rektstr1 = rekt1.__str__()
        rektstr2 = '[Rectangle] () 0/0 - 1/1'
        self.assertEqual(rektstr1, rektstr2)

if __name__ == '__main__':
    unittest.main()
