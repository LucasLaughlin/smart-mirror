class DataEntry():
    def __init__(self, content, date = None):
        self.content=content
        self.date =date
        
    def display(self) ->str:
        if self.date: displayString = str(self.date) +" : "+ self.content
        else: displayString = self.content
        return """<li name="CalendarItemFive" class="list-group-item"> """ + displayString + """ </li>"""
        