# CAN bus visualization

This is the application part of the paper: "Visual analysis of CAN bus traffic".
It allows you get visual view of traffic and analyse CAN bus attacks.


![N|Solid](https://github.com/guardeec/canbus/blob/master/pic/DoS.png)

# How to visualize?
Run *visualization.html* via:
  - Server (you can also use IDE preview, for example [Brackets](http://brackets.io/index.html) LivePreview)
  - Google Chrome with [disabled](https://stackoverflow.com/questions/3102819/disable-same-origin-policy-in-chrome) web-security

You can select file in *visualization.html* using this line:
```javascript
d3.json("data/DoS.json", function (data) {
```
# I want to visualize my own dumps!
You can use *analyze.py* file (require Python 2.7). This file parse CAN bus raw CSV files from [HCLR dataset](http://ocslab.hksecurity.net/Datasets/CAN-intrusion-dataset). So if you bring your traffic to the same CSV data structure, you can use this *.py* file to create *.json* dataset that can be visualized.
The data structure of *analyze.py* input CSV files is next:

| Timestamp | CAN ID | DLC | DATA[0] | DATA[1] | DATA[2] | DATA[3] | DATA[4] | DATA[5] | DATA[6] | DATA[7] | Flag |
| --------- | ------ | --- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ---- |

# If you have some questions:

Max Kolomeets - *ITMO student / SPIIRAS junior R&D*.

E-mail: guardeecwalker@gmail.com

Telegram: http://t.me/guardeec


