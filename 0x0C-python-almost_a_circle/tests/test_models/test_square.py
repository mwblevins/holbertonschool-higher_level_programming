#!/usr/bin/python3
"""unit tests for square.py"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import os
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """da UWUnit tests"""
    def test_if_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_if_rekt(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_update_1(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2)
        self.assertEqual(sqr1.id, 2)

    def test_update_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2)
        self.assertEqual(sqr1.size, 2)

    def test_update_3(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2, 2)
        self.assertEqual(sqr1.x, 2)

    def test_update_4(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(2, 2, 2, 2)
        self.assertEqual(sqr1.y, 2)

    def test_upd_kwa_1(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(id=2)
        self.assertEqual(sqr1.id, 2)

    def test_upd_kwa_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(size=2)
        self.assertEqual(sqr1.size, 2)

    def test_upd_kwa_3(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(x=2)
        self.assertEqual(sqr1.x, 2)

    def test_upd_kwa_4(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr1.update(y=2)
        self.assertEqual(sqr1.y, 2)

    def test_upd_kwa_5(self):
        sqr1 = Square(2, 2, 2, 2)
        sqr1.update(id=5, y=3)
        self.assertEqual(sqr1.id, 5)
        self.assertEqual(sqr1.y, 3)

    def test_upd_kwa_6(self):
        sqr1 = Square(2, 2, 2, 2)
        sqr1.update(size=1, x=1, y=1, id=1)
        self.assertEqual(sqr1.id, 1)

    def test_str_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        sqrstr1 = sqr1.__str__()
        sqrstr2 = '[Square] (1) 1/1 - 1'
        self.assertEqual(sqrstr1, sqrstr2)

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__id)

    def test_privacy_2(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__size)

    def test_privacy_3(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__x)

    def test_privacy_4(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 1, 1, 1).__y)

    def test_arg_limit(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_okay_sqr(self):
        sqr1 = Square(3, 0, 0, 1)
        self.assertEqual(sqr1.area(), 9)

    def test_size_init(self):
        sqr1 = Square(3)
        self.assertEqual(sqr1.width, sqr1.size)
        self.assertEqual(sqr1.height, sqr1.size)

    def test_richard(self):
        sqr1 = Square(1, 1, 1 ,1)
        richard = {"id": 1, "size": 1, "x": 1, "y": 1}
        dick = sqr1.to_dictionary()
        self.assertEqual(richard, dick)

    def test_get_size(self):
        sqr1 = Square(8)
        self.assertEqual(8, sqr1.size)

    def test_get_x(self):
        sqr1 = Square(8, 6)
        self.assertEqual(6, sqr1.x)

    def test_get_y(self):
        sqr1 = Square(8, 6, 7)
        self.assertEqual(7, sqr1.y)

    def test_get_id(self):
        sqr1 = Square(8, 6, 7, 5)
        self.assertEqual(5, sqr1.id)

    def test_set_size(self):
        sqr1 = Square(8)
        sqr1.size = 1
        self.assertEqual(1, sqr1.size)

    def test_set_x(self):
        sqr1 = Square(8, 6)
        sqr1.x = 1
        self.assertEqual(1, sqr1.x)

    def test_set_y(self):
        sqr1 = Square(8, 6, 7)
        sqr1.y = 1
        self.assertEqual(1, sqr1.y)

    def test_set_id(self):
        sqr1 = Square(8, 6, 7, 5)
        sqr1.id = 1
        self.assertEqual(1, sqr1.id)

    def test_flt_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.2)

    def test_non_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_chr_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('a')

    def test_str_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("UWU")

    def test_boo_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_lst_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([2, 2])

    def test_dic_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"size": 1})

    def test_set_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 1})

    def test_tup_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 1))

    def test_ngv_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3)

    def test_zed_reg(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_cmp_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(3))

    def test_nan_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_inf_reg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_flt_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 2.2)

    def test_non_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_chr_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 'a')

    def test_str_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "UWU")

    def test_boo_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True)

    def test_lst_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [2, 2])

    def test_dic_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"size": 1})

    def test_set_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 1})

    def test_tup_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 1))

    def test_ngv_reg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -3)

    def test_cmp_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(3))

    def test_nan_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'))

    def test_inf_reg_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'))

    def test_flt_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, 2.2)

    def test_non_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, None)

    def test_chr_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, 'a')

    def test_str_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2,"UWU")

    def test_boo_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, True)

    def test_lst_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, [2, 2])

    def test_dic_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, {"size": 1})

    def test_set_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, {1, 1})

    def test_tup_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, (1, 1))

    def test_ngv_reg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 2, -3)

    def test_cmp_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, complex(3))

    def test_nan_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_inf_reg_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    @staticmethod
    def disp_yoink(shape):
        yoink = StringIO()
        sys.stdout = yoink
        shape.display()
        sys.stdout = sys.__stdout__
        return yoink

    def test_sqr_dis(self):
        sqr1 = Square(2, 1, 1, 1)
        yoink = TestSquare.disp_yoink(sqr1)
        sqrstr = "\n ##\n ##\n"
        self.assertEqual(yoink.getvalue(), sqrstr)

    def test_sqr_dis_nof(self):
        sqr1 = Square(2, 0, 0, 0)
        yoink = TestSquare.disp_yoink(sqr1)
        sqrstr = "##\n##\n"
        self.assertEqual(yoink.getvalue(), sqrstr)

    def test_str_sqr_nof(self):
        sqr1 = Square(1, 0, 0, 1)
        sqrstr1 = sqr1.__str__()
        sqrstr2 = '[Square] (1) 0/0 - 1'
        self.assertEqual(sqrstr1, sqrstr2)

if __name__ == '__main__':
    unittest.main()
