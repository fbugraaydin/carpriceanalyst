class Advert:
    def __init__(self, year, km, price, address):
        self.year = year
        self.km = km
        self.price = price
        self.address = address

    def __str__(self):
        return "Year: {year}, Km: {km}, Price: {price}, Address:{address} \n".format(
            year=self.year,
            km=self.km,
            price=self.price,
            address=self.address
        )
