import * as React from "react";
import { List, Datagrid, TextField } from 'react-admin';

const BottleContent = (record) => {
    
}

export const DrinkList = (props) => (
    <List {...props} pagination={null}>
        <Datagrid rowClick="edit">
            <TextField source="pump_number" />
            <TextField source="name" />
            <TextField source="total_volume" />
            <TextField source="volume_left" />
        </Datagrid>
    </List>
);