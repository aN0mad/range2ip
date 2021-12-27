# range2ip
Parse CIDRs and IP ranges to single IP addresses

## Installation
range2ip utilizes [pipx](https://pipxproject.github.io/pipx/) to handle environment isolation from other tools. Installation for pipx can be found [here](https://pipxproject.github.io/pipx/installation/).

Step 1: Clone the repo and change directories
```text
┌──(root💀HOST)-[/opt]
└─# cd range2ip
```

<p></p>

Step 2: Install range2ip with pipx
```text
┌──(root💀HOST)-[/opt/range2ip]
└─# pipx install .
```
<p></p>

## Usage
```text
range2ip -h
usage: range2ip [-h] [-r RANGES] [-o OUTPUT] [-v]

Parse CIDRs and IP ranges to single IP addresses

optional arguments:
  -h, --help            show this help message and exit
  -r RANGES, --ranges RANGES
                        Text file with IP ranges on each line (default: None)
  -o OUTPUT, --output OUTPUT
                        Output file name (.txt is appended) (default: 1640623992.252814_output.txt)
  -v, --verbose         Print more info (default: False)
```

## Examples
```text
# range2ip -r ranges.txt -o newData

=================
Total ranges: 6
Total IPs: 540

Output file: newData.txt
=================       
```