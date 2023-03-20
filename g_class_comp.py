# Uma classe chamada computador com seus respectivos atributos.

class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram 


pc = Computer("Sony", "Core i7", "16gb")  
print(pc.brand, pc.processor, pc.ram, sep=" - ")