import * as React from "react";
import DataProvider from "./DataProvider";
import { Admin, Resource } from 'react-admin';
import { DrinkList } from "./resources/DrinksList";
import { DrinkEdit } from "./resources/DrinksEdit";
import { DrinkCreate } from "./resources/DrinksCreate";
import DrinkIcon from '@material-ui/icons/LocalDrink';
import CoktailIcon from '@material-ui/icons/LocalBar';
import { CoktailList } from "./resources/CoktailList";
import { CoktailEdit} from "./resources/CoktailEdit";

const App = () => (
    <Admin dataProvider={DataProvider('')}>
        <Resource name="drinks" list={DrinkList} edit={DrinkEdit} create={DrinkCreate} icon={DrinkIcon}/>
        <Resource name="coktails" list={CoktailList} edit={CoktailEdit} create={CoktailEdit} icon={CoktailIcon}/>
    </Admin>
);

export default App;