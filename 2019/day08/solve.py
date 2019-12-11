from functools import reduce

class Image:
    def __init__(self, string, width, height):
        self.width = width
        self.height = height
        self.string = string

    def _paint(self, lower, upper):
        layer = ''
        for lp, up in zip(lower, upper):
            if up == '2':
                layer += lp
            else:
                layer += up
        return layer 

    def get_layer(self, layer):
        i = layer * self.width * self.height
        return self.string[i:i+self.width*self.height]

    def get_row(self, layer, row):
        i = layer * self.width * self.height + row * self.width
        return self.string[i:i+self.width]

    def layer_count(self):
        return len(self.string) // (self.width*self.height)

    def decode(self):
        lays = [self.get_layer(i) for i in reversed(range(self.layer_count()))]
        return reduce(self._paint, lays)


width = 25
height = 6
with open('input', 'r') as f:
    encoded_img = Image(f.read().strip(), width, height)

# part 1
layers = [encoded_img.get_layer(i) for i in range(encoded_img.layer_count())]
layer = sorted(layers, key=lambda layer: layer.count('0'))[0]
print(layer.count('1') * layer.count('2'))


# part 2
s = encoded_img.decode().replace('0', ' ')
i = 0
for _ in range(height):
    print(s[i:i+width])
    i += width


