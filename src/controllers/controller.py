class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_button_click(self):
        data = self.model.get_data()
        self.view.update_display(data)

    def update_model(self, new_data):
        self.model.set_data(new_data)
        self.view.update.display(new_data)

    def update_view(self):
        data = self.model.get_data()
        self.view.update_label(data)
        