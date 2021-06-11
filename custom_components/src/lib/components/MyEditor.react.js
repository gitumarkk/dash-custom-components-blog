import React from 'react';
import PropTypes from 'prop-types';

import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';

/**
 * MyEditor is a quill editor.
 */
const MyEditor = ({id, setProps, value}) => {
    return (
        <div id={id}>
            <ReactQuill
                onChange={(value) => setProps({value})}
                value={value || ''}
            />
        </div>
    );
};

MyEditor.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The edited content
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default MyEditor;
