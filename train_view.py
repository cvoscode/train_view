import plotly.graph_objects as go
class Viewer():
    def __init__(self) -> None:
        self.fig=go.FigureWidget()
        self.fig._config = self.fig._config | {'showLink':False,'displaylogo': False}
    
    def add_view_value(self,name:str, mode:str):
        """adds a new value to watch to the Figure

        Args:
            name (str): Name of the Variable
            mode (str): Can be any of the plotly.graph_objects modes: e.g. lines, markers
        """
        self.fig.add_scatter(name=name,mode=mode)

    
    def update_view_value(self,x,y,trace_number:int):
        """updates the values of a trace

        Args:
            x (_type_): _description_
            y (_type_): _description_
            trace_number (int): _description_
        """

        self.fig.data[trace_number].x=x
        self.fig.data[trace_number].y=y
    def append_view_value(self,x:float or int,y:float or int,trace_number:int):
        """appends a new value to the figure

        Args:
            x (float or int): Value to append to the x axis
            y (float or int): Value to append to the y axis
            trace_number (int): number of the trace to append to
        """
        # somehow we have to instaciate the tuple first, list did not work so we need to use tuples...
        if isinstance(self.fig.data[trace_number].x, type(None)):
            self.fig.data[trace_number].x=()
        self.fig.data[trace_number].x=self.fig.data[trace_number].x+(x,)
        if isinstance(self.fig.data[trace_number].y, type(None)):
            self.fig.data[trace_number].y=()
        self.fig.data[trace_number].y=self.fig.data[trace_number].y+(y,)
        
    def update_layout(self,title:str=None,xaxis:str=None,yaxis:str=None,showlegend:bool=True):
        """Updates the layout of the plot

        Args:
            title (str, optional): Title of the plot. Defaults to None.
            xaxis (str, optional): Name of the xaxis. Defaults to None.
            yaxis (str, optional): Name of the yaxis. Defaults to None.
            showlegend (bool, optional): Show a legend or do not. Defaults to True.
        """
        self.fig.update_layout(title=title,
                                xaxis=dict(title=xaxis),
                                yaxis=dict(title=yaxis),
                                showlegend=showlegend)
    
