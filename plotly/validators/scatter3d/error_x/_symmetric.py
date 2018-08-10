import _plotly_utils.basevalidators


class SymmetricValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='symmetric',
        parent_name='scatter3d.error_x',
        **kwargs
    ):
        super(SymmetricValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            **kwargs
        )