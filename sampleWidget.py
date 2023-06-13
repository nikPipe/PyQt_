try:
    from importlib import reload
except:
    pass

from import_module import *
from PyQt_ import sample_widget_template, color_variable, styleSheet


class sampleWidget(QWidget):
    def __init__(self, parent=None):
        super(sampleWidget).__init__(parent)


        self.sample_widget = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()
        self.color_variable = color_variable.COLOR_VARIABLE()
        self.styleSheet_widget = styleSheet.STYLESHEET()

        self.initUI()
        self.show()


    def initUI(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def(self)

        widgetList = [self.verticalLayoutWidget(), self.horizontalLayoutWidget(), self.gridLayoutWidget()]
        verticalLayout = self.sample_widget.verticalLayout_def(parent_self=widget, set_object_name='verticalLayout', widget_list=widgetList)

        return widget

    def verticalLayoutWidget(self):
        '''

        :return:
        '''
        widget = self.sample_widget.widget_def()

        #BUTTON ONE
        buttonOneObject = 'buttonOne'
        buttonOneObject_styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonOneObject, color=self.color_variable.red_color.get_value(),
                                                                       background=self.color_variable.green_color.get_value(),
                                                                          font_size=20, font_weight='bold')
        buttonOne = self.sample_widget.pushButton(set_text='Test', set_object_name=buttonOneObject, set_styleSheet=buttonOneObject_styleSheet)

        #BUTTON TWO
        buttonTwoObject = 'buttonTwo'
        buttonTwoObject_styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonTwoObject, color=self.color_variable.red_color.get_value(),
                                                                          background=self.color_variable.green_color.get_value(),
                                                                            font_size=20, font_weight='bold')
        buttonTwo = self.sample_widget.pushButton(set_text='Test', set_object_name=buttonTwoObject, set_styleSheet=buttonTwoObject_styleSheet)


        buttonList = [buttonOne, buttonTwo]
        verticalLayout = self.sample_widget.verticalLayout_def(parent_self=widget, set_object_name='verticalLayout', widget_list=buttonList)

        return widget

    def horizontalLayoutWidget(self):
        '''

        :return:
        '''
        widegt = self.sample_widget.widget_def()

        #BUTTON ONE
        buttonOneObject = 'buttonOne'
        buttonOneObject_styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonOneObject, color=self.color_variable.red_color.get_value(),
                                                                          background=self.color_variable.green_color.get_value(),
                                                                            font_size=20, font_weight='bold')
        buttonOne = self.sample_widget.pushButton(set_text='Test', set_object_name=buttonOneObject, set_styleSheet=buttonOneObject_styleSheet)

        #BUTTON TWO
        buttonTwoObject = 'buttonTwo'
        buttonTwoObject_styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonTwoObject, color=self.color_variable.red_color.get_value(),
                                                                            background=self.color_variable.green_color.get_value(),
                                                                                font_size=20, font_weight='bold')
        buttonTwo = self.sample_widget.pushButton(set_text='Test', set_object_name=buttonTwoObject, set_styleSheet=buttonTwoObject_styleSheet)


        buttonList = [buttonOne, buttonTwo]
        horizontalLayout = self.sample_widget.horizontalLayout_def(parent_self=widegt, set_object_name='horizontalLayout', widget_list=buttonList)

        return widegt

    def gridLayoutWidget(self):
        '''

        :return:
        '''

        widget = self.sample_widget.widget_def()

        #BUTTON ONE
        buttonOneObject = 'buttonOne'
        buttonOneObject_styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonOneObject, color=self.color_variable.red_color.get_value(),
                                                                            background=self.color_variable.green_color.get_value(),
                                                                                font_size=20, font_weight='bold')
        buttonOne = self.sample_widget.pushButton(set_text='Test', set_object_name=buttonOneObject, set_styleSheet=buttonOneObject_styleSheet)

        #BUTTON TWO
        buttonTwoObject = 'buttonTwo'
        buttonTwoObject_styleSheet = self.sample_widget.styleSheet_def(obj_name=buttonTwoObject, color=self.color_variable.red_color.get_value(),
                                                                            background=self.color_variable.green_color.get_value(),
                                                                                font_size=20, font_weight='bold')
        buttonTwo = self.sample_widget.pushButton(set_text='Test', set_object_name=buttonTwoObject, set_styleSheet=buttonTwoObject_styleSheet)

        buttonList = {}
        buttonList[buttonOne] = [0, 0, 0, 0]
        buttonList[buttonTwo] = [0, 1, 0, 0]

        gridLayout = self.sample_widget.gridLayout_def(parent_self=widget, set_object_name='gridLayout', widget_list=buttonList)




















