# AUTO GENERATED FILE - DO NOT EDIT

export myeditor

"""
    myeditor(;kwargs...)

A MyEditor component.
MyEditor is a quill editor.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `value` (String; optional): The edited content
"""
function myeditor(; kwargs...)
        available_props = Symbol[:id, :value]
        wild_props = Symbol[]
        return Component("myeditor", "MyEditor", "custom_components", available_props, wild_props; kwargs...)
end

