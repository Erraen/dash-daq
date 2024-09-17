# AUTO GENERATED FILE - DO NOT EDIT

#' @export
daqLEDDisplay <- function(id=NULL, backgroundColor=NULL, className=NULL, color=NULL, label=NULL, labelPosition=NULL, n_digits=NULL, size=NULL, style=NULL, theme=NULL, value=NULL) {
    
    props <- list(id=id, backgroundColor=backgroundColor, className=className, color=color, label=label, labelPosition=labelPosition, n_digits=n_digits, size=size, style=style, theme=theme, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'LEDDisplay',
        namespace = 'dash_daq',
        propNames = c('id', 'backgroundColor', 'className', 'color', 'label', 'labelPosition', 'n_digits', 'size', 'style', 'theme', 'value'),
        package = 'dashDaq'
        )

    structure(component, class = c('dash_component', 'list'))
}
