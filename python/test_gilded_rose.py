# -*- coding: utf-8 -*-
import unittest

from gilded_rose import *


class GildedRoseTest(unittest.TestCase):
    def test_basic_item(self):
        items = [Item("food", 2, 4), Item("magical carpet", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("food", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(3, items[0].quality)
        
        self.assertEqual("magical carpet", items[1].name)
        self.assertEqual(-2, items[1].sell_in)
        self.assertEqual(0, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

        self.assertEqual(-3, items[1].sell_in)
        self.assertEqual(0, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)



    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0), Item("The Best Aged Brie Ever!", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)
        
        self.assertEqual("The Best Aged Brie Ever!", items[1].name)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(50, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(4, items[0].quality)




    def test_conjured_items(self):
        items = [Item("Conjured Strawberry Jelly", 2, 9), Item("A Conjured Potato", -1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured Strawberry Jelly", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(7, items[0].quality)
        
        self.assertEqual("A Conjured Potato", items[1].name)
        self.assertEqual(-2, items[1].sell_in)
        self.assertEqual(0, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(5, items[0].quality)

        self.assertEqual(-3, items[1].sell_in)
        self.assertEqual(0, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)


        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)




    def test_backstage_pass(self):
        items = [Item("Fancy Backstage passes", 6, 44), Item("Super Fancy Backstage passes", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Fancy Backstage passes", items[0].name)
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(46, items[0].quality)
        
        self.assertEqual("Super Fancy Backstage passes", items[1].name)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(50, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(49, items[0].quality)

        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(0, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(50, items[0].quality)



    def test_sulfuras(self):
        items = [Item("Mega Sulfuras", 695, 80), Item("Super Sulfuras", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Mega Sulfuras", items[0].name)
        self.assertEqual(695, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
        
        self.assertEqual("Super Sulfuras", items[1].name)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(80, items[1].quality)


        gilded_rose.update_quality()
        self.assertEqual(695, items[0].sell_in)
        self.assertEqual(80, items[0].quality)



        
if __name__ == '__main__':
    unittest.main()
