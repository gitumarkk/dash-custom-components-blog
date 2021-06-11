# AUTO GENERATED FILE - DO NOT EDIT

myCalendar <- function(id=NULL, date=NULL) {
    
    props <- list(id=id, date=date)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MyCalendar',
        namespace = 'custom_components',
        propNames = c('id', 'date'),
        package = 'customComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
