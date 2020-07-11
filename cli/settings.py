# mapping table between relay numbers and gpio input
relay_cmd = {
    1 : "gpio write 0 %d",
    2 : "gpio write 1 %d",
    3 : "gpio write 2 %d",
    4 : "gpio write 3 %d",
    5 : "gpio write 4 %d",
    6 : "gpio write 5 %d",
    7 : "gpio write 6 %d",
    8 : "gpio write 7 %d"
}

relay_init = {
    1 : "gpio mode 0 out",
    2 : "gpio mode 1 out",
    3 : "gpio mode 2 out",
    4 : "gpio mode 3 out",
    5 : "gpio mode 4 out",
    6 : "gpio mode 5 out",
    7 : "gpio mode 6 out",
    8 : "gpio mode 7 out" 
}