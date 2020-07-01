class Page:
    def __init__(self, index, link):
        self.index = index
        self.link = link

    def __str__(self):
        return "Page Index : {index}, Link: {link} \n".format(index=self.index, link=self.link)