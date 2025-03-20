class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    


class BasicItem(Item):
    def update_quality(self):
        # When the quality is already 0, do nothing
        if self.quality == 0:
            pass 
        # When the sell date has pasted and the quality is 2 or more, reduce quality by 2
        elif self.sell_in <= 0 and self.quality >= 2:
            self.quality -= 2
        # When the sell date has not pasted or the quality is equal to 1, reduce quality by 1
        else:
            self.quality -= 1

        self.sell_in -= 1
        
        return self.sell_in, self.quality


class ConjuredIteam(Item):
    def update_quality(self):
        # When the quality is already 0, do nothing
        if self.quality == 0:
            pass 
        # When the sell date has pasted and the quality is 4 or more, reduce quality by 4
        elif self.sell_in <= 0 and self.quality >= 4:
            self.quality -= 4
        # When the sell date has pasted and the quality is 4 or more, reduce quality by 4
        elif self.sell_in <= 0 and self.quality == 3:
            self.quality -= 3
        # When the sell date has not pasted or the quality is equal to 2 or 3, reduce quality by 2
        elif self.quality >= 2:
            self.quality -= 2
        else:
            self.quality -= 1

        self.sell_in -= 1

        return self.sell_in, self.quality


class AgedBrie(Item):
    def update_quality(self):
        # When the quality is already 50, do nothing
        if self.quality == 50:
            pass 
        # When the sell date has pasted and the quality is 48 or less, increase quality by 2
        elif self.sell_in <= 0 and self.quality <= 48:
            self.quality += 2
        # When the sell date has not pasted or the quality is equal to 49, increase quality by 1
        else:
            self.quality += 1

        self.sell_in -= 1

        return self.sell_in, self.quality


class BackstagePasses(Item):
    def update_quality(self):
        # When the sell date has pasted, quality is 0
        if self.sell_in <= 0:
            self.quality = 0
        # When the quality is already 50, do nothing
        elif self.quality == 50:
            pass  
        # When the sell date is within 5 days and the quality is 47 or less, increase quality by 3
        elif self.sell_in <= 5 and self.quality <= 47:
            self.quality += 3
        # When the sell date is within 10 days and the quality is 48 or less, increase quality by 2    
        elif self.sell_in <= 10 and self.quality <= 48:
            self.quality += 2
        # When the sell date has not pasted or the quality is equal to 49, increase quality by 1
        else:
            self.quality += 1

        self.sell_in -= 1

        return self.sell_in, self.quality




class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if "Aged Brie" in item.name:
                brie = AgedBrie(item.name, item.sell_in, item.quality)
                item.sell_in, item.quality = brie.update_quality()
            
            elif "Conjured" in item.name:
                conjured_item = ConjuredIteam(item.name, item.sell_in, item.quality)
                item.sell_in, item.quality = conjured_item.update_quality()            

            elif "Sulfuras" in item.name:
                # Quality is always 80 and the sell by date never changes
                pass

            elif "Backstage passes" in item.name:
                backstage_passes = BackstagePasses(item.name, item.sell_in, item.quality)
                item.sell_in, item.quality = backstage_passes.update_quality()

            else:
                basic_item = BasicItem(item.name, item.sell_in, item.quality)
                item.sell_in, item.quality = basic_item.update_quality()                 