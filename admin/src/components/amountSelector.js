import * as React from "react";
import { Field } from 'react-final-form';
import Slider from '@material-ui/core/Slider';

const AmountSelectorComponent = (props) => {
  console.log(props)
  let {input} = props
  return <Slider
      defaultValue={input.value}
      max={25}
      min={1}
      onChange={(e,value) => input.onChange(value)}
      aria-labelledby="discrete-slider-always"
      marks={ [{value:1, label: '1 cl'},{value:12, label: '12 cl'},{value:25, label: '25 cl'}] }
      step={1}
      valueLabelDisplay="on"
      valueLabelFormat={(x) => `${x} cl`}/>
}

export const AmountSelector = ({ source, record }) => <Field name={source} component={AmountSelectorComponent} />