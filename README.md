# TOC Project 2017

A telegram bot based on a finite state machine

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

there are four transactions departing from the initial state
each of transcation have four sequential states
at the end of sequential states it `go_back` to `user`

* user
	* Input: "go to state1" -> "go to state2" -> "go to state3" -> "go to state4"
		* Reply: "I'm entering state1"
        * Reply: "I'm entering state2"
        * Reply: "I'm entering state3"
        * Reply: "I'm entering state4"

	* Input: "go to state5" -> "go to state6" -> "go to state7" -> "go to state8"
		* Reply: "I'm entering state5"
        * Reply: "I'm entering state6"
        * Reply: "I'm entering state7"
        * Reply: "I'm entering state8"

	* Input: "go to state9" -> "go to state10" -> "go to state11" -> "go to state12"
		* Reply: "I'm entering state9"
        * Reply: "I'm entering state10"
        * Reply: "I'm entering state11"
        * Reply: "I'm entering state12"

	* Input: "go to state13" -> "go to state14" -> "go to state15" -> "go to state16"
		* Reply: "I'm entering state13"
        * Reply: "I'm entering state14"
        * Reply: "I'm entering state15"
        * Reply: "I'm entering state16"


## Author
[james831018](https://github.com/james831018)
