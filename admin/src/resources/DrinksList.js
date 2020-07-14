import * as React from "react";
import { List, Datagrid, TextField, NumberField, LinearProgress } from 'react-admin';

const BottleContent = ({record}) => {
    console.log(record)
    let fillDegre = Math.round((record.volume_left / record.total_volume)*100)
    fillDegre = fillDegre > 100 ? 100: fillDegre
    fillDegre = fillDegre < 0 ? 0: fillDegre
    return <LinearProgress variant="determinate" value={fillDegre} />
}

export const DrinkList = (props) => (
    <List {...props} pagination={null}>
        <Datagrid rowClick="edit">
            <TextField source="pump_number" />
            <BottleContent/>
            <TextField source="name" />
            <NumberField source="total_volume" />
            <NumberField source="volume_left" />
        </Datagrid>
    </List>
);