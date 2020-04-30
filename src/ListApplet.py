from Applet import Applet 

class ListApplet(Applet):
    def __init__(self):
        self.entries= list()
        self.title= ""
    
    def display(self) -> str:
        self.getData()
        html = """<div class="col m-4">
            <ul class="list-group">
            <li class="list-group-item"> <h5>"""+ self.title +"""</h5> </li>"""
        for item in self.entries:
            html = html + item.display()
        html = html + """</ul></div>"""
        return html