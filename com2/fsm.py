from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'go to state2'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'go to state3'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'go to state4'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'go to state5'

    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'go to state6'

    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == 'go to state7'

    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == 'go to state8'

    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == 'go to state9'

    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == 'go to state10'

    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == 'go to state11'

    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == 'go to state12'

    def is_going_to_state13(self, update):
        text = update.message.text
        return text.lower() == 'go to state13'

    def is_going_to_state14(self, update):
        text = update.message.text
        return text.lower() == 'go to state14'

    def is_going_to_state15(self, update):
        text = update.message.text
        return text.lower() == 'go to state15'

    def is_going_to_state16(self, update):
        text = update.message.text
        return text.lower() == 'go to state16'

    def on_enter_state1(self, update):
        update.message.reply_text("I'm entering state1")
        self.go_back(update)

    def on_enter_state3(self, update):
        update.message.reply_text("I'm entering state3")
        self.go_back(update)

    def on_enter_state2(self, update):
        update.message.reply_text("I'm entering state2")
        self.go_back(update)

    def on_enter_state4(self, update):
        update.message.reply_text("I'm entering state4")
        self.go_back(update)

    def on_enter_state5(self, update):
        update.message.reply_text("I'm entering state5")
        self.go_back(update)

    def on_enter_state6(self, update):
        update.message.reply_text("I'm entering state6")
        self.go_back(update)

    def on_enter_state7(self, update):
        update.message.reply_text("I'm entering state7")
        self.go_back(update)

    def on_enter_state8(self, update):
        update.message.reply_text("I'm entering state8")
        self.go_back(update)

    def on_enter_state9(self, update):
        update.message.reply_text("I'm entering state9")
        self.go_back(update)

    def on_enter_state10(self, update):
        update.message.reply_text("I'm entering state10")
        self.go_back(update)

    def on_enter_state11(self, update):
        update.message.reply_text("I'm entering state11")
        self.go_back(update)

    def on_enter_state12(self, update):
        update.message.reply_text("I'm entering state12")
        self.go_back(update)

    def on_enter_state13(self, update):
        update.message.reply_text("I'm entering state13")
        self.go_back(update)

    def on_enter_state14(self, update):
        update.message.reply_text("I'm entering state14")
        self.go_back(update)

    def on_enter_state15(self, update):
        update.message.reply_text("I'm entering state15")
        self.go_back(update)

    def on_enter_state16(self, update):
        update.message.reply_text("I'm entering state16")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_exit_state5(self, update):
        print('Leaving state5')

    def on_exit_state6(self, update):
        print('Leaving state6')

    def on_exit_state7(self, update):
        print('Leaving state7')

    def on_exit_state8(self, update):
        print('Leaving state8')

    def on_exit_state9(self, update):
        print('Leaving state9')

    def on_exit_state10(self, update):
        print('Leaving state10')

    def on_exit_state11(self, update):
        print('Leaving state11')

    def on_exit_state12(self, update):
        print('Leaving state12')

    def on_exit_state12(self, update):
        print('Leaving state13')

    def on_exit_state12(self, update):
        print('Leaving state14')

    def on_exit_state12(self, update):
        print('Leaving state15')

    def on_exit_state12(self, update):
        print('Leaving state16')
