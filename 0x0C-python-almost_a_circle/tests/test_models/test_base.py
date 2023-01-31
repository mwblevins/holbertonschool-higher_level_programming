#!/usr/bin/python3
"""unit tests for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """da UWUnit tests"""

    def test_non(self):
        base1 = Base(None)
        base2 = Base()
        self.assertEqual(base1.id + 1, base2.id)

    def test_tmi(self):
        with self.assertRaises(TypeError):
            Base(5, 5)

    def test_privacy_1(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_jason_rekt(self):
        rekt1 = {"width": 1, "height": 1, "x": 1, "y": 1, "id": 1}
        self.assertEqual(type(Base.to_json_string([rekt1])), str)

    def test_jason_sqr(self):
        sqr1 = {"size": 1, "x": 1, "y": 1, "id": 1}
        self.assertEqual(type(Base.to_json_string([sqr1])), str)

    def test_jason_rekt_2(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt2 = Rectangle(2, 2, 2, 2, 2)
        rekt_richard = [rekt1.to_dictionary(), rekt2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(rekt_richard)), 104)

    def test_jason_sqr_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr2 = Square(2, 2, 2, 2)
        sqr_richard = [sqr1.to_dictionary(), sqr2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(sqr_richard)), 76)

    def test_jason_empty(self):
        dict1 = []
        js = Base.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    def test_jason_none(self):
        dict1 = None
        js = Base.to_json_string(dict1)
        self.assertEqual(len(js), 2)

    def test_stf_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        Square.save_to_file([sqr1])
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 38)

    def test_stf_rkt(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([rekt1])
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 52)

    def test_stf_sqr_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr2 = Square(2, 2, 2, 2)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 76)

    def test_stf_rkt_2(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        rekt2 = Rectangle(2, 2, 2, 2, 2)
        Rectangle.save_to_file([rekt1, rekt2])
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 104)

    def test_stf_sqr_mpt(self):
        Square.save_to_file([])
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 2)

    def test_stf_sqr_non(self):
        Square.save_to_file(None)
        with open("Square.json") as fred:
            self.assertEqual(len(fred.read()), 2)

    def test_stf_rkt_mpt(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 2)

    def test_stf_rkt_non(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as fred:
            self.assertEqual(len(fred.read()), 2)

    def test_fjs_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        dick1 = sqr1.to_dictionary()
        jason_in = Square.to_json_string([dick1])
        jason_out = Square.from_json_string(jason_in)
        self.assertEqual(len(str(dick1)) + 2, len(str(jason_out)))

    def test_fjs_sqr_2(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr2 = Square(2, 2, 2, 2)
        dic1 = sqr1.to_dictionary()
        dic2 = sqr2.to_dictionary()
        jason_in = Base.to_json_string([dic1, dic2])
        jason_out = Base.from_json_string(jason_in)
        self.assertEqual(jason_out, [dic1, dic2])

    def test_fjs_rkt(self):
        rekt1 = Rectangle(1, 1, 1, 1, 1)
        dick1 = rekt1.to_dictionary()
        jason_in = Rectangle.to_json_string([dick1])
        jason_out = Rectangle.from_json_string(jason_in)
        self.assertEqual(len(str(dick1)) + 2, len(str(jason_out)))

    def test_fjs_non(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_fjs_mpt(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_crt_sqr(self):
        sqr1 = Square(2, 2, 2, 2)
        dick1 = sqr1.to_dictionary()
        sqr11 = Square.create(**dick1)
        self.assertEqual(str(sqr11), str(sqr1))

    def test_crt_sqr_neq(self):
        sqr1 = Square(2, 2, 2, 2)
        dick1 = sqr1.to_dictionary()
        sqr11 = Square.create(**dick1)
        self.assertNotEqual(sqr11, sqr1)

    def test_crt_sqr_not(self):
        sqr1 = Square(2, 2, 2, 2)
        dick1 = sqr1.to_dictionary()
        sqr11 = Square.create(**dick1)
        self.assertIsNot(sqr11, sqr1)

    def test_crt_rkt(self):
        rekt1 = Rectangle(2, 2, 2, 2, 2)
        dick1 = rekt1.to_dictionary()
        rekt11 = Rectangle.create(**dick1)
        self.assertEqual(str(rekt11), str(rekt1))

    def test_crt_rkt_neq(self):
        rekt1 = Rectangle(2, 2, 2, 2, 2)
        dick1 = rekt1.to_dictionary()
        rekt11 = Rectangle.create(**dick1)
        self.assertNotEqual(rekt1, rekt11)

    def test_crt_rkt_not(self):
        rekt1 = Rectangle(2, 2, 2, 2, 2)
        dick1 = rekt1.to_dictionary()
        rekt11 = Rectangle.create(**dick1)
        self.assertIsNot(rekt1, rekt11)

    def test_lff_sqr(self):
        sqr1 = Square(1, 1, 1, 1)
        sqr2 = Square(2, 2, 2, 2)
        Square.save_to_file([sqr1, sqr2])
        sqrlst = Square.load_from_file()
        self.assertEqual(str(sqr2), str(sqrlst[1]))

    def test_lff_rkt(self):
        rekt1 = Rectangle(1, 1, 1, 1)
        rekt2 = Rectangle(2, 2, 2, 2)
        Rectangle.save_to_file([rekt1, rekt2])
        rktlst = Rectangle.load_from_file()
        self.assertEqual(str(rekt2), str(rktlst[1]))

    def test_lff_dne(self):
        loadup = Base.load_from_file()
        self.assertEqual([], loadup)

if __name__ == '__main__':
    unittest.main()
