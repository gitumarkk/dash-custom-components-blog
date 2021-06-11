import React from 'react';
import PropTypes from 'prop-types';

import dayjs from 'dayjs';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

/**
 * MyCalendar allows the user to select a date
 */
const MyCalendar = ({id, setProps, date}) => {
    return (
        <div id={id}>
            <Calendar
                onChange={(date) =>
                    setProps({date: dayjs(date).format('DD-MMM-YYYY')})
                }
                value={dayjs(date, 'DD-MMM-YYYY').toDate()}
            />
        </div>
    );
};

MyCalendar.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The date as a string
     */
    date: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default MyCalendar;
