import os
import pandas as pd
import streamlit.components.v1 as components
from typing import Literal
# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("ag_grid"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "ag_grid",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:5173",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "ag_grid",
        path=build_dir
    )


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.

# https://www.ag-grid.com/vue-data-grid/localisation/
AGGridLocale = Literal[
    'AG_GRID_LOCALE_EG', 'AG_GRID_LOCALE_BG', 'AG_GRID_LOCALE_HK', 'AG_GRID_LOCALE_CN',
    'AG_GRID_LOCALE_TW', 'AG_GRID_LOCALE_HR', 'AG_GRID_LOCALE_CZ', 'AG_GRID_LOCALE_DK',
    'AG_GRID_LOCALE_NL', 'AG_GRID_LOCALE_FI', 'AG_GRID_LOCALE_FR', 'AG_GRID_LOCALE_DE',
    'AG_GRID_LOCALE_GR', 'AG_GRID_LOCALE_IL', 'AG_GRID_LOCALE_HU', 'AG_GRID_LOCALE_IT',
    'AG_GRID_LOCALE_JP', 'AG_GRID_LOCALE_KR', 'AG_GRID_LOCALE_NO', 'AG_GRID_LOCALE_IR',
    'AG_GRID_LOCALE_PL', 'AG_GRID_LOCALE_PT', 'AG_GRID_LOCALE_BR', 'AG_GRID_LOCALE_RO',
    'AG_GRID_LOCALE_SK', 'AG_GRID_LOCALE_ES', 'AG_GRID_LOCALE_SE', 'AG_GRID_LOCALE_TR',
    'AG_GRID_LOCALE_UA', 'AG_GRID_LOCALE_PK', 'AG_GRID_LOCALE_VN'
]

AGGridRowSelection = Literal[
    "single", "multiple"
]

def ag_grid(
        df: pd.DataFrame,
        column_defs,
        locale_text: AGGridLocale = "AG_GRID_LOCALE_BR",
        row_selection: AGGridRowSelection = "single",
        style: str="height: 200",
        key=None
    ):
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.

    row_data = df.to_dict(orient="records")

    component_value = _component_func(
        rowData=row_data,
        colDefs=column_defs,
        localeText=locale_text,
        rowSelection=row_selection,
        style=style,
        key=key,
        default={}
    )

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value
